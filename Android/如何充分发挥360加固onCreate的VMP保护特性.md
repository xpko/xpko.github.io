# 如何充分发(白)挥(嫖)360加固onCreate的VMP保护特性

献丑了，下面不用看了，原来免费版支持通过注解 [@QVMProtect](https://bbs.kanxue.com/target-N47xcMwLQkEpIb29pdLKI9BY6iO2xqUlwvsvdNzpEbPcIPLDakSx82zg7_2BWpvKf2.htm) 来定制化VMP保护的函数，我一直以为这个功能是付费的....emmmm

--------



众所周知，360加固仅对Activity的onCreate函数进行了vmp加强保护，但一般我们的核心代码都不在该函数里，这样就起不到应有的保护作用了，那怎样才能把核心代码放到onCreate里呢？

## 开始探究

首先分析，360加固识别onCreate规则，一个继承Activity的类，并且该类下实现了Activity的onCreate函数，并在AndroidManifest.xml里注册该activity

```java
public class Request extends Activity {
    protected void onCreate(Bundle savedInstanceState) {
    }
}
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <application>
        <activity android:name="xxx.xxxx.Request" />
    </application>

</manifest>
```

但是这样的实现IDE会提示，无法通过编译

```java
Overriding method should call super.onCreate
```

直接加个注解即可，让它不提示

```java
public class Request extends Activity {
    @SuppressLint("MissingSuperCall")
    protected void onCreate(Bundle savedInstanceState) {
    }
}
```

360成功加固了该onCreate函数

![image-20250114162328243](./assets/image-20250114162328243.png)

然后是调用，一般常规的调用就是startActivity->进入系统代码->然后由系统实例化Activity->最后调用app里实现的onCreate函数，但其实app也可以自己实例化该activity，直接`new Request()`即可，但该实例化不要放在子线程里，否则会报

```log
Can't create handler inside thread Thread[Thread-6,5,main] that has not called Looper.prepare()
```

activity对象实例化后，就可以去调onCreate函数了，这里调用onCreate函数就没有线程限制了，任意线程都可以调用

这样就实现在任意线程主动调用onCreate函数了，虽然onCreate没有返回值，但是有Bundle参数，直接把返回值放在Bundle参数里即可

## 实际效果

比如核心代码是一个网络请求

```java
public class Request extends Activity {
    @SuppressLint("MissingSuperCall")
    protected void onCreate(Bundle savedInstanceState) {
        String urlString = "https://note.shlu.fyi";
        StringBuilder result = new StringBuilder();
        HttpsURLConnection urlConnection = null;

        try {
            URL url = new URL(urlString);
            urlConnection = (HttpsURLConnection) url.openConnection();
            urlConnection.setRequestMethod("GET");
            urlConnection.setConnectTimeout(10000); // 10秒
            urlConnection.setReadTimeout(10000); // 10秒

            int responseCode = urlConnection.getResponseCode();
            if (responseCode == HttpsURLConnection.HTTP_OK) {
                InputStream in = urlConnection.getInputStream();
                BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                String line;

                while ((line = reader.readLine()) != null) {
                    result.append(line);
                }

                reader.close();
                in.close();
            } else {
                result.append("响应码：").append(responseCode);
            }

        } catch (Exception e) {
            e.printStackTrace();
            result.append("异常：").append(e.getMessage());
        } finally {
            if (urlConnection != null) {
                urlConnection.disconnect();
            }
        }
        System.out.println(result);
    }

}
```

由于android系统限制，网络请求需要放在子线程里

```java
public class Main extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        Button request= findViewById(R.id.request);
        Request requestObj=new Request();//UI主线程实例化activity对象
        request.setOnClickListener(v->{
            new Thread(()->requestObj.onCreate(null)).start();//子线程里调用onCreate函数
        });
    }
}
```

这样就实现了核心代码的vmp保护

## 封装实现

不过这样使用起来肯定是不太方便的，比如函数参数和返回值的处理，为此笔者优化了下代码，封装了一个库： [VMP361](https://github.com/xpko/VMP361) 

使用时，直接继承其中的VMP361.Method类，把要保护的核心代码放入onCreate方法，然后在 AndroidManifest.xml 里注册即可

```java
public class Request extends VMP361.Method {

    @Override
    protected void onCreate(Bundle args) {//这里建议设为 protected， 防止被外部调用
        super.onCreate(args);//调用父类的onCreate解析参数
        String urlString = "https://note.shlu.fyi?arg0="+getArg(0);//获取参数
        StringBuilder result = new StringBuilder();
        HttpsURLConnection urlConnection = null;

        try {
            URL url = new URL(urlString);
            urlConnection = (HttpsURLConnection) url.openConnection();
            urlConnection.setRequestMethod("GET");
            urlConnection.setConnectTimeout(10000); // 10秒
            urlConnection.setReadTimeout(10000); // 10秒

            int responseCode = urlConnection.getResponseCode();
            if (responseCode == HttpsURLConnection.HTTP_OK) {
                InputStream in = urlConnection.getInputStream();
                BufferedReader reader = new BufferedReader(new InputStreamReader(in));
                String line;

                while ((line = reader.readLine()) != null) {
                    result.append(line);
                }

                reader.close();
                in.close();
            } else {
                result.append("响应码：").append(responseCode);
            }

        } catch (Exception e) {
            e.printStackTrace();
            result.append("异常：").append(e.getMessage());
        } finally {
            if (urlConnection != null) {
                urlConnection.disconnect();
            }
        }
        result(result);//返回结果
    }

}
```

其中getArg(0)，可以获取对应索引的参数，返回值为泛型，可以自动转换类型，result(result)将处理后的结果返回

接下来就可以调用了

```java
public class Main extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        Button request= findViewById(R.id.request);
        Button hook= findViewById(R.id.hook);
        Button code= findViewById(R.id.code);
        request.setOnClickListener(v->{
            new Thread(()-> System.out.println("qqqq:"+VMP361.createMethod(Request.class).call("aaa"))).start();
        });
    }
}
```

一行代码搞定：

```java
VMP361.createMethod(Request.class).call("aaa")
```

## 批量化操作(TODO)

将要想保护的函数或类加上注解，比如

```java
import x.vmp.VMP361
public class EncryptUtil {
    
    @VMP361.Protect
    public String encrypt(String data){
        return base64(aes(data));
    }
}
```

然后通过AS插件，自动化提取被注解的函数的代码，放到一个以<类名>+<函数名>命名的Activity里的onCreate方法里，并将该Activity注册到AndroidManifest.xml里，最后再通过上面说的一行代码调用即可

```java
import x.vmp.VMP361
public class EncryptUtil {
    
    @VMP361.Protect
    public String encrypt(String data){
       return VMP361.createMethod(EncryptUtil_encrypt.class).call(data)
    }
}
```

```java
import x.vmp.VMP361
public class EncryptUtil_encrypt extends VMP361.Method {
    
    @Override
    public void onCreate(Bundle args){
        super.onCreate(args);
        result(base64(aes(getArg(0))));
    }
}
```

当然，这只是一种最简单的函数，实际函数可能要复杂的多，比如涉及外部变量和函数调用等等

## 基于成品APK做批量化操作(TODO)

还有一种方式不是基于AS插件，而是直接对apk进行操作，通过dexlib等类似的工具直接解析重构dex和AndroidManifest.xml文件，看看后面有空时间再搞吧，或者有做过这方面研究的大佬也可以试试

不过不确定360加固保护onCreate的个数有没有限制，有知道的大佬可以评论区说下
