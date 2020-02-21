# -*- coding: UTF-8 -*-

import random
import string
import os
import re
from spider import m3u8Spider
from downloader import downloader
from sys import argv

# example:python3 cmd.py http://www.jiaxingren.com/folder24/folder147/folder149/folder170/2018-10-25/416269.html

CWD = os.getcwd()
M3U8_DIR = os.path.join(CWD, 'm3u8')
M3U8_FILE = os.path.join(M3U8_DIR, 'm3u8.txt')

def writeM3U8(websiteUrl):
    # 实例化爬虫
    p = m3u8Spider.M3u8Spider(websiteUrl)
    # 创建代理ip池
    if (p.createProxyIpPool()):
        # 生成代理地址
        proxyUrl = p.getProxyUrl()
        # 生成用户代理
        userAgent = p.getUserAgent()
        header = {
            'user-agent': userAgent
        }
        # 获取m3u8di地址列表
        m3u8List = p.getM3u8List('', header)
        print(m3u8List)

        # if len(m3u8List) > 0:
        #     saveDir = 'download/'
        #     file = 'video.mp4'
        #     # 初始化下载参数
        #     options = {
        #         'm3u8Url': '',
        #         'saveDir': saveDir,
        #         'file': file,
        #         'downloadParams': '-vcodec copy -acodec copy -absf aac_adtstoasc'
        #     }
        #     for m3u8Url in m3u8List:
        #         options['m3u8Url'] = m3u8Url
        #         options['file'] = ''.join(random.sample(
        #             string.ascii_letters + string.digits, 16)) + '.mp4'

        #         # 提取m3u8流，生成mp4
        #         down = downloader.Downloader(options)
        #         res = down.download()
        #         print(res)

        # 文件夹不存在创建
        if not os.path.exists(M3U8_DIR):
            os.mkdir(M3U8_DIR)

        # 写入文本
        if len(m3u8List) > 0:
            for m3u8Url in m3u8List:
                fp = open(M3U8_FILE, 'a', encoding='utf-8')
                fp.writelines(m3u8Url + '\n')
                fp.close()

if __name__ == '__main__':
    websiteUrl = ''
    if len(argv) < 2:
        exit('请输入网页地址')
    else:
        websiteUrl = argv[1]

    if websiteUrl == '':
        exit('请输入网页地址')
    elif re.match(r'^http[s]?:/{2}\w.+$', websiteUrl) is None:
        exit('请输入合法的网页地址')
    else:
        writeM3U8(websiteUrl)