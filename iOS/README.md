# 基础篇

## 刷机
iOS刷机很简单，直接通过爱思助手进行刷即可，但有几点需要注意

+ 苹果有个验证机制，这个机制有很多限制，你只能刷最新的系统，不能刷老系统，要想刷老系统，需要一个该老系统对应的SHSH2文件，而这个SHSH2文件不好获取的，你只能获取现在可以刷的系统的SHSH2文件，老的系统的SHSH2文件就没法获取了，但也可以通过某些工具强制刷，但这样做会有很多副作用，不建议采用。
+ [SHSH2提取备份教程](https://dkxuanye.cn/?p=614)，[iOS_shsh2](https://github.com/jitcor/my_notes/releases/tag/iOS_shsh2)
+ 所以在系统有新版时，记得及时备份SHSH2文件
+ 当然一些已经不再提供系统更新支持的老版手机，其最终支持版本会一直可以下载其SHSH2文件，也就是该最终版本会永久支持其刷机
+ 刷机前确认手机是否有[Apple ID 锁（激活锁）](https://www.i4.cn/news_detail_19670.html)（不是[网络锁(运营商锁)](https://www.i4.cn/news_detail_19376.html)，网络锁是限制SIM卡的）

## 越狱
+ checkm8
    - checkra1n
    - palera1n
+ 

## 抓包
+ IP
    - tcp
        * http
            + WIFI代理
        * tls
            + 证书
            + https
                - WIFI代理
    - 虚拟网卡
        * VPN
        * rvictl

抓包工具

charles

wireshark

reqable

stream


# 工具篇

[多开工具：LiveContainer](https://github.com/khanhduytran0/LiveContainer)  
[固件解析工具：ipsw](https://github.com/blacktop/ipsw)  
```bash
# 查看固件基础信息
ipsw info path/to/xxx.ipsw
```
```
[IPSW Info]
===========
Version        = 14.4.2
BuildVersion   = 18D70
OS Type        = Production
FileSystem     = 038-96340-065.dmg
RestoreRamDisk = [038-96438-065.dmg 038-96118-065.dmg]

Devices
-------

iPad (7th generation)
 > iPad7,11_J171AP_18D70
   - TimeStamp: 06 Jan 2021 20:35:32 PST
   - KernelCache: kernelcache.release.ipad7c
   - CPU: A10 Fusion (ARMv8.1-A), ID: t8010
   - BootLoaders
       * iBEC.ipad7c.RELEASE.im4p
       * iBoot.ipad7c.RELEASE.im4p
       * iBSS.ipad7c.RELEASE.im4p
       * LLB.ipad7c.RELEASE.im4p
       * sep-firmware.j171.RELEASE.im4p

iPad (7th generation)
 > iPad7,12_J172AP_18D70
   - TimeStamp: 06 Jan 2021 20:35:39 PST
   - KernelCache: kernelcache.release.ipad7c
   - CPU: A10 Fusion (ARMv8.1-A), ID: t8010
   - BootLoaders
       * iBEC.ipad7c.RELEASE.im4p
       * iBoot.ipad7c.RELEASE.im4p
       * iBSS.ipad7c.RELEASE.im4p
       * LLB.ipad7c.RELEASE.im4p
       * sep-firmware.j172.RELEASE.im4p

```
```bash
ipsw mount fs /path/to/xxx.ipsw
```
```
   • Mounted fs DMG 038-96340-065.dmg
      • Press Ctrl+C to unmount '/tmp/038-96340-065.dmg.mount' ...
```
# 技术篇
## 获取系统库二进制文件
```bash
# 1.下载对应版本固件，推荐爱思助手里下载，或者网站：ipsw.me
# 2.ipsw命令挂载,然后可以在磁盘挂载列表找到对应挂载点，如下AzulD开头就是
```

![image-20240930174658706](./README.assets/image-20240930174658706.png)

```bash
# 找到/System/Library/Caches/com.apple.dyld这个目录，复制出来（省去以后再次挂载）
# 利用dsc_extractor工具导出系统库
dsc_extractor path/to/com.apple.dyld/dyld_shared_cache_arm64 <out_dir>
# 导出后，系统库路径：<out_dir>/usr/lib/libxxx.dylib
# 然后可以直接拖入IDA等分析工具分析即可
```

 [dsc_extractor](./README.assets/dsc_extractor) 









