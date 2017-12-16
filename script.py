#!/usr/bin/env python
# -*- coding:utf-8 -*-
import glob
import os
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    file_list = glob.glob('bugs/*.html')

    with open('index.html', 'a+') as fp:
        fp.write('<hr>')
        fp.write('<p align="center">--- WooYun漏洞代码审计集锦 ---</p>')
        fp.write('<hr></br>')

    for f in file_list:
        with open(f, 'r') as fp:
            content = fp.read()
            selector = etree.HTML(content)      # 将源码转化为能被XPath匹配的格式
            #print selector
            no = selector.xpath('//*[@id="bugDetail"]/div[@class="content"]/h3/a/text()')[0].strip() #返回为一列表
            title = selector.xpath('//*[@id="bugDetail"]/div[@class="content"]/h3[@class="wybug_title"]/text()')[0][5:].strip() #返回为一列表
            author = selector.xpath('//*[@id="bugDetail"]/div[@class="content"]/h3[@class="wybug_author"]/a/text()')[0].strip() #返回为一列表

            # print no, '-', title, '-', author
            # bug = '编号: '.encode('utf-8') + bug_id.strip() + '&emsp;&emsp;' + '<a href="' + f.strip() + '">' + title.strip() + '</a></br>'
            bug_info = no.strip() + '&emsp;&emsp;' + '<a href="' + f.strip() + '">' + title.strip() + '</a>' + '(' + author.strip() + ')</br>'
            print bug_info

            with open('index.html', 'a+') as fp:
                fp.write(bug_info)


    print '[*] All Done!'

if __name__ == '__main__':
    main()
