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

