# 1000php
1000个PHP代码审计案例 (2016.7以前乌云公开漏洞)

在原来的基础上[Xyntax/1000php](https://github.com/Xyntax/1000php)添加了简单的漏洞索引，并且加入了原css文件，方便查看

## Sample

![image](https://raw.githubusercontent.com/starnightcyber/1000php/master/pic/wooyun-index.png)

点击其中某个漏洞，查看

![image](https://raw.githubusercontent.com/starnightcyber/1000php/master/pic/bug.png)

刚才试过了，直接打开index.html好像并不会简单按照我们的意愿显示，可以重新再执行一下代码：

python script.py

这样会重新生成index.html，在本地打开应该就没有问题，另外可能会出现乱码，可以用谷歌浏览器打开。

说明
---
* 数据取自3.8W乌云已公开漏洞(截至2016.7)
* 漏洞在`./bugs`,`./upload`保存了相关漏洞的图片资源
* 使用特征匹配提取,杂质在5%以内,如遇其他非php漏洞自行删除即可
* 愿乌云早日回归
