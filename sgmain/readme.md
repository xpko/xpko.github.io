## 架构分析

|   组件   |        类         |        说明        |
| :------: | :---------------: | :----------------: |
|  初始化  |   SecurityInit    |   负责全局初始化   |
|   异常   |   JAQException    |    接口调用异常    |
| 安全接口 | SecuritySignature | 安全签名、白盒签名 |
| 安全接口 |  SecurityCipher   | 安全加密、白盒加密 |
| 安全接口 |  SecurityStorage  |      安全存储      |

## 静态数据加密组件

```java
package com.alibaba.wireless.security.open.staticdataencrypt;

import com.alibaba.wireless.security.framework.InterfacePluginInfo;
import com.alibaba.wireless.security.open.IComponent;
import com.alibaba.wireless.security.open.SecException;

@InterfacePluginInfo(pluginName = "main")
/* loaded from: I:\So库_6.3\classes.dex */
public interface IStaticDataEncryptComponent extends IComponent {
    public static final int ALGORITHM_MAX_NUMBER = 19;
    public static final int OPEN_ENUM_CIPHER_AES128 = 16;
    public static final int OPEN_ENUM_CIPHER_AES192 = 17;
    public static final int OPEN_ENUM_CIPHER_AES256 = 18;
    public static final int OPEN_ENUM_CIPHER_ARCFOUR = 3;

    byte[] staticBinarySafeDecrypt(int i, String str, byte[] bArr, String str2) throws SecException;

    byte[] staticBinarySafeDecryptNoB64(int i, String str, byte[] bArr, String str2) throws SecException;

    byte[] staticBinarySafeEncrypt(int i, String str, byte[] bArr, String str2) throws SecException;

    byte[] staticBinarySafeEncryptNoB64(int i, String str, byte[] bArr, String str2) throws SecException;

    String staticSafeDecrypt(int i, String str, String str2, String str3) throws SecException;

    String staticSafeEncrypt(int i, String str, String str2, String str3) throws SecException;
}
```



## 模拟加载libsgmain.so

```java
public void sgmain(){
        String libDir=getApplicationInfo().nativeLibraryDir;
        String sgmainPath=libDir+"/libsgmain.so";
        String sgmainOptDir=getDir("sgmain",MODE_PRIVATE).getAbsolutePath();
        log("path:"+sgmainPath);
        PathClassLoader sgmainClassLoader=new PathClassLoader(sgmainPath,sgmainOptDir,getClassLoader());
        try {
            log("sgmain classloader:"+sgmainClassLoader);
            Class<?> sgmainCls=sgmainClassLoader.loadClass("com.alibaba.wireless.security.mainplugin.SecurityGuardMainPlugin");
            log("main class:"+sgmainCls);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }


    }
```
这里直接加载SecurityGuardMainPlugin以及同包下的R类会报错，而加载同dex下的com.taobao.dp.util.ZipUtils类却不会报错\
进一步分析，可以发现ZipUtils类所在包只有它一个类，并且其仅调用了系统Api\
所以可以得出结论：若同包下任一类调用了未加载的类，则该包下的所有类都将无法正常加载
