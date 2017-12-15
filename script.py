#!/usr/bin/env python
#! -*- coding:utf-8 -*-
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
            text = selector.xpath('//title/text()') #返回为一列表
            # print text
            bug_info = text[0]
            title, bug_id, wooyun = bug_info.split('|')
            # print bug_id.strip(), '-', title.strip(), '--', f.strip()

        with open('index.html', 'a+') as fp:
            bug = '编号: ' + bug_id.strip() + '&emsp;&emsp;' + '<a href="' + f.strip() + '">' + title.strip() + '</a></br>'
            print bug
            fp.write(bug)

    print '[*] Done ...'

if __name__ == '__main__':
    main()
