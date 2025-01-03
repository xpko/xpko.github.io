# 谷歌网页索引

本来google的网页索引只要在google search console里的站点地图里提交sitemap.xml即可，但实测提交后，发现返回**无法获取**，经尝试众多方案后无果（基本上跟这个帖子遇到的是一样的：[Please help, google cannot fetch my sitemap, tried everything](https://www.reddit.com/r/TechSEO/comments/12p2bs7/please_help_google_cannot_fetch_my_sitemap_tried/) ），值得另寻他径

## Google search console api 方案

官方文档：https://developers.google.com/webmaster-tools/about?hl=zh-cn





## Google indexing api

官方文档：https://developers.google.com/search/apis/indexing-api/v3/quickstart?hl=zh-cn

Indexing API主要用于**特定类型的内容**，如**招聘信息（Job Postings）**和**直播事件（Live Streaming）**。

## 用到工具

站点地图验证工具：https://www.xml-sitemaps.com/validate-xml-sitemap.html



## 问题填坑

```
问题：(caused by proxyerror('unable to connect to proxy', filenotfounderror(2, 'no such file or directory')
```

将urllib3降到1.25.11

```
http://localhost:4000/wechat/Should%20We%20Chat,%20Too%20Security%20Analysis%20of%20WeChat%E2%80%99s%20MMTLS%20Encryption%20Protocol/WeChat%20Crypto%20diagrams%20(inner%20layer).png
```

```
http://localhost:4000/wechat/Should%20We%20Chat,%20Too%20Security%20Analysis%20of%20WeChat%E2%80%99s%20MMTLS%20Encryption%20Protocol/Should%20We%20Chat,%20Too%20Security%20Analysis%20of%20WeChat%E2%80%99s%20MMTLS%20Encryption%20Protocol/WeChat%20Crypto%20diagrams%20(inner%20layer).png
```

