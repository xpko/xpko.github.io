# sgmain错误码列表

## 初始化(SecurityInit)

| 错误码                               | 值   | 含义                                                         |
| :----------------------------------- | :--- | :----------------------------------------------------------- |
| SEC_ERROR_INIT_CONTEXT_ISNULL        | 101  | 参数不正确，请检查输入的参数。                               |
| SEC_ERROR_INIT_SO_CHECK_ERROR        | 102  | libsgmain.so文件和无线保镖的jar包不匹配。请检验是否存在libsgmain.so文件被破坏或修改的情况。 |
| SEC_ERROR_INIT_LOADSO_FAIL           | 103  | libsgmain.so文件装载问题，通常不会发生。如果发生此问题，可以卸载APK，再重新安装来尝试。 |
| SEC_ERROR_INIT_NO_RSA_FILE_ERROR     | 104  | APK中没有正常的RSA签名文件。请检验签名过程。                 |
| SEC_ERROR_INIT_PUBLICKKEY_FIND_ERROR | 105  | RSA文件不正常，无法正常解析出公钥。                          |
| SEC_ERROR_INIT_SO_NOT_EXIST          | 106  | 在APK中找不到对应 aebi 的 libsgmain.so 文件，请检查是否正常打包了无线保镖SDK提供的so文件。（不同版本的so和jar不能混用） |
| SEC_ERROR_INIT_UNKNOWN_ERROR         | 199  | 未知错误，请重试。                                           |

## 安全签名（SecuritySignature)

| 错误码                                       | 值   | 含义                                                         |
| :------------------------------------------- | :--- | :----------------------------------------------------------- |
| SEC_ERROR_SIGNATRUE_INVALID_INPUT            | 601  | 参数不正确，请检查输入的参数                                 |
| SEC_ERROR_SIGNATURE_NO_MEM                   | 602  | 内存分配失败，请重试                                         |
| SEC_ERROR_SIGNATURE_NO_SEEDSECRET            | 606  | 使用带seedkey的top签名时，没有找到seedkey对应的seedsecret    |
| SEC_ERROR_SIGNATURE_DATA_FILE_MISMATCH       | 607  | 图片文件存在问题。一般是获取图片文件时的apk签名和当前程序的apk签名不一致。请使用当前程序的apk重新生成图片 |
| SEC_ERROR_SIGNATURE_NO_DATA_FILE             | 608  | 没有找到图片文件，请确保图片文件在 res\drawable 目录下。如果是 Android Studio 工程中开启了 shrinkResources 优化，需要将安全组件的图片文件排除 |
| SEC_ERROR_SIGNATURE_INCORRECT_DATA_FILE      | 609  | 图片文件格式有问题，请重新生成图片文件                       |
| SEC_ERROR_SIGNATURE_INCORRECT_DATA_FILE_DATA | 610  | 图片文件内的内容不正确，请重新生成图片文件                   |
| SEC_ERROR_SIGNATURE_KEY_NOT_EXSITED          | 611  | 参数中的key在图片文件中找不到，请确认key和图片文件配套       |
| SEC_ERROR_SIGNATURE_ILLEGEL_KEY              | 612  | 输入的key非法，key不能为：‘:’, ‘\|’, ‘/’, ‘.’,‘1’,‘2’,‘3’,‘4’,‘5’,‘6’,‘7’,‘8’ |
| SEC_ERROR_SIGNATRUE_UNKNOWN                  | 613  | 未知错误                                                     |

## 安全加密（SecurityCipher）

| 错误码                                 | 值   | 含义                                                         |
| :------------------------------------- | :--- | :----------------------------------------------------------- |
| SEC_ERROR_STA_INVALID_PARAM            | 301  | 参数不正确，请检查输入的参数                                 |
| SEC_ERROR_STA_DATA_FILE_MISMATCH       | 302  | 图片文件有问题。一般是获取图片文件时的apk签名和当前程序的apk签名不一致。请使用当前程序的apk重新生成图片 |
| SEC_ERROR_STA_NO_DATA_FILE             | 303  | 没有找到图片文件，请确保图片文件在res\drawable目录下。如果是Android Studio工程中开启了shrinkResources优化，需要将安全组件的图片文件排除 |
| SEC_ERROR_STA_INCORRECT_DATA_FILE      | 304  | 图片文件格式有问题，请重新生成图片文件                       |
| SEC_ERROR_STA_INCORRECT_DATA_FILE_DATA | 305  | 图片文件内的内容不正确，请重新生成图片文件                   |
| SEC_ERROR_STA_KEY_NOT_EXISTED          | 306  | 参数中的key在图片文件中找不到，请确认图片文件中有这个key     |
| SEC_ERROR_STA_ILLEGEL_KEY              | 307  | 输入的key非法，key不能为：‘:’, ‘\|’, ‘/’, ‘.’, ‘1’, ‘2’,‘3’,‘4’,‘5’,‘6’,‘7’,‘8’ |
| SEC_ERROR_STA_NO_MEMORY                | 308  | 内存不足，请重试                                             |
| SEC_ERROR_STA_NO_SUCH_INDEX            | 309  | 在图片文件中没有找到这个index                                |
| SEC_ERROR_STA_INVALID_ENCRYPTED_DATA   | 310  | 非法的加密数据                                               |
| SEC_ERROR_STA_STORE_UNKNOWN_ERROR      | 399  | 未知错误，请重试                                             |

