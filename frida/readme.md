# 版本对应
| frida    | frida-tools |
| :----:   | :----:      |
| 12.7.22  | 5.2.0       |
| 15.1.2   | 10.2.2      |
| 16.0.8   | 12.0.4      |

一键查看对应版本https://github.com/frida/frida/releases/tag/12.7.22
# ~~安装frida~~
> **Note**  
> 直接安装frida-tools即可，会自动安装对应版本的frida，并且若是单独再安装frida，可能会出现找不到DLL问题
```
..\python3.6.8\Scripts>pip3.6 install frida==12.7.22  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
# 安装frida-tools
```
..\python3.6.8\Scripts>pip3.6 install frida-tools==5.2.0  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
> MacOS 下安装需要加sudo,否则会无法使用frida的命令行工具
# 安装多个Python版本问题
设置pythonpath为当前要用的版本路径即可
# 问题：`ImportError: DLL load failed while importing _frida: 找不到指定的模块。`
refs:https://blog.csdn.net/guo343310267/article/details/88343025  
需要安装最新版的frida，安装历史版本的没有egg文件，导致出现上面的错误  

# 重新编译Frida
```
$ git clone https://github.com/frida/frida.git

$ cd frida

$ make

$ export ANDROID_NDK_ROOT=/Users/{username}/Library/Android/sdk/ndk/22.0.6917172/

$ sudo apt-get install npm

$ sudo apt install python3-pip

$ pip3 install colorama prompt-toolkit pygments

$ rm -rf build

$ make core-android-x86_64

$ make core-android-x86

# 最后生成的文件在 build/frida-android-x86 build/frida-android-x86_64 
# 如果需要调整编译参数，在releng/setup-env.sh中进行调整 比如: meson_common_flags="['-g']"
```
## 重新编译Frida(16.+)
* refs:https://frida.re/docs/building/#gnulinux  
```
$ git clone --recurse-submodules https://github.com/frida/frida.git
$ cd frida
$ make
```
# 检测frida服务是否在运行
```python
# 仅适用于低于15的版本，15以上的版本已经去掉了该握手验证，具体参看：https://frida.re/news/2021/07/18/frida-15-0-released/
def check_frida_server(ip=default_ip, port=default_port):
    try:
        tcp = socket.socket()
        tcp.settimeout(2)
        tcp.connect((ip, port))
        tcp.send(b'\x00AUTH\r\n')
        res = tcp.recv(100)
        return str(res).find('REJECTED') >= 0
    except Exception as e:
        return False

# for v15+
def check_frida_server_v15(ip=default_ip, port=default_port):
    try:
        tcp = socket.socket()
        tcp.settimeout(300)
        tcp.connect((ip, port))
        tcp.send(b"""GET /ws HTTP/1.1
                     Upgrade: websocket
                     Connection: Upgrade
                     Sec-WebSocket-Key: EcDK00jyHpvcc1F/rraBPw==
                     Sec-WebSocket-Version: 13
                     Host: 127.0.0.1:27045
                     User-Agent: Frida/15.1.2

""")
        res = tcp.recv(100)
        return res==b'HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n'
    except Exception as e:
        print(e)
        return False


```
# 参考
https://www.mobibrw.com/2021/28588
