# 将github仓库无侵入转换为github-pages

啥叫无侵入？

就是在转换为github-pages后，通过github仓库依然可以正常查看readme.md

第一先开启github pages

jekyll-gh-pages.yml

第二开启github action



## 建立readme.md索引

通过py脚本遍历仓库下所有md文档，然后在主md里建立一个索引目录，脚本代码见：[generate_directory_index.py](https://github.com/xpko/xpko.github.io/blob/master/generate_directory_index.py)

对应的github action: [update-readme-index.yml](https://github.com/xpko/xpko.github.io/blob/master/.github/workflows/update-readme-index.yml)



但现在有一个问题：readme.md里的.md后缀，不会替换成.html或空

问题探究：

经过分析github action 代码，发现核心代码在[pages-gem](https://github.com/github/pages-gem)上

相关issue: [reason for blacklisting plugins?](https://github.com/github/pages-gem/issues/926)

​         ^ TODO:  该issue下给出了一个绕过白名单限制的解决方案，后面有时间可以研究下

相关issue: [Links with titles not handled properly](https://github.com/github/pages-gem/issues/876)

​         ^ 据该issue提示：问题出在jekyll-relative-links这个插件上，版本为0.6.1，但其已在[0.7.0](https://github.com/benbalter/jekyll-relative-links/releases/tag/v0.7.0)版本已修复，但官方一直不处理

经过分析Pages-gem项目提交记录，发现v229~v230已经更新到了0.7.0，但在v231又降回去了，commit: [pages-gem/commit/c29f89c3c](https://github.com/github/13c55cfc4aec49d58089a58c123e980)

​        ^ 因此现在只要在action里指定该[Pages-gem v230](https://github.com/github/pages-gem/releases/tag/v230)，也就是[Jekyll-build-pages v1.0.11](https://github.com/actions/jekyll-build-pages/releases/tag/v1.0.11)版本：

```yaml
uses: actions/jekyll-build-pages@v1.0.11
```



推荐：

一个快速部署（克隆->改名->完成）jekyll博客的开源项目：[jekyll-now](https://github.com/barryclark/jekyll-now)