## 安全存储（SecurityStorage）

| 错误码                                        | 值   | 含义                                                       |
| :-------------------------------------------- | :--- | :--------------------------------------------------------- |
| SEC_ERROR_DYN_STORE_INVALID_PARAM             | 501  | 参数不正确，请检查输入的参数                               |
| SEC_ERROR_DYN_STORE_NO_MEMORY                 | 502  | 内存不足，请重试                                           |
| SEC_ERROR_DYN_STORE_GET_SYS_PROPERTIES_FAILED | 503  | 获取系统属性失败，请确认是否有软件拦截，获取系统参数       |
| SEC_ERROR_DYN_STORE_GET_DATA_FILE_KEY_FAILED  | 504  | 获取图片文件的密钥失败，请确认图片文件的格式和内容是否正确 |
| SEC_ERROR_DYN_STORE_GET_ENCRYPT_KEY_FAILED    | 505  | 获取动态加密密钥失败，请重试                               |
| SEC_ERROR_DYN_STORE_INVALID_ENCRYPTED_DATA    | 506  | 待解密数据不是可解密数据                                   |
| SEC_ERROR_DYN_STORE_DECRYPT_MISMATCH_KEY_DATA | 507  | 待解密数据与密钥不匹配，请重试                             |
| SEC_ERROR_DYN_STORE_DDPEX_KEY_VALUE_NOT_EXSIT | 508  | 传入key对应的value不存在                                   |
| SEC_ERROR_DYN_STORE_UNKNOWN_ERROR             | 599  | 未知错误，请重试                                           |

## 白盒加密（SecurityCipher）

| 错误码                                  | 值   | 含义                                                         |
| :-------------------------------------- | :--- | :----------------------------------------------------------- |
| SEC_ERROR_ATLAS_ENC_INVALID_PARAM       | 1001 | 参数不正确，请检查输入的参数                                 |
| SEC_ERROR_ATLAS_ENC_DATA_FILE_MISMATCH  | 1002 | 图片文件有问题。一般是获取图片文件时的apk签名和当前程序的apk签名不一致。请使用当前程序的apk重新生成图片 |
| SEC_ERROR_ATLAS_ENC_NO_DATA_FILE        | 1003 | 没有找到图片文件，请确保图片文件在res\drawable目录下         |
| SEC_ERROR_ATLAS_ENC_INCORRECT_DATA_FILE | 1004 | 图片文件格式有问题，请重新生成图片文件                       |
| SEC_ERROR_ATLAS_ENC_NO_KEY              | 1006 | 图片文件中找不到秘钥数据，请确认图片是否正确                 |
| SEC_ERROR_ATLAS_ENC_NO_MEMORY           | 1008 | 内存不足，请重试                                             |
| SEC_ERROR_ATLAS_ENC_UNKNOWN_ERROR       | 1099 | 未知错误，请重试                                             |

## 白盒签名（SecuritySignature）

| 错误码                                       | 值   | 含义                                                         |
| :------------------------------------------- | :--- | :----------------------------------------------------------- |
| SEC_ERROR_SIGNATRUE_INVALID_INPUT            | 601  | 参数不正确，请检查输入的参数                                 |
| SEC_ERROR_SIGNATURE_NO_MEM                   | 602  | 内存分配失败，请重试                                         |
| SEC_ERROR_SIGNATURE_NO_SEEDSECRET            | 606  | 使用带seedkey的top签名时，没有找到seedkey对应的seedsecret    |
| SEC_ERROR_SIGNATURE_DATA_FILE_MISMATCH       | 607  | 图片文件存在问题。一般是获取图片文件时的apk签名和当前程序的apk签名不一致。请使用当前程序的apk重新生成图片 |
| SEC_ERROR_SIGNATURE_NO_DATA_FILE             | 608  | 没有找到图片文件，请确保图片文件在res\drawable目录下。如果是Android Studio工程中开启了shrinkResources优化，需要将安全组件的图片文件排除。 |
| SEC_ERROR_SIGNATURE_INCORRECT_DATA_FILE      | 609  | 图片文件格式有问题，请重新生成图片文件                       |
| SEC_ERROR_SIGNATURE_INCORRECT_DATA_FILE_DATA | 610  | 图片文件内的内容不正确，请重新生成图片文件                   |
| SEC_ERROR_SIGNATURE_KEY_NOT_EXSITED          | 611  | 参数中的key在图片文件中找不到，请确认图片文件中有这个key     |
| SEC_ERROR_SIGNATURE_ILLEGEL_KEY              | 612  | 输入的key非法，key不能为：‘:’, ‘\|’, ‘/’, ‘.’, ‘1’, ‘2’,‘3’,‘4’,‘5’,‘6’,‘7’,‘8’ |
| SEC_ERROR_SIGNATRUE_UNKNOWN                  | 613  | 未知错误                                                     |



