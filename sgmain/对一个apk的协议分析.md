# 对一个apk的协议分析

> 转：https://bbs.kanxue.com/thread-258114.htm

过年的时候看见一个apk，因为肺炎在屋头宅的发霉，拿出来玩玩，小白图个乐，大佬乎喷。

**Apk信息**

![img](./images/840122_ZA5TBNPQDDGN4ZB.png)

APK下载地址：[So库_6.3.apk](./assets/So库_6.3.apk)

这个app的协议是明文，只有一个sign签名。

**1APK的协议**

长链接的心跳

**![img](./images/840122_6ZD8RUYBC7C9PM6.png)**

返回值

```json
{"cod":"0","type":"5","msg":"\u83b7\u53d6\u6210\u529f",
 
"username":"ii12qqaa",
 
"vip":"\u666e\u901a\u4f1a\u5458","time":"8888888888","jifen":"0","login":"106",
 
"userid":"4232206e2a",
 
"token":"9f1ff9900178b5d0fe3db2a37d078ac5201c02380ebb0ba71a3bbf71bb2a8b2c0e18907e0383e8341dc00ee45fbc6923be0313f558197894"}
```

登录和注册

![img](./images/840122_CG2ZXU5ZAKB5P3F.png)

Type 1=登录 2=注册

Username 和password 是账户和密码

imei手机序列号

t是时间戳

sign是加密验证

返回值：

```json
{"cod":"0","type":"2",
 
"msg":"\u6ce8\u518c\u6210\u529f",
 
"username":"yyyyyy1234qq",
 
"vip":"\u666e\u901a\u4f1a\u5458",
 
"time":"8888888888","jifen":"0","login":"0","userid":"06ef899b13",
 
"token":"9f1ff9900178b5d0fe3db2a77951decf2913053b5cbb0ba71a3bbf71bb2a8b2c0e18907e0383e8341dc00ee45fbc6923be0313f558197894"}
```

2，搜索协议的逻辑

Name是搜索内容

![img](./images/840122_H93KVC89FS3ZCF7.png)

应用上点击列表后向服务器发送 urn：btih： ，时间戳，sign

![img](./images/840122_46ND366MES2D9ZN.png)

返回值

```json
{"msg":"0",

"list":[{"name":"1.rm",

"data":"83a371d890c1178e8ecc8c060f17d2acf4a0eff707955035be407f7ce707d8ed49d5689a4abbffb8", "size":""}]}
```

再次在应用上点击

![img](./images/840122_PEPAD8JNPXSPMYY.png)

返回值：

```json
{"url":"http://120.76.250.16/video.php?host=sz.btfs.mail.ftn.qq.com&code=87d1e08d092c1d05527947754d542095aade3db0cf4619df17e81d10b6e414c4fe101e3622bbcc09f45404c17b601e05d2861bfb4799b740e087e2d94ab886f7&data=83a371d890c1178e8ecc8c060f17d2acf4a0eff707955035be407f7ce707d8ed49d5689a4abbffb81d30aadc7fb85e082658c7","cookie":"b4d29c58","msg":"0"}
```

这个就是视频源了，开始寻找sign的签名算法。

**2 apk源码**

在com.Soku. jxActivity的内部类madaper中onBindViewHolder方法发送hash以及data拿到视频地址

![img](./images/840122_H9E83RQE89PPTTB.png)

sign是调用com.Soku.Sign.getsign方法取返回值,传入的参数为 hash+time

（BuildConfig.VERSION_NAME的值是 6.3"）

![img](./images/840122_ZA7QKAWA4SC6AR4.png)

接下来调用 suritySignature.sign(),这个 类位于ibaba.wireless.security.jaq.SecuritySignature;

（SecureSignatureDefine.OPEN_KEY_SIGN_INPUT值为"INPUT"）

![img](./images/840122_77WFZHYE683TSVN.png)

之后是一个接口类IsecureSignatureComponent；他的实现在lib\armeabi\d1libsgmain.so中

但是这并不是一个so文件而是一个jar包。

我通过ddms绘制函数轨迹得到完整的调用链。

com.alibaba.wireless.security.a.h.a.sign()->

com.taobao.wireless.security.adapter.a.b.a()->  //判断传入的参数map类型

com.taobao.wireless.security.adapter.a.b.a();-> //重载的函数， 这个函数的作用是将Unicode字节码转成UTF-8

com.taobao.wireless.security.adapter.a.b.a();-> 

com.taobao.wireless.security.adapter.JNICLibrary.doCommandNative（int i, Object... objArr）；

最后调用了native函数。传入的参数为10401，new object{ hash+time+“6.3“，"3be780bc-8cf2-446c-9e03-de3a8fd9d0a7", Integer.valueOf(3),"0335"}

