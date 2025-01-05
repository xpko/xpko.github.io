# 【源码定制】移植Youpk到Android 8.0 (Pixel2 XL)

### Youpk4Pixel2XL
  `Youpk`是一种通过修改系统源码实现主动调用进行脱壳的工具，基于`android-7.1.2_r33`分支做的定制，仅支持`Pixel`机型，但该机型问题太多了，买了两个，一个时不时无限重启，一个充不进去电，正好身边有一部`Pixel 2 XL`用着还不错，并且`Pixel 2 XL`支持的最初始分支`android-8.0.0_r21`与`android-7.1.2_r33`分支挺近的，代码差别应该不是很大，就想把`Youpk`移植到`Pixel 2 XL`，正好也学习下`Youpk`的工作原理。 

  在此特感谢`Youpk`工具作者的开源精神，否则要凭空研究出来对于我来说真是太难了，需要对越来越庞大的android源码有充分的了解。因此，我这个移植也会依照`Youpk`的格式开源。以及感谢在移植过程中，在网上搜索到的各种填坑文章，以及Google开源的Android源码，还有各种在线源码搜索服务，还有各种编译系统以及填坑的文章,以及现在越来越快的科学速度，以及各种涉及到的效率工具。  

  具体原理就不用讲了，参考Youpk即可，其实我也不太懂，我就只管移植完事即可,哈哈。  

  很少研究这方面，若是有遗漏地方大佬勿喷，欢迎提出来哈
### 与Youpk不同的地方
- `CompilerFilter::kVerifyAtRuntime`换成了`CompilerFilter::kVerify`  
- `mirror::ClassLoader*`换成了`ObjPtr<mirror::ClassLoader>`  
- `StringPrintf`换成了`android::base::StringPrintf`  
- `ReaderMutexLock mu(self, *class_linker->DexLock());`换成了`ReaderMutexLock mu(self, *Locks::dex_lock_);`  
- `ClassLinker`里好几个函数返回值变成了`ObjPtr<T>`格式  
- `PrettyMethod(method)`换成了`method->PrettyMethod()`  
- `NATIVE_METHOD`和`REGISTER_NATIVE_METHODS`位置发生了改变  

### 最后
附上开源地址:[Humenger/Youpk4Pixel2XL](https://github.com/Humenger/Youpk4Pixel2XL)  
### 源码编译
- [【源码编译】android-8.0.0_r21 for Pixel 2 XL on ubuntu20.04-server](https://blog.csdn.net/qq_26914291/article/details/127630786)