## 客户端错误码

> ref: https://help.aliyun.com/zh/captcha/captcha1-0/user-guide/common-error-codes

| 错误码                                     | 值   | 含义                                                         |
| ------------------------------------------ | ---- | ------------------------------------------------------------ |
| SEC_ERROR_SECURITYBODY_INVALID_PARAM       | 1401 | 参数不正确，请检查输入的参数                                 |
| SEC_ERROR_SECURITYBODY_ENCRYPTION_ERROR    | 1407 | 数据加密错误，请确保使用正确的图片yw_1222_0335.jpg，请联系我们 |
| SEC_ERROR_SECURITYBODY_DATA_FILE_MISMATCH  | 1411 | 图片yw_1222_0335.jpg与SDK之间不匹配，请确保使用的SDK和图片来自同一个下载的zip |
| SEC_ERROR_SECURITYBODY_NO_DATA_FILE        | 1412 | 图片yw_1222_0335.jpg在App中未找到，请检查是否正确引入图片。另外如果设值gradle关于shrinkResource相关配置后，请keep注图片yw_1222_0335.jpg。否则打包时图片yw_1222_0335.jpg会被优化。具体信息，请参见[Resource Shrinking](http://tools.android.com/tech-docs/new-build-system/resource-shrinking) |
| SEC_ERROR_SECURITYBODY_INCORRECT_DATA_FILE | 1413 | 非法的图片yw_1222_0335.jpg，请检查该图片正确性，确保和下载的SDK的zip中是一致的。 |
| SEC_ERROR_SECURITYBODY_KEY_NOT_EXSITED     | 1414 | 图片yw_1222_0335.jpg中缺少相关数据，请重新下载图片。         |
| SEC_ERROR_SECURITYBODY_LOW_VERSION_DATA    | 1415 | 非法的图片yw_1222_0335.jpg 图片是低版本的，请下载新的图片和SDK相匹配 |
| SEC_ERROR_SECURITYBODY_UNKNOWN             | 1499 | 未知错误，请联系我们                                         |
| SEC_ERROR_INIT_PUBLICKKEY_FIND_ERROR       | 105  | RSA文件不正常，无法正常解析出公钥                            |
| SEC_ERROR_INIT_SO_NOT_EXIST                | 106  | 在APK中找不到对应aebi的libsecurityguard***.so文件，请确认存在此文件，并且它的版本和jar包的版本号一致。（不同版本的不通用，请不要用其他版本的替换） |
| SEC_ERROR_INIT_DECODESO_FAIL               | 107  | libsecurityguard***.so解码失败，请卸载后全新安装或检查磁盘空间 |
| SEC_ERROR_INIT_LOADSOINNER_FAILED          | 108  | 加载内部so失败                                               |
| SEC_ERROR_INIT_FDSOFUN_FAILED              | 109  | 内部so运行失败                                               |
| SEC_ERROR_INIT_PLUGIN_NOT_EXISTED          | 110  | 插件不存在，请检查打包配置中，so是否正确打入APK中            |
| SEC_ERROR_INIT_PLUGIN_LOAD_FAILED          | 111  | 加载插件失败，一般不会发生。请检查是否存在IO异常或内存分配不足 |
| SEC_ERROR_INIT_LOAD_INTERFACE_NOT_EXISTED  | 112  | 获取接口失败，请检查插件so版本是否与JAR包版本是否匹配        |
| SEC_ERROR_PLUGIN_REQUIREMENT_NOT_MEET      | 113  | 插件依赖不匹配，请检查插件版本，查看依赖关系是否兼容         |
| SEC_ERROR_INIT_EXTRACT_DIR_NOT_EXISTED     | 114  | 系统IO异常，插件加载目录打开失败                             |
| SEC_ERROR_INIT_DATA_FILE_MISMATCH          | 121  | 图片文件有问题。一般是生成图片文件时WSG上注册的应用公钥和当前应用的公钥信息不一致。 |
| SEC_ERROR_INIT_NO_DATA_FILE                | 122  | 没有找到图片文件，请确保图片文件在项目目录下                 |
| SEC_ERROR_INIT_INCORRECT_DATA_FILE         | 123  | 图片文件格式由问题，请重新生成图片文件。一种常见场景就是二方和三方图片混用。二方和三方的图片不兼容，需要各自生成。还有一个场景是4.x.x的SDK使用了5的图片，v5图片只能在6.x.x上使用 |
| SEC_ERROR_INIT_LOW_VERSION_DATA            | 124  | 当前图片的版本太低                                           |
| SEC_ERROR_INIT_PARSE_USER_CONFIG_ERROR     | 125  | init with authcode初始化错误，请联系答疑账户具体定位         |
| SEC_ERROR_INIT_UNKNOWN_ERROR               | 199  | 未知错误，请重试                                             |



## 以下提取自APP内部代码文件

```java
package com.alibaba.wireless.security;

/* loaded from: classes.dex */
public class SecExceptionCode {
    public static final int SEC_ERROE_NOCAPTCHA_INVALID_PARAM = 1201;
    public static final int SEC_ERROE_NOCAPTCHA_INVALID_THREAD = 1205;
    public static final int SEC_ERROE_NOCAPTCHA_NOT_INIT_YET = 1203;
    public static final int SEC_ERROE_NOCAPTCHA_NO_MEMORY = 1202;
    public static final int SEC_ERROE_NOCAPTCHA_QUEUE_FULL = 1204;
    public static final int SEC_ERROE_NOCAPTCHA_UNKNOWN_ERR = 1299;
    public static final int SEC_ERROE_OPENSDK_DECODE_FAILED = 1102;
    public static final int SEC_ERROE_OPENSDK_INCORRECT_DATA_FILE = 1106;
    public static final int SEC_ERROE_OPENSDK_INVALID_BIZTYPE = 1107;
    public static final int SEC_ERROE_OPENSDK_INVALID_LENGTH = 1103;
    public static final int SEC_ERROE_OPENSDK_INVALID_PARAM = 1101;
    public static final int SEC_ERROE_OPENSDK_NO_MEMORY = 1108;
    public static final int SEC_ERROE_OPENSDK_UNKNOWN_ERR = 1199;
    public static final int SEC_ERROE_OPENSDK_UNSUPPORTED_VERSION = 1104;
    public static final int SEC_ERROE_OPENSDK_VERSION_MISMATCH = 1105;
    public static final int SEC_ERROR_ATLAS_ENC = 1000;
    public static final int SEC_ERROR_ATLAS_ENC_DATA_FILE_MISMATCH = 1002;
    public static final int SEC_ERROR_ATLAS_ENC_INCORRECT_DATA_FILE = 1004;
    public static final int SEC_ERROR_ATLAS_ENC_INVALID_PARAM = 1001;
    public static final int SEC_ERROR_ATLAS_ENC_LOW_VERSION_DATA_FILE = 1010;
    public static final int SEC_ERROR_ATLAS_ENC_NO_ATLAS_DATA = 1007;
    public static final int SEC_ERROR_ATLAS_ENC_NO_DATA_FILE = 1003;
    public static final int SEC_ERROR_ATLAS_ENC_NO_KEY = 1006;
    public static final int SEC_ERROR_ATLAS_ENC_NO_MEMORY = 1008;
    public static final int SEC_ERROR_ATLAS_ENC_UNKNOWN_ERROR = 1099;
    public static final int SEC_ERROR_ATLAS_GET_KEY_SEED_FAILED = 1009;
    public static final int SEC_ERROR_ATLAS_UNSUPPORTED = 1098;
    public static final int SEC_ERROR_AVMP = 1900;
    public static final int SEC_ERROR_AVMP_SAFETOKEN = 1700;
    public static final int SEC_ERROR_AVMP_SAFETOKEN_INVALID_PARAM = 1701;
    public static final int SEC_ERROR_DYN_ENC = 400;
    public static final int SEC_ERROR_DYN_ENC_BASE64_DECODE_FAILED = 423;
    public static final int SEC_ERROR_DYN_ENC_DECRYPT_FAILED = 422;
    public static final int SEC_ERROR_DYN_ENC_DECRYPT_MISMATCH_KEY_DATA = 407;
    public static final int SEC_ERROR_DYN_ENC_GET_DATA_FILE_KEY_FAILED = 404;
    public static final int SEC_ERROR_DYN_ENC_GET_ENCRYPT_KEY_FAILED = 405;
    public static final int SEC_ERROR_DYN_ENC_GET_SYS_PROPERTIES_FAILED = 403;
    public static final int SEC_ERROR_DYN_ENC_INVALID_ENCRYPTED_DATA = 406;
    public static final int SEC_ERROR_DYN_ENC_INVALID_PARAM = 401;
    public static final int SEC_ERROR_DYN_ENC_NO_MEMORY = 402;
    public static final int SEC_ERROR_DYN_ENC_UNKNOWN_ERROR = 499;
    public static final int SEC_ERROR_DYN_STORE = 500;
    public static final int SEC_ERROR_DYN_STORE_DDPEX_KEY_VALUE_NOT_EXSIT = 508;
    public static final int SEC_ERROR_DYN_STORE_GET_DATA_FILE_KEY_FAILED = 504;
    public static final int SEC_ERROR_DYN_STORE_GET_ENCRYPT_KEY_FAILED = 505;
    public static final int SEC_ERROR_DYN_STORE_GET_SYS_PROPERTIES_FAILED = 503;
    public static final int SEC_ERROR_DYN_STORE_INVALID_PARAM = 501;
    public static final int SEC_ERROR_DYN_STORE_NO_MEMORY = 502;
    public static final int SEC_ERROR_DYN_STORE_UNKNOWN_ERROR = 599;
    public static final int SEC_ERROR_FRAMEWORK_INVALID_SO_NAME = 7;
    public static final int SEC_ERROR_GENERIC_AVMP_AVMPINIT_FAILED = 1907;
    public static final int SEC_ERROR_GENERIC_AVMP_DATA_FILE_MISMATCH_PLATFORM = 1914;
    public static final int SEC_ERROR_GENERIC_AVMP_INCORRECT_JPG_FILE = 1903;
    public static final int SEC_ERROR_GENERIC_AVMP_INVALID_ARGS = 1901;
    public static final int SEC_ERROR_GENERIC_AVMP_INVALID_AVMP_CONTEXT = 1910;
    public static final int SEC_ERROR_GENERIC_AVMP_INVALID_AVMP_PARAM = 1909;
    public static final int SEC_ERROR_GENERIC_AVMP_INVALID_AVMP_RETURN_TYPE = 1908;
    public static final int SEC_ERROR_GENERIC_AVMP_INVLIAD_MWUA_DATA_FILE = 1916;
    public static final int SEC_ERROR_GENERIC_AVMP_JPG_FILE_MISMATCH = 1902;
    public static final int SEC_ERROR_GENERIC_AVMP_LOW_VERISON_JPG = 1904;
    public static final int SEC_ERROR_GENERIC_AVMP_NO_BYTE_CODE = 1906;
    public static final int SEC_ERROR_GENERIC_AVMP_NO_DATA_FILE = 1905;
    public static final int SEC_ERROR_GENERIC_AVMP_UNKNOWN_ERROR = 1999;
    public static final int SEC_ERROR_GENERIC_AVMP_VM_CALL_FAILED = 1912;
    public static final int SEC_ERROR_GENERIC_AVMP_VM_DESTROIED = 1913;
    public static final int SEC_ERROR_GENERIC_AVMP_VM_SYMBOL_NOT_FOUND = 1911;
    public static final int SEC_ERROR_INIT = 100;
    public static final int SEC_ERROR_INIT_CONTEXT_ISNULL = 101;
    public static final int SEC_ERROR_INIT_DATA_FILE_MISMATCH = 121;
    public static final int SEC_ERROR_INIT_DECODESO_FAIL = 107;
    public static final int SEC_ERROR_INIT_EXTRACT_DIR_NOT_EXISTED = 114;
    public static final int SEC_ERROR_INIT_FAILED_GET_ROOTDIR = 109;
    public static final int SEC_ERROR_INIT_INCORRECT_DATA_FILE = 123;
    public static final int SEC_ERROR_INIT_INVALID_PARAM = 118;
    public static final int SEC_ERROR_INIT_LOADSOINNER_FAILED = 108;
    public static final int SEC_ERROR_INIT_LOADSO_FAIL = 103;
    public static final int SEC_ERROR_INIT_LOAD_INTERFACE_NOT_EXISTED = 112;
    public static final int SEC_ERROR_INIT_LOW_VERSION_DATA = 124;
    public static final int SEC_ERROR_INIT_NO_ANNOTATION = 150;
    public static final int SEC_ERROR_INIT_NO_DATA_FILE = 122;
    public static final int SEC_ERROR_INIT_NO_RSA_FILE_ERROR = 104;
    public static final int SEC_ERROR_INIT_NULL_APPLICTION_CONTEXT = 116;
    public static final int SEC_ERROR_INIT_PARSE_USER_CONFIG_ERROR = 125;
    public static final int SEC_ERROR_INIT_PLUGIN_LOAD_FAILED = 111;
    public static final int SEC_ERROR_INIT_PLUGIN_NOT_EXISTED = 110;
    public static final int SEC_ERROR_INIT_PUBLICKKEY_FIND_ERROR = 105;
    public static final int SEC_ERROR_INIT_RESERVE_DEPENDENCY_NOT_MEET = 117;
    public static final int SEC_ERROR_INIT_SOURCE_DIR_NOT_EXISTED = 115;
    public static final int SEC_ERROR_INIT_SO_CHECK_ERROR = 102;
    public static final int SEC_ERROR_INIT_SO_NOT_EXIST = 106;
    public static final int SEC_ERROR_INIT_UNKNOWN_ERROR = 199;
    public static final int SEC_ERROR_LBSRISK = 2200;
    public static final int SEC_ERROR_LBSRISK_GET_BINARY_FAILED = 2212;
    public static final int SEC_ERROR_LBSRISK_GET_WUA_FAILED = 2208;
    public static final int SEC_ERROR_LBSRISK_INIT_JNI_FAILED = 2206;
    public static final int SEC_ERROR_LBSRISK_INIT_WUA_FAILED = 2207;
    public static final int SEC_ERROR_LBSRISK_INPUT_RESET_BINARY_INVALID = 2205;
    public static final int SEC_ERROR_LBSRISK_INVALID_BINARY_FORMAT = 2222;
    public static final int SEC_ERROR_LBSRISK_INVALID_LOCATION_OBJECT = 2209;
    public static final int SEC_ERROR_LBSRISK_INVALID_LOCATION_SET = 2202;
    public static final int SEC_ERROR_LBSRISK_INVALID_PARAM = 2201;
    public static final int SEC_ERROR_LBSRISK_INVALID_PARAM2 = 2211;
    public static final int SEC_ERROR_LBSRISK_NOT_INIT = 2204;
    public static final int SEC_ERROR_LBSRISK_NO_MEMORY = 2203;
    public static final int SEC_ERROR_MALDETECT = 1300;
    public static final int SEC_ERROR_MALDETECT_UNKNOWN_ERR = 1399;
    public static final int SEC_ERROR_MALDETECT_UNSUPPORTED = 1398;
    public static final int SEC_ERROR_MIDDLE_TIER = 2300;
    public static final int SEC_ERROR_MIDDLE_TIER_INIT_FAILED = 2303;
    public static final int SEC_ERROR_MIDDLE_TIER_INVALID_PARA = 2301;
    public static final int SEC_ERROR_MIDDLE_TIER_NO_APPKEY = 2302;
    public static final int SEC_ERROR_MIDDLE_TIER_UNKONWN_ENCODING_ERROR = 2398;
    public static final int SEC_ERROR_MIDDLE_TIER_UNKONWN_ERROR = 2399;
    public static final int SEC_ERROR_MIDDLE_TIER_UNSUPPORT_BINARY_DATA_YET = 2304;
    public static final int SEC_ERROR_NOCAPTCHA = 1200;
    public static final int SEC_ERROR_NO_ERROR = 0;
    public static final int SEC_ERROR_OPENSDK = 1100;
    public static final int SEC_ERROR_PAGETRACK = 2000;
    public static final int SEC_ERROR_PAGE_TRACK_ERROR_INVALID_PARAM = 2001;
    public static final int SEC_ERROR_PAGE_TRACK_ERROR_NO_MEMORY = 2003;
    public static final int SEC_ERROR_PAGE_TRACK_ERROR_PAGE_NOT_MATCH = 2002;
    public static final int SEC_ERROR_PKG_VALID = 800;
    public static final int SEC_ERROR_PKG_VALID_INVALID_APK_PATH = 805;
    public static final int SEC_ERROR_PKG_VALID_INVALID_JPG = 802;
    public static final int SEC_ERROR_PKG_VALID_INVALID_PARAM = 801;
    public static final int SEC_ERROR_PKG_VALID_NO_CONFIG_FILE = 804;
    public static final int SEC_ERROR_PKG_VALID_NO_MEMORY = 803;
    public static final int SEC_ERROR_PKG_VALID_OPEN_APK_FAILED = 806;
    public static final int SEC_ERROR_PKG_VALID_UNKNOWN_ERR = 899;
    public static final int SEC_ERROR_PLUGIN_REQUIREMENT_NOT_MEET = 113;
    public static final int SEC_ERROR_SAFETOKEN = 1600;
    public static final int SEC_ERROR_SAFETOKEN_APPKEY_NOT_EXIST = 1605;
    public static final int SEC_ERROR_SAFETOKEN_CALL_VM_FAILED = 1612;
    public static final int SEC_ERROR_SAFETOKEN_DATA_FILE_MISMATCH = 1602;
    public static final int SEC_ERROR_SAFETOKEN_INCORRECT_DATA_FILE = 1604;
    public static final int SEC_ERROR_SAFETOKEN_INVALID_ENCRYPTED = 1611;
    public static final int SEC_ERROR_SAFETOKEN_INVALID_PARAM = 1601;
    public static final int SEC_ERROR_SAFETOKEN_INVALID_SEED = 1620;
    public static final int SEC_ERROR_SAFETOKEN_INVALID_TOKEN_ENCRYPTED = 1609;
    public static final int SEC_ERROR_SAFETOKEN_INVALID_TOKEN_FORMAT = 1606;
    public static final int SEC_ERROR_SAFETOKEN_LOW_VERISON_JPG = 1607;
    public static final int SEC_ERROR_SAFETOKEN_NO_DATA_FILE = 1603;
    public static final int SEC_ERROR_SAFETOKEN_OTP_UNSUPPORT = 1622;
    public static final int SEC_ERROR_SAFETOKEN_STORAGE_NOT_EXIST = 1608;
    public static final int SEC_ERROR_SAFETOKEN_TOKEN_NOT_EXIST = 1610;
    public static final int SEC_ERROR_SAFETOKEN_UNKNOWN_ERR = 1699;
    public static final int SEC_ERROR_SAFETOKEN_UNSUPPORTED = 1698;
    public static final int SEC_ERROR_SECURITYBODY = 1400;
    public static final int SEC_ERROR_SECURITYBODY_APPKEY_ERROR = 1405;
    public static final int SEC_ERROR_SECURITYBODY_CONCURRENT = 1409;
    public static final int SEC_ERROR_SECURITYBODY_DATA_FILE_MISMATCH = 1411;
    public static final int SEC_ERROR_SECURITYBODY_ENCRYPTION_ERROR = 1407;
    public static final int SEC_ERROR_SECURITYBODY_INCORRECT_DATA_FILE = 1413;
    public static final int SEC_ERROR_SECURITYBODY_INVALID_PARAM = 1401;
    public static final int SEC_ERROR_SECURITYBODY_INVALID_THREAD = 1402;
    public static final int SEC_ERROR_SECURITYBODY_KEY_NOT_EXSITED = 1414;
    public static final int SEC_ERROR_SECURITYBODY_LOW_VERSION_DATA = 1415;
    public static final int SEC_ERROR_SECURITYBODY_NET_ERROR = 1403;
    public static final int SEC_ERROR_SECURITYBODY_NOT_INITED = 1410;
    public static final int SEC_ERROR_SECURITYBODY_NO_DATA_FILE = 1412;
    public static final int SEC_ERROR_SECURITYBODY_SERVER_ERROR = 1404;
    public static final int SEC_ERROR_SECURITYBODY_SIGNATURE_ERROR = 1406;
    public static final int SEC_ERROR_SECURITYBODY_TOP_ERROR = 1408;
    public static final int SEC_ERROR_SECURITYBODY_UNKNOWN_ERR = 1499;
    public static final int SEC_ERROR_SECURITYBODY_UNSUPPORTED = 1498;
    public static final int SEC_ERROR_SECURITYBODY_ZIP_FAILED = 1416;
    public static final int SEC_ERROR_SET_GLOBAL_USER_DATA = 119;
    public static final int SEC_ERROR_SIGNATRUE = 600;
    public static final int SEC_ERROR_SIGNATRUE_INVALID_INPUT = 601;
    public static final int SEC_ERROR_SIGNATRUE_UNKNOWN = 699;
    public static final int SEC_ERROR_SIGNATURE_ATLAS_KEY_NOT_EXSITED = 613;
    public static final int SEC_ERROR_SIGNATURE_BASE64_FAILED = 604;
    public static final int SEC_ERROR_SIGNATURE_BLOWFISH_FAILED = 614;
    public static final int SEC_ERROR_SIGNATURE_CONFUSE_FAILED = 605;
    public static final int SEC_ERROR_SIGNATURE_DATA_FILE_MISMATCH = 607;
    public static final int SEC_ERROR_SIGNATURE_HASHHEX_FAILED = 603;
    public static final int SEC_ERROR_SIGNATURE_ILLEGEL_KEY = 612;
    public static final int SEC_ERROR_SIGNATURE_INCORRECT_DATA_FILE = 609;
    public static final int SEC_ERROR_SIGNATURE_INCORRECT_DATA_FILE_DATA = 610;
    public static final int SEC_ERROR_SIGNATURE_KEY_NOT_EXISTED = 611;
    public static final int SEC_ERROR_SIGNATURE_KEY_NOT_EXSITED = 611;
    public static final int SEC_ERROR_SIGNATURE_LOW_VERSION_DATA_FILE = 615;
    public static final int SEC_ERROR_SIGNATURE_NONSUPPORTED_SIGN_TYPE = 698;
    public static final int SEC_ERROR_SIGNATURE_NO_DATA_FILE = 608;
    public static final int SEC_ERROR_SIGNATURE_NO_MEM = 602;
    public static final int SEC_ERROR_SIGNATURE_NO_SEEDSECRET = 606;
    public static final int SEC_ERROR_SIMULATORDETECT = 1500;
    public static final int SEC_ERROR_SIMULATORDETECT_UNSUPPORTED = 1598;
    public static final int SEC_ERROR_STA_DATA_FILE_MISMATCH = 302;
    public static final int SEC_ERROR_STA_DECRYPT_MISMATCH_KEY_DATA = 311;
    public static final int SEC_ERROR_STA_ENC = 300;
    public static final int SEC_ERROR_STA_ILLEGEL_KEY = 307;
    public static final int SEC_ERROR_STA_INCORRECT_DATA_FILE = 304;
    public static final int SEC_ERROR_STA_INCORRECT_DATA_FILE_DATA = 305;
    public static final int SEC_ERROR_STA_INVALID_ENCRYPTED_DATA = 310;
    public static final int SEC_ERROR_STA_INVALID_PARAM = 301;
    public static final int SEC_ERROR_STA_KEY_ENC = 700;
    public static final int SEC_ERROR_STA_KEY_ENC_INVALID_ENCRYPTED_DATA = 704;
    public static final int SEC_ERROR_STA_KEY_ENC_INVALID_PARAM = 701;
    public static final int SEC_ERROR_STA_KEY_ENC_MISMATCH_KEY_DATA = 705;
    public static final int SEC_ERROR_STA_KEY_ENC_NO_KEY = 703;
    public static final int SEC_ERROR_STA_KEY_ENC_NO_MEMORY = 702;
    public static final int SEC_ERROR_STA_KEY_ENC_UNKNOWN_ERROR = 799;
    public static final int SEC_ERROR_STA_KEY_NOT_EXISTED = 306;
    public static final int SEC_ERROR_STA_LOW_VERSION_DATA_FILE = 312;
    public static final int SEC_ERROR_STA_NO_DATA_FILE = 303;
    public static final int SEC_ERROR_STA_NO_MEMORY = 308;
    public static final int SEC_ERROR_STA_NO_SUCH_INDEX = 309;
    public static final int SEC_ERROR_STA_STORE = 200;
    public static final int SEC_ERROR_STA_STORE_DATA_FILE_MISMATCH = 202;
    public static final int SEC_ERROR_STA_STORE_ILLEGEL_KEY = 207;
    public static final int SEC_ERROR_STA_STORE_INCORRECT_DATA_FILE = 204;
    public static final int SEC_ERROR_STA_STORE_INCORRECT_DATA_FILE_DATA = 205;
    public static final int SEC_ERROR_STA_STORE_INDEX_NOT_EXISTED = 209;
    public static final int SEC_ERROR_STA_STORE_INVALID_PARAM = 201;
    public static final int SEC_ERROR_STA_STORE_KEY_NOT_EXSITED = 206;
    public static final int SEC_ERROR_STA_STORE_LOW_VERSION_DATA_FILE = 212;
    public static final int SEC_ERROR_STA_STORE_NO_DATA_FILE = 203;
    public static final int SEC_ERROR_STA_STORE_NO_MEMORY = 208;
    public static final int SEC_ERROR_STA_STORE_NO_SUCH_INDEX = 209;
    public static final int SEC_ERROR_STA_STORE_UNKNOWN_ERROR = 299;
    public static final int SEC_ERROR_STA_UNKNOWN_ERROR = 399;
    public static final int SEC_ERROR_UMID_ENVIRONMENT_CHANGED = 906;
    public static final int SEC_ERROR_UMID_GET_URL_ERROR = 903;
    public static final int SEC_ERROR_UMID_INVALID_PARAM = 901;
    public static final int SEC_ERROR_UMID_NETWORK_ERROR = 904;
    public static final int SEC_ERROR_UMID_NO_NETWORK_INIT = 907;
    public static final int SEC_ERROR_UMID_SERVER_RESP_INVALID = 905;
    public static final int SEC_ERROR_UMID_THREADPOOL_FULL = 902;
    public static final int SEC_ERROR_UMID_TIME_OUT = 908;
    public static final int SEC_ERROR_UMID_UNKNOWN_ERR = 999;
    public static final int SEC_ERROR_UMID_VALID = 900;
    public static final int SEC_ERROR_UNIFIED_SECURITY = 2400;
    public static final int SEC_ERROR_UNIFIED_SECURITY_GET_MINIWUA_FAILED = 2404;
    public static final int SEC_ERROR_UNIFIED_SECURITY_GET_SIGN_FAILED = 2405;
    public static final int SEC_ERROR_UNIFIED_SECURITY_GET_UMT_FAILED = 2406;
    public static final int SEC_ERROR_UNIFIED_SECURITY_GET_WUA_FAILED = 2407;
    public static final int SEC_ERROR_UNIFIED_SECURITY_INIT_FAILED = 2403;
    public static final int SEC_ERROR_UNIFIED_SECURITY_INVALID_PARA = 2401;
    public static final int SEC_ERROR_UNIFIED_SECURITY_NO_APPKEY = 2402;
    public static final int SEC_ERROR_UNIFIED_SECURITY_UNKONWN_ENCODING_ERROR = 2498;
    public static final int SEC_ERROR_UNIFIED_SECURITY_UNKONWN_ERROR = 2499;
}
```

