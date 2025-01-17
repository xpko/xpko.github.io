### 编译Cydia插件



以该插件为例子：https://github.com/NyaMisty/Surge4Advanced

```
git clone https://github.com/NyaMisty/Surge4Advanced
cd Surge4Advanced
git switch remotes/origin/new
make clean & make
make package
```

然后成品deb包就可以在package/里找到了

若是要在rootless模式下安装

可以在Makefile文件开头增加以下两行

```makefile
ARCHS = armv7 armv7s arm64
ROOTLESS=1
```

control文件里修改Architecture属性为

```ma
iphoneos-arm64
```

然后重新执行

```shell
make clean & make
make package
```





