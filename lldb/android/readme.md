# LLDB for android

# 环境配置

- 下载sdk
- 下载ndk
- lldb-server路径:sdk/lldb/3.1/android/{arch}/lldb-server
- lldb路径：sdk\ndk\23.0.7599858\toolchains\llvm\prebuilt\windows-x86_64\bin\lldb.cmd
# 配置lldb-server
```
adb push lldb-server /data/local/tmp/
adb shell su -c 'chmod +x ./data/local/tmp/lldb-server'
adb shell su -c './data/local/tmp/lldb-server platform --listen "*:1234" --server'
```
### 方案二
```
adb push lldb-server /data/local/tmp/
adb shell su -c 'chmod +x ./data/local/tmp/lldb-server'
adb shell su -c './data/local/tmp/lldb-server platform --listen unix-abstract:///data/local/tmp/debug.sock --server'
```
# 配置lldb
```
adb forward tcp:1234 tcp:1234
lldb.cmd
platform list
platform select remote-android
platform connect connect://:1234
```
### 方案二
```
lldb.cmd
platform list
platform select remote-android
platform connect unix-abstract-connect:///data/local/tmp/debug.sock
```
# 注入进程
```
platform process list
attach <pid>
```
> 获取进程pid: ps -A | grep \<packageName\>

# 具体调试
- 常用命令：wa,image,info,br
- 内存写入断点
```
watchpoint set expression -w write -- 0xe8583c00+32
```
# 其它
## 常用命令
- help:查看所有帮助信息
- apropos:查找和特定的词或主题相关的调试器命令列表
- image list -o -f :查找所有模块基址
## pycharm 导入lldb模块
ref:[pycharm下设置PYTHONPATH](https://blog.csdn.net/weixin_41698305/article/details/90902427)  
lldb模块路径：`sdk\ndk\23.0.7599858\toolchains\llvm\prebuilt\windows-x86_64\lib\python3.9\site-packages` 
- 直接在Window下python里import lldb会报找不到_lldb模块
- 可以在msys2命令行里启动pycharm.exe，然后在pycharm里正常编写代码即可(前提需要在msys2里用pacman先安装lldb)(若是pacman报密钥错误，不要搜解决方案，解决不了的，直接删除原来msys2，再[下载最新版msys2重新安装](https://www.msys2.org/)即可)(安装完成后再用[pacman更新](https://kaosx.us/docs/pacman/)下)
- 当然也可以再macOS里pycharm使用lldb，没什么坑
## python api for lldb
ref:[python-reference](https://lldb.llvm.org/use/python-reference.html)
## pycharm 编写lldb调试代码
[./lldb_template.py](./lldb_template.py)
## lldb 调试时汇编显示错误问题
```
(lldb) dis -A thumb
cmd: dis -A thumb
->  0xc90701e6: mov    r6, r0
    0xc90701e8: ldr    r0, [pc, #0x3c]
    0xc90701ea: add    r0, pc
    0xc90701ec: ldr    r0, [r0]
    0xc90701ee: ldr    r0, [r0]
    0xc90701f0: cmp    r0, r6
    0xc90701f2: .short 0xbf04                    ; unknown opcode
    0xc90701f4: add    sp, #0x8
    0xc90701f6: pop    {r4, r5, r6, pc}
    0xc90701f8: movs   r0, #0x10
    0xc90701fa: .long  0xebeaf6db                ; unknown opcode
    0xc90701fe: ldr    r1, [r4, #0x4]
    0xc9070200: mov    r5, r0
    0xc9070202: mov    r2, r6
    0xc9070204: .long  0x0000f7ff                ; unknown opcode

```
## LLDB调试尽量不要断在匿名函数上，否则容易出现异常
## 多个Thread被断下时如何切换线程
```
thread select <thread index>
```
## image lookup 用法
```
(lldb) image lookup -n gaea::idl::BaseModel::Pack
cmd: image lookup -n gaea::idl::BaseModel::Pack
2 matches found in C:\Users\shlu\.lldb\module_cache\remote-android\.cache\88BCF618-38A8-E885-2B70-C424D3CDD73F-D4819735\libgaea.so:
        Address: libgaea.so[0x00191f40] (libgaea.so.PT_LOAD[0]..text + 120672)
        Summary: libgaea.so`gaea::idl::BaseModel::Pack(cmp_ctx_s*) const        Address: libgaea.so[0x00191fe4] (libgaea.so.PT_LOAD[0]..text + 120836)
        Summary: libgaea.so`gaea::idl::BaseModel::Pack(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >*) const

```
```
(lldb) image lookup -a 0xcfddd00a
cmd: image lookup -a 0xcfddd00a
      Address: libgaea.so[0x0019200a] (libgaea.so.PT_LOAD[0]..text + 120874)
      Summary: libgaea.so`gaea::idl::BaseModel::Pack(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >*) const + 38

```
## 参考
- [远程调试](https://lldb.llvm.org/use/remote.html)
- [lldb调试命令](https://lldb.llvm.org/use/map.html)
