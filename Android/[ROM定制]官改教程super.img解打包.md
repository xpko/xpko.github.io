# 【ROM定制】官改教程:super.img解打包！

> 转：https://www.coolapk.com/feed/40147757?shareKey=YzNiODgyZWI1Mzc2NjM1Nzc5MmQ~&shareUid=11751112&shareFrom=com.coolapk.market_12.4.2

 看到很多人貌似都不会1,特此简单的写一下，
 此文参考了[@上下五千年666666](https://www.coolapk.com/u/上下五千年666666) 和[@tong1298](https://www.coolapk.com/u/tong1298) 二位大佬的教程，特加提炼

![img](./assets/1165d357dc04251a1306ff499be1ea00.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑


 需要用到的工具以及获取方式:

![img](./assets/71b6b944dd3b26cb35f7707e31ae1145.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

Termux：用来安装TIK，以及操作解打包
 获取：https

![img](./assets/ce7f4b4e723f0a1e13885eda57b111c7.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

://lecloud.lenovo.com/share/qHeZixSqRNLganZU（密码：i9qp）
 解压后恢复备份，需要root权限

![img](./assets/1b8319aab4033d57c52398bbcd59d498.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

DNA-Android：用来合并Super分段和去除vb验证
 获取：需要在大佬群文件内查找，入口在[@tao1996](https://www.coolapk.com/u/tao1996) 主页

![img](./assets/488cd6afef864392a92dbfef9c3dfb15.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

在这里面需要用到最新版的工具箱和插件里的合并super文件包括去除vb插件

Tiny Fastboot Sript:可以不用自己写脚本。
 获取：相信大家都有吧！
 ～～～～～～～～～～～～～～～～～～～～～～～～～～～～～
 废话不多说，即刻开始讲解。
 1,首先我以EU最新版为例

![img](./assets/966d89c3985fa2ec60f260c0659b1e15.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

包都是现下

2,打开mt管理器解压Rom包，

![img](./assets/6bf5f196892505ce1a18c12b5ef83e30.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

3,打开DNA ANDROID，授予存储与root权限
 之后新建工程，
 之后打开mt管理器，把super分段镜像0-11移动到dna工程目录

![img](./assets/f6befd94d873f640ba7730e052ef46c7.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

打开Dna安卓工具，点击工程菜单，点击插件功能，点击合并分段super插件

![img](./assets/9ea4bc15d355c4a90f42b9a10aacb1b7.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

这样就已经合并完了12g是正常的
 然后新建打开dna工程，打开mt管理器把vbmeta和vbmeta_system.img两个文件移动到新工程目录，

![img](./assets/d98497523ecd89f5b45cdc9de7481bf1.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

再次打开dna安卓，插件功能里找到去除vb验证执行，out目录内是已经输出的去验证文件，然后把它们都移动回原压缩包

![img](./assets/6fea42902afe7323daa7373dba97468b.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

4,打开termux输入su获取权限

![img](./assets/8c658e7c820135e953a3759b549ae38b.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

然后，退出应用长按应用图标进入设置，点击权限授予允许管理所有！！！

![img](./assets/0af9ef00afadd19503fa246a42da315b.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

之后把应用强行停止再进入，输入ubuntu进入TIK

![img](./assets/f59fc7305c2dab4affd584651ab32822.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

必须操作上一步，吧应用强行停止

5,打开mt管理器解压Rom包，实际在tik解压也行，楼主习惯使用mt。

 6,在tik创建任务。注意不要使用中文！

![img](./assets/96cc17cae94cc1629f6f77e838d8deca.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

我这里创建的是“0”

然后把dna安卓里合并的super移动到tik项目里

 tik的项目目录是/data/data/com.termux/files/home/ubuntu/root/TIK/你创建的项目名称

 之后输入2选择解包菜单

![img](./assets/8a6ccb4daec081b33b6882964380539c.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

输入0,分解所有文件

![img](./assets/8b2022cc1dbe3b459da0512cfbb19b95.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

分解完后是这样的

![img](./assets/589a7100336a8452eb735caf3c5358f5.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

然后把b分区文件全删了，因为是白的！

 只保留a区四个

![img](./assets/7cb20bb2b0c0f313d925aa79b5ba61dc.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

之后再把这四个文件移动到项目目录！
 现在可以把super.img删除了

![img](./assets/a77aaa3b57d486502b9b6922fc422cc6.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

之后到termux

 还是解压所有文件

![img](./assets/d19bf676e3e5f193871f67040752980a.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

解压好后是这样的，

![img](./assets/021fb2930c58df536224e65485209cdb.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

你可以到目录去删除一些用不到的软件，去除温控添加功能等等！我这里就不发图了接打包！
 我也不知道这super哪里蹦出来的，所以逐个选择img格式打包把！

![img](./assets/494beafbf55e425c43f854327ce5cde4.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

![img](./assets/6c903b66e54c54a1dd0d959b19831204.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

打包完后，建议新作一个工程目录！
 然后把打包出来的img镜像移动到新目录
 到目录里手动创建一个文件夹命名为super
 之后把镜像移动到super文件夹

 然后开始打包！
 选择66打包super

![img](./assets/0bdbcb83dcaa974bc3efba9068aef6d9.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

按我的填写就行最后回车

![img](./assets/82effd525bdaac8ad48f18e9bc6f411f.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

出现类似提示，即打包成功！



![img](./assets/031e84654b250a2fb10f92055813dca8.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

![img](./assets/801ec08a46daa039a3b894be458b48c8.jpeg)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

最后你就可以把他移动到最开始解压的那个压缩包进行压缩啦

![img](./assets/ce7f4b4e723f0a1e13885eda57b111c7.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑



 最后用tfs刷入我就不做过多解释啦

![img](./assets/c8e0e1f1c84bce8a5313bf363098ee75.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑

稍等我测试一下会放上本帖的栗子！
 EU最新解锁分区版本！

 测试🌰已经因误删文件报废！

 [#motorolaedgespro#](https://www.coolapk.com/t/motorolaedgespro?type=12) [#MotoedgeS30#](https://www.coolapk.com/t/MotoedgeS30?type=12) [#MotoedgeX30#](https://www.coolapk.com/t/MotoedgeX30?type=12)