![img](./images/840122_DSTXYUQHYE79HKP.png)

![img](./images/840122_84W8XDGCGTEAHVQ.png)



接下来就开始对 libsgmain-5.4.56.so的分析

**3 libsgmainso.so的分析**

Jar包中的lib\armeabi\libsgmain-5.4.56.so，简单粗暴的将所有节头的偏移和大小置0后使用ida打开

这个so里面很多的流程混淆，具体可以参考这篇大佬的文章

[详细分析一款移动端浏览器安全性](https://www.anquanke.com/post/id/179080)

https://www.anquanke.com/post/id/179080

很多的函数并不能F5 

经过分析，函数开始处与函数结束处取一个内存中的值判断是否相等，如果不相等就跳转另一个地址

并且这个值并不参与运算中来，所以修改后并不影响我们的分析并且可以愉快的F5了

![img](./images/840122_HC3C79H476S6QQN.jpg)![img](./images/840122_SEJ7HCQJVRT7ZUE.png)

执行流程

首先so会去寻找 Boolean，String，Integer并做方法全局化引用 。

然后0xb9b0处解密加载

com/taobao/wireless/security/adapter/common/HttpUti，

解密 函数 sub_903F0 他的第一个参数是要解密的数据，第二个是返回值，三是 要解密的数据的大小

 首先申请一段56byte的内存(就叫malloc_56)再申请11byte的内存，将后面这个11byte的内存地址放入 malloc_56 的首地址。

这 11byte的内存存入的是10字节的密钥RC4算法， malloc_56[1]是0， malloc_56[2],是11，后面的都是一些函数地址了

![img](./images/840122_ETWV9QGW7QHT3JY.png)

密钥DcO/lcK+h? m3c*q@ （好像其他版本的密钥都是一样的）

![img](./images/840122_WEAAK8Q6PSRP4SZ.png)

![img](./images/840122_EDQ4W8N27WWHZE2.png)

接着再申请一个malloc_56，首地址存放要解密的数据地址。通过一个函数75DDA里的switch去调用sub_7C700

这就是RC4解密函数

RC4_Initialization初始化xor盒子

RC4_Decrypt解密

![img](./images/840122_VES5CSNWAFSVZHX.jpg)

sub_7CA82 就是 RC4_Decrypt

![img](./images/840122_NTX8SVH866MBQQH.png)

经过几次解密加载其他一些类后才会在偏移0xB986解密并加载com.taobao.wireless.security.adapter.JNICLibrary。

![img](./images/840122_UN7QYKRNC2K77EV.png)

在JNICLibrary加载之后并不会马上调用RegisterNatives函数，而是继续解密加载其他的类并创建全局变量。最后在偏移0xbdce处注册doCommandNative函数，注册函数地址为0xbc38。

![img](./images/840122_NBE9KPU8PFKDDRT.png)

doCommandNative 函数， doCommandNative 的返回值是v6，这个值是由loc_9CD0函数得到的

![img](./images/840122_5RATMK2TRBKCZFU.png)

可以看到返回值v9是由off函数得到的，这个函数由sub_9630解密得出 doCommandNative传入的参数为1，4，1，1，m_off，0。

得到的地址为0x29d0d

![img](./images/840122_QE5ANUPU4HZQF4D.png)

m_off + 16 是Java传入的objarray，m_off + 12是env（这个方法到sub_29F9C并没有结束，只是跳转过去了而已）

```c
void __fastcall 29E6C(int m_off, _DWORD *a2, int a3, int a4, int a5, int a6, )
{
  v21 = m_off;
  v22 = *(_DWORD *)off_ABBA8;//获得这个位置的值在函数末尾再次获取
  *a2 = 99;
  v23 = *(_DWORD *)(m_off + 16);
  (*(void (**)(void))(**(_DWORD **)(m_off + 12) + 692))();// JNI::GetObjectArrayElement 
  v24 = *(_DWORD *)(v21 + 12);
  sub_9A568();//处理age[0] (hash+time+6.3)
  v25 = *(_DWORD *)(v21 + 16);
  sub_9C6E0(*(JNIEnv **)(v21 + 12));//处理age[1] key
  sub_9C7AC(*(_DWORD *)(v21 + 12), *(_DWORD *)(v21 + 16), 2);//处理age[2] 调用intValue
  v26 = *(_DWORD *)(v21 + 16);
  sub_9C6E0(*(JNIEnv **)(v21 + 12));处理age[3]
  sub_29F9C()
}
```

sub_9A568函数 malloc一段内存空间，大小为ArrayLength*4 

![img](./images/840122_ZBG7BQPUZFUWZ43.png)

这里有个小bug

```c
     v8 = ((int (__fastcall *)(JNIEnv *, int, int))(*v4)->GetObjectArrayElement)(v4, v12, v7) == 0;
        v9 = 0;
        if ( !v8 )
          sub_9A138();
        *(_DWORD *)(v13 + 4 * v7++) = v9;
```

if(!v8)? ? V8是objectarray,获取成功了直接丢了不要？？？以至于后面对这个malloc加载获取值时 LDR R0 ，0x0000000？？？

困扰了我好多天，还以为后面还有函数对这个malloc做了操作

汇编代码

![img](./images/840122_6E6RFN8H3YM4CZR.png)

BLX R3就是去执行的GetObjectArrayElement。

BEQ相等则跳转，转换成伪c 应该是if（v8）

![img](./images/840122_7JXU3WSWS26FW53.png)

在sub_9A138函数中调用Java层方法String.getBytes ( 刚刚得到的ObjectArray )，

再得到它的ArrayLength和ByteArrayElements

申请malloc空间大小为56(malloc_56)，跟解密类名一样的结构体

再将 ByteArrayElements拷贝到 malloc_arr里面 ， sub_9A568函数结束.

![img](./images/840122_XVDT8RG6M4AG3JQ.png)



处理key的函数sub_9C6E0与这个差不多 获取key的ObjectArray，调用GetStringUTFChars，申请malloc_32,malloc_128,将 malloc_128地址放入 malloc_32[0],

大小放入 malloc_32[2],再就是一些函数地址。之后将utf8格式的key拼接到 malloc_32后面

![img](./images/840122_32MY25533JGMU54.png)

![img](./images/840122_XZG8FEB72H2DXBC.png)

 sub_9C7AC函数调用java方法intValue拿到返回值

后面还有一个解密函数sub_903F0，直接运行一下返回值是0

对Java层传递过来的参数就处理完了

后面对 sub_9A568的返回值再次处理，申请malloc_8 

```c
 malloc_8= (_DWORD *)malloc_0(8);
  if ( !malloc_8)
  {
    sub_A1308(0, v22, v23, v24, 0, v22);
    __asm { LDCL            p15, c15, [R8], {0xFF} }
  }
  *malloc_8= 0;
  malloc_8[1] = 0;
 v23 = 4 * number;
  *malloc_8 = **(_DWORD **)(hashobj + 4 * number);
  malloc_8[1] = *(_DWORD *)(*(_DWORD *)(hashobj + 4 * number) + 4);
  *(_DWORD *)(malloc_off+ 4 * number) = malloc_8;
```

malloc_off是解密函数执行完之后申请的一块 ArrayLength*4 大小的内存（ sub_9A56 里的 ArrayLength ）



![img](./images/840122_7MA8YTBM6NV8WYQ.png)



之后调用 sub_46708函数 传入malloc_off的指针和一个值为0x63的指针

 sub_46708 函数一共有三次对 0x9db0 的调用，没有获取任何返回值，不知道是干什么的。。

![img](./images/840122_4W8CQ2U42CJQXEJ.png)

这个函数地址是0x9db0 就是doCommandNative 解密处理参数的函数



然后偏移0x46BD2 处是个 Switch r1的值就是0x4977c

![img](./images/840122_QGRS9T3G898AMY9.png)

0x4977c 里面有个很大switch循环，不知道为什么还不能 Specify switch idiom 。只能将就看了

![img](./images/840122_CMF8PWWAC9CXPAN.png)

switsh_2

![img](./images/840122_BVZDQGP5DA88R8W.png)

这段数据怎么来的我还没找到，不过我重打包apk和修改key的值都不会正常返回sign，这段数据应该就是apk的签名了，这四层switch循环弄得像个迷宫一样

![img](./images/840122_U9WFADEWBXW5RDX.jpg)

key_2并不是由key加密或者其他方式得来的，猜测于apk的签名验证有关

最后的sign签名算法是在0x75dda方法里的case0x17里面。偏移0x76ff6,传入的两个参数都是malloc_56结构体，第一个结构体的值是key2，第二个结构体的值是hash+time+”6.3“（http心跳检测时就为time+“6.3”） 



```c
int __fastcall Decryptkey(int key2_malloc, int hash)
{
hash_ = hash;
  v48 = *off_ABBA8;
  v3 = 0;
  if ( key2_malloc )
  {
    if ( hash )
    {
      key2_size = *(key2_malloc + 4);
      if ( key2_size )
      {
        if ( *(hash_ + 4) )
        {
          if ( key2_size < 65 )
            v5 = (*(key2_malloc + 40))();       // 创建个malloc_56结构体，将key2copy过去
          else
            sub_78530();
          v7 = v5;
          m_key2 = 0;
          if ( v5 )
          {
            v9 = *(v5 + 4) == 0;
            v10 = 0;
            v11 = 0;
            v3 = 0;
            if ( !v9 )
            {
              v44 = mirror_key2_1;
              key2 = v7;
              v45 = v7;
              aeabi_memclr4(mirror_key2_1, 64);
              aeabi_memclr4(mirror_key2_2, 64);
              memcpy8(mirror_key2_1, *key2, key2[1]);
              memcpy8(mirror_key2_2, *key2, key2[1]);
              i = 0;
              do
              {
                mirror_key2_1[-i] ^= 0x36u;
                mirror_key2_2[-i] ^= 0x5Cu;
                --i;
              }
              while ( i != -64 );
              sub_97DA4();                      // 申请 malloc_56_100
              m_key2 = malloc_56_100;
              (*(malloc_56_100 + 12))();        // copy mirror_key2_1
              (*(m_key2 + 48))(m_key2, hash_);  // mirror_key2_1后面加上hash
              sub_78530();                      // 这里面的算法不想看了
              v16 = v15;
              v11 = 0;
              if ( v15 )
              {
                v3 = 0;
                v7 = v45;
                if ( *(v15 + 4) )
                {
                  sub_98594();                  // 申请malloc_56,里面的数据大小为0x40,并copy过去mirror_key_2_2
                  v18 = v17;
                  (*(v17 + 48))();              // 在刚刚申请的malloc_56的数据mirror_key2_2后面拼接上hash
                  sub_78530();                  // 再次执行这个函数执行后的返回值就是key_3
                  v11 = v18;
                  v7 = v45;
                  v3 = v19;
                }
              }
              else
              {
                v3 = 0;
                v7 = v45;
              }
              v10 = v16;
            }
          }
          else
          {
            v10 = 0;
            v11 = 0;
            v3 = 0;
          }
          v20 = v10;
          free_malloc56(v7, v7, v11, v6, v43, v44, v45, v11);
          free_malloc56(m_key2, v21, v22, v23, v24, v25, v26, v27);
          free_malloc56(v20, v28, v29, v30, v31, v32, v33, v34);
          free_malloc56(v41, v35, v36, v37, v38, v39, v40, v41);
        }
      }
    }
  }
  result = *off_ABBA8 - v48;
  if ( *off_ABBA8 == v48 )
    result = v3;
  return result;
}
```



本来想把算法复现的，可惜调试调试着就蒙圈了[捂脸] [捂脸] ，现在肺炎也快过去了，不玩了开始找工作去，哈哈哈。

![img](./images/840122_5RZ6U699H9MNUSM.gif)

就这样吧，我已经把原版的so发了出来，签名函数位置也说了，大佬们有兴趣可以去看看。

这个函数返回值是一个malloc 大小0x14的数据(取个名字叫key_3)，经过算法



```c
  do
          {
            _byte = *(*key_3 - i);              // 作用
            v7 = (_byte >> 4) + 87;             // 循环获取key_3里的一个byte值
            if ( _byte >> 5 <= 4 )              // 如果byte小于0x80,就将byte逻辑右移4位后逻辑或上0x30
                                                //     不小于就byte逻辑右移4位后加上87(0x57)
              v7 = (_byte >> 4) | 0x30;
            offset = 2 * i;
            *(*sign - 2 * i) = v7;              // 得到的值放入sign(结果)中 i是为负数
            v9 = _byte & 0xF;                   // byte与0xf,结果小于0xa就或上0x30
                                                //           否则结果加上0x5c
                                                // 熟悉ascll码就知道0x30-0x39对应0-9，0x61-0x7a对应小写的字母
            if ( v9 < 0xA )
            {
              v11 = v9 | 0x30;
              sign_off = *sign - offset;
            }
            else
            {
              sign_off = *sign - offset;
              v11 = v9 + 87;
            }
            *(sign_off + 1) = v11;              // 放入sign中
            --i;
            key_3 = key_3_;
          }
          while ( -var_0x14 != i );
```

扩展成0x28的数据，这个就是最终的sign了



最后这个token 通过抓包改登录协议的imei或者重新注册账号去登录，连我换几个热点都是返回一样的值，估计是使用更底层的设备id加密得到的值，，，这就超出了我的认知了，还望大佬们提示一下。

[[注意\]APP应用上架合规检测服务，协助应用顺利上架！](https://www.kanxue.com/manxi.htm)



------

**补充 By shlu**

经在android 14上测试，发现sign固定返回607 ？？android版本问题？有联网操作？？



