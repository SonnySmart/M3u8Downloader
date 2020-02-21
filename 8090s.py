# -*- coding: UTF-8 -*-

import cmd
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = 'http://8090s.cc'
CLASS = [
    '/type/1.html', # 电影
    '/type/2.html', # 连续剧
]

def getPlay(url):
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    res = http.request('get', url)
    html = res.data
    html = html.decode('utf-8')
    # 匹配链接 href="/play/94999-1-1.html"
    pattern = re.compile(r'/play/\d+-1-1.html')
    httpLinkList = re.findall(pattern, html)
    httpLinkList = list(set(httpLinkList))
    for httpLink in httpLinkList:
        m3u8_url = HOST + httpLink
        cmd.writeM3U8(m3u8_url)
        print(httpLink)

def getRecommend(url):
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    res = http.request('get', url)
    html = res.data
    html = html.decode('utf-8')
    #print(html)

    # 匹配链接 href="/detail/94999.html"
    pattern = re.compile(r'/detail/\d+.html')
    httpLinkList = re.findall(pattern, html)
    httpLinkList = list(set(httpLinkList))
    for httpLink in httpLinkList:
        play_url = HOST + httpLink
        #print(play_url)
        getPlay(play_url)

def main():
    for c in CLASS:
        url = HOST + c
        print(url)
        getRecommend(url)

if __name__ == '__main__':
    main()