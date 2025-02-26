# 安装
## MacOS
* `$ sudo /bin/sh -c "$(curl -fsSL https://static.palera.in/scripts/install.sh)"`
# 越狱
越狱前需要清除锁屏密码，这里测试用的iPhone X (A11) (iOS 16.6.1)
## MacOS
* 打开一个命令行窗口
* `$ palera1n`
* 当出现日志`<Info>: Press Enter when ready for DFU  mode`时点击回车键
* 按提示进行操作进入DFU模式
* 等待进入PongoOS (手机上显示出logo)
* 重新插拔数据线
* 这时手机界面会出现运行日志信息
* 等待后续执行完成进入iOS系统后
* 稍等片刻后，桌面会出现一个palera1n应用
* 进入palera1n应用安装Sileo应用
* 进入Sileo安装所需插件即可

## 后续

安装sileo后有一个大问题，就是不能再安装iphone-arm架构的插件了，只能安装iphone-arm64的插件，也就说一些老插件将不能使用了

其中包括appstore++，不过这个可以通过巨魔商店安装

## FAQ
* 若是越狱后重启系统了怎么办？
  重新执行一遍上面的步骤

* 若是设置了手机密码 (包括面容ID，指纹ID) 导致手机重启怎么办？
  恢复出厂设置后执行一遍上面的步骤

* Type-C转Lightning和PD快充线支持吗？

  不支持? 我实际测试支持的啊，难道是第一次不行，后续第二次以后可以
# 参考
- [Installing palera1n](https://ios.cfw.guide/installing-palera1n/#running-palera1n-1)
- [Palera1n越狱简体中文，iOS15.0~16.7越狱支持Mac/Linux/U盘多平台](https://dkxuanye.cn/?p=6813)
