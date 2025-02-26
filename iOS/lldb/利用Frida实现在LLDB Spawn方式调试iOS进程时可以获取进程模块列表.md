# 利用Frida实现在LLDB Spawn方式调试iOS进程时可以获取进程模块列表

```shell
frida -Uf <package_name> --pause
```

```
debugserver 127.0.0.1:1234 --attach=575 
```

```
%resume
```

```
lldb
```

