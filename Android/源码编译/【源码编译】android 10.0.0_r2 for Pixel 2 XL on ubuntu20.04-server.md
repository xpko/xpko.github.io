# 【源码编译】android 10.0.0_r2 for Pixel 2 XL on ubuntu20.04-server

[【源码编译】android-13.0.0_r7 for Pixel 4 on ubuntu20.04-server](https://blog.csdn.net/qq_26914291/article/details/127729612)  
[【源码编译】android-12.1.0_r11 for Pixel 4 on ubuntu20.04-server](https://blog.csdn.net/qq_26914291/article/details/127748826)  
[【源码编译】android-11.0.0_r46 for Pixel 4 on ubuntu20.04-server](https://blog.csdn.net/qq_26914291/article/details/127748916)  
[【源码编译】android 10.0.0_r2 for Pixel 2 XL on ubuntu20.04-server](https://blog.csdn.net/qq_26914291/article/details/127512748)  
[【源码编译】android-9.0.0_r46 for Pixel 2 XL on ubuntu20.04-server](https://blog.csdn.net/qq_26914291/article/details/127748976)  
[【源码编译】android-8.0.0_r21 for Pixel 2 XL on ubuntu20.04-server](https://blog.csdn.net/qq_26914291/article/details/127630786)  

@[TOC](内容索引)
# 前言
感谢看雪，简书，CSDN等各个平台上的前辈的编译教程，感谢Google让android编译越来越简单，以前编译基本各种问题，现在直接一步到底，超级流畅
# 配置环境
- ubuntu20.04-server(已切换清华镜像)
- 4 core
- 8G RAM
- 2T disk
- 物理主机
- 必备代理，速度够快，建议20Mb/s以上
- Pixel 2 XL 手机一部
- 配置[proxychains](https://github.com/haad/proxychains)
# 选择分支
这里我选择android-10.0.0_r2，因为我看到几个逆向教程里都是使用的这个分支，所以选择这个分支方便逆向分析，至于具体原因猜测是该分支支持的机型比较多，支持机型列表：Pixel 3a XL、Pixel 3a、Pixel 3 XL、Pixel 3、Pixel 2 XL、Pixel 2、Pixel XL、Pixel，从Pixel到Pixel3都支持，而我就是用的Pixel 2 XL

> 注意：分支需要与设备型号匹配，并不是一个机型就可以通刷所有分支的，具体匹配列表参看：[Here](https://source.android.com/docs/setup/about/build-numbers#source-code-tags-and-builds)

# 下载源码
```bash 
sudo apt-get update

sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5-dev lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig python

mkdir ~/bin
export PATH=~/bin:$PATH

proxychains curl https://storage.googleapis.com/git-repo-downloads/repo -o ~/bin/repo
chmod a+x ~/bin/repo

mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY

git config --global user.name Your Name
git config --global user.email you@example.com

# -b 后面代号选择，访问：https://source.android.com/setup/start/build-numbers#source-code-tags-and-builds
proxychains repo init -u https://android.googlesource.com/platform/manifest -b android-10.0.0_r2

# -j 的数字根据机器性能而定
proxychains repo sync -c -j8

```
# 导入设备驱动(可选，刷入真实设备需要)

- 下载Pixel 2 XL对应版本驱动文件，地址：[taimenqp1a.190711.020](https://developers.google.com/android/drivers#taimenqp1a.190711.020)
- 将两个压缩包放入源码根目录
- 执行解压命令 `tar -zxvf xxxxx.tgz`
- 执行解压出的sh文件，一般是在`8.e.`条结束，在最后会让输入`I ACCEPT`，不要回车太快，否则直接跳过去了
- 执行完后可在源码根目录下找到vector目录
# 配置jdk
android-8.1.0_r1之前需要自己安装jdk，之后源码里就自带了，路径：prebuilts/jdk，所以android-8.0.0_r1之后就不用再配置jdk了
# 构建源码
```bash 
cd WORKING_DIRECTORY

sudo apt-get install libncurses5

export _JAVA_OPTIONS="-Xmx4g"

source build/envsetup.sh

lunch aosp_taimen-user

m 
```
> 这里循环执行m，报错就继续执行，有给修复提示，就按提示做，否则默认一直m，只要不是每次错误都一样
# 刷入镜像
```bash 
cd WORKING_DIRECTORY/out/target/product/taimen/
fastboot flashall -w
```
# 刷入镜像（远程服务器编译，本地Window）(On Xshell 5)
- xshell下
```bash
cd WORKING_DIRECTORY/out/target/product/taimen/
sz *.txt
sz *.img
```
- window下
切换到sz命令下载的目录，在该目录打开cmd，执行如下命令
```
set ANDROID_PRODUCT_OUT=./
fastboot flashall -w
```

# 编译Pixel 2 XL内核
> 内核源码并不在aosp里，需要单独下载，大概4.35GB \
> 各个机型的内核不一样，具体参看：https://source.android.google.cn/setup/build/building-kernels?hl=zh-cn
## 下载源码
```bash 
mkdir android-msm-wahoo-4.4-android10-qpr3

cd android-msm-wahoo-4.4-android10-qpr3

proxychains repo init -u https://android.googlesource.com/kernel/manifest -b android-msm-wahoo-4.4-android10-qpr3

proxychains repo sync -c -j8
```
## 切换到指定commitId
这个commitId可以通过查看手机内核版本获取，一般是-g{commitId}形式出现
- 显示提交详情，详情里有full_commitId
```bash 
repo forall -c 'git show $commitId'
```
- 切换到该提交
```bash 
repo forall -c 'git reset --hard $full_commitId'
```
## 编译源码
```bash 
# openssl/bio.h file not found
sudo apt-get install libssl-dev

# soong_zip: cammand not found
export PATH=/mnt/d/tool/android/android-10.0.0_r2/out/soong/host/linux-x86/bin:$PATH

build/build.sh
```
## 替换aosp内核
> aosp里替换上面编译后的内核，这里通过环境变量TARGET_PREBUILT_KERNEL指定，方便动态切换内核，具体看：https://source.android.google.cn/setup/build/building-kernels?hl=zh-cn#running
```bash 
cd android-10.0.0_r2

# 先初始化aosp编译环境，具体看上面构建aosp源码步骤

export TARGET_PREBUILT_KERNEL=/mnt/d/tool/android/kernel/android-msm-wahoo-4.4-android10-qpr3/out/android-msm-wahoo-4.4/dist/Image.lz4-dtb

m bootimage
```
> 之后按上面的<刷入镜像>步骤正常刷入即可
# 定制
- 修改代码
- `m <target module>`
- `make snod` (编译system.img，忽略依赖)
- `m`
- 定制时系统日志检查`dmesg | grep <tag>` or `cat /proc/kmsg | grep <tag>`
> 这里的\<target module\>在bp文件里指的是模块名，若是可执行文件就在bp里着cc_binary{}结构的模块，其name属性就是模块名。若是库，就找cc_library开头的，若是App就找android_app开头的....等等
## 修改system.img
由于在系统运行时，模块肯定处于占用中，这时是没法覆盖的，当然你也可以直接覆盖整个system.img文件，但谷歌官方固件肯定跟我们编译的固件不同，从运行后的系统就可以看到区别，应该是在原来系统源码上加了一些私有的东西，当然你也可以尝试下recovery模式下覆盖文件，但实际测试twrp进入recovery模式后，会出现很多问题，data分区加密需要格式化，system挂载不上等等。
最后剩下唯一可行的方案就是修改system.img文件了





## audit2allow运行环境修复
```bash 
sudo apt-get install python2
rm -rf /usr/bin/python
sudo ln -s /usr/bin/python2 /usr/bin/python
```
## root权限
// 看参考
## 默认开启USB调试(persist.sys.usb.config依然为none，防止检测usb连接)

- 开启USB调试
```java
//android-10.0.0_r2/frameworks/base/services/core/java/com/android/server/adb/AdbService.java#119
                // mAdbEnabled = containsFunction(
                //         SystemProperties.get(USB_PERSISTENT_CONFIG_PROPERTY, ""),
                //         UsbManager.USB_FUNCTION_ADB);
                mAdbEnabled = true;

```
- 自动处理USB验证
```java
//android-10.0.0_r2/frameworks/base/packages/SystemUI/src/com/android/systemui/usb/UsbDebuggingActivity.java#onCreate()
   @Override
    public void onCreate(Bundle icicle) {
        //......
        setupAlert();
        //....
        mAlert.getButton(BUTTON_POSITIVE).setOnTouchListener(filterTouchListener);
        //add code
        try {
            IBinder b = ServiceManager.getService(ADB_SERVICE);
            IAdbManager service = IAdbManager.Stub.asInterface(b);
            service.allowDebugging(true, mKey);
        } catch (Exception e) {
            Log.e(TAG, "Unable to notify Usb service", e);
        }
        finish();
    }

```
## 制作releasekey
- 源码根目录下创建create_key.sh
```bash 
#create_key.sh
subject='/C=CN/ST=Shanghai/L=Shanghai/O=marto/OU=marto/CN=marto.cc/emailAddress=android@marto.cc'
for x in releasekey platform shared media networkstack;
do
  ./development/tools/make_key ~/.android-certs/$x "$subject";
done

```
- 源码根目录执行`cp -r ~/.android-certs/releasekey.* build/target/product/security/`
- `testkey`->`releasekey`
```mk
# build/core/config.mk

# The default key if not set as LOCAL_CERTIFICATE
ifdef PRODUCT_DEFAULT_DEV_CERTIFICATE
  DEFAULT_SYSTEM_DEV_CERTIFICATE := $(PRODUCT_DEFAULT_DEV_CERTIFICATE)
else
  DEFAULT_SYSTEM_DEV_CERTIFICATE := build/target/product/security/releasekey
endif
.KATI_READONLY := DEFAULT_SYSTEM_DEV_CERTIFICATE
```
```mk
# build/core/Makefile

# The "test-keys" tag marks builds signed with the old test keys,
# which are available in the SDK.  "dev-keys" marks builds signed with
# non-default dev keys (usually private keys from a vendor directory).
# Both of these tags will be removed and replaced with "release-keys"
# when the target-files is signed in a post-build step.
ifeq ($(DEFAULT_SYSTEM_DEV_CERTIFICATE),build/target/product/security/releasekey)
BUILD_KEYS := release-keys
else
BUILD_KEYS := dev-keys
endif

```
- `m -j4`重新编译
## 修改设备属性
## 隐藏BL解锁
## 系统属性访问trace
```cpp
//bionic/libc/bionic/system_property_api.cpp

#include <async_safe/log.h>

__BIONIC_WEAK_FOR_NATIVE_BRIDGE
const prop_info* __system_property_find(const char* name) {
  char value[PROP_VALUE_MAX] = {0};
  system_properties.Get(name, value);
   async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call __system_property_find %s -> %s",name,value);
  return system_properties.Find(name);
}

__BIONIC_WEAK_FOR_NATIVE_BRIDGE
int __system_property_read(const prop_info* pi, char* name, char* value) {
  int ret= system_properties.Read(pi, name, value);
  async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call __system_property_read %s -> %s",name,value);
  return ret;
}

__BIONIC_WEAK_FOR_NATIVE_BRIDGE
int __system_property_get(const char* name, char* value) {
  int ret= system_properties.Get(name, value);
  async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call __system_property_get %s -> %s",name,value);
  return ret;
}


```
## 开启应用debuggable(ro.debuggable依然为0)
```java
//frameworks/base/core/java/android/content/pm/PackageParser.java#parseBaseApplication()

       // if (sa.getBoolean(
       //         com.android.internal.R.styleable.AndroidManifestApplication_debuggable,
       //         false)) {
            ai.flags |= ApplicationInfo.FLAG_DEBUGGABLE;
            // Debuggable implies profileable
            ai.privateFlags |= ApplicationInfo.PRIVATE_FLAG_PROFILEABLE_BY_SHELL;
       // }

```
## 修改屏幕默认休眠时间(单位：ms)
```xml
<!-- frameworks/base/packages/SettingsProvider/res/values/defaults.xml  -->
    <integer name="def_screen_off_timeout">36000000</integer>
```
## 屏幕锁定默认为“无”
```xml
<!-- frameworks/base/packages/SettingsProvider/res/values/defaults.xml  -->
<bool name="def_lockscreen_disabled">true</bool>
```
## 修改默认语言为中文
```shell
# build/tools/buildinfo.sh

# ..........

echo "# end build properties"

echo "# custom build properties"

echo "# default language"
echo "ro.product.locale=zh_CN"
echo "ro.product.locale.language=zh"
echo "ro.product.locale.region=CN"
echo "persist.sys.language=zh"
echo "persist.sys.country=CN"
echo "persist.sys.timezone=Asia/Shanghai"


echo "# end custom build properties"

```
## ptrace trace
```cpp
//bionic/libc/bionic/ptrace.cpp

#include <async_safe/log.h>

long ptrace(int req, ...) {
  //......
  
  va_end(args);
  
  async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call ptrace pid:%d,addr:0x%p",pid,addr);

  long result = __ptrace(req, pid, addr, data);
  if (is_peek && result == 0) {
    return peek_result;
  }
  return result;
}

```
## getenforce 强制返回Enforcing


# 更多逆向技术交流
加入星球《[逆向涉猎](https://t.zsxq.com/071NJKjZb)》
# 参考
- https://source.android.com/setup/develop
- [下载编译安卓源码(Google)](http://koifishly.com/2020/07/24/android/source-code/xia-zai-bian-yi-yun-xing-an-zhuo-yuan-ma/)
- [Android10源码定制(一) 制作完全Root版本](http://www.zhuoyue360.com/crack/34.html)
- [AOSP系统签名的生成以及替换](https://www.jianshu.com/p/bb5325760506)
- https://source.android.com/devices/tech/ota/sign_builds
- https://source.android.com/devices/bootloader/locking_unlocking?hl=zh-cn
- [Android 7.1修改默认的休眠时间](https://blog.csdn.net/qq_35003588/article/details/99567368)
- [aosp 更改默认语言、时区问题](https://balalals.cn/archives/aosp%E6%9B%B4%E6%94%B9%E9%BB%98%E8%AE%A4%E8%AF%AD%E8%A8%80%E6%97%B6%E5%8C%BA%E9%97%AE%E9%A2%98)
- [SELinux政策文件](https://source.android.com/security/selinux/implement)
- [构建Pixel2内核](https://www.modb.pro/db/375240) 
- [通过串口实时打印Android内核调试log信息](https://blog.csdn.net/zxc99408267/article/details/80789670)
- [adb如何打印kernel输出log](https://www.jianshu.com/p/9b657c3c3560)
- [第3章 内核调试手段之内核打印](https://blog.51cto.com/u_15315240/3212141)
- http://www.juneleo.cn/47a3736f9762/
- [[run_soong_ui] Error 1](https://stackoverflow.com/questions/51324238/aosp-build-stopped-subcommand-failed?answertab=active#tab-top)
- [源码编译（1）——Android6.0源码编译详解](https://bbs.pediy.com/thread-269575.htm#%EF%BC%882%EF%BC%89%E9%85%8D%E7%BD%AE%E9%A9%B1%E5%8A%A8%E6%96%87%E4%BB%B6)