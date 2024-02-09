import os
from bs4 import BeautifulSoup
import requests
import re

# 判断是否为首次使用
if os.path.exists('data'):
    pass
else:
    with open('data', 'w') as fp:
        fp.write('/storage/emulated/0/Download/')
    print('填类似于这样的目录:\n/storage/emulated/0/netease/cloudmusic/Music/\n留空，则默认为：/storage/emulated/0/Download/')
    path = input('请输入你的下载目录：')
    with open('data', 'w') as fp:
        fp.write(path)
    


def main():

    
    share_url = 'http'+share_url.split('http')[1][:-11]
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; SM-N9600 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/12.0 Mobile Safari/537.36 COVC/045816'}
    
    with open('data', 'r') as fp:
        path = fp.read()
    
    if path == '':
        path = '/storage/emulated/0/Download/'
    
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    
    
    def get_url(share_url): # 获得音乐的id，然后返回音乐直链
    
        responds = requests.get(url=share_url, headers=headers)
        soup = BeautifulSoup(responds.text, 'html.parser')
        
        a = str(soup.find_all('script')[-2]).split('\n')
        a = a[1:-1]
        b = ''
        for i in a:
            b += i
        url = eval(b)['@id']
        id = url[url.find('id=')+3:].split('&')[0]
        
        name = soup.title.getText()[:-13]
        return 'https://music.163.com/song/media/outer/url?id='+id,name.replace('/','、')+'.m4a'
    
    
    def rename(s): # 这个函数是合法化文件名称，作者太懒了，直接复制于 百度旗下的AI语言模型，文心一言
        # 替换非法字符
        s = re.sub(r'[\\/*?:"<>|]', '_', s)
        # 删除前导的点（在某些操作系统中，这可能会导致问题）
        s = re.sub(r'^\.', '', s)
        # 删除尾随的点
        s = re.sub(r'\.$', '', s)
        return s
    
    
    
    
    
    def download(url,name):
        responds = requests.get(url=url, headers=headers)
        with open(path+name, 'wb') as fp:
            fp.write(responds.content)
    
    
    
    music_url,name = get_url(share_url)
    name =rename(name)
    download(music_url,name)
    print('\n下载成功，',name, '已保存到', path, '\n')

while True:
    try:
        print('如果您想退出，请输入 退出 或者 q 或者 exit')
        share_url = input('分享的链接：')
        if share_url = 'q' or 'Q' or '退出' or 'exit' or 'Exit' or 'quit' or 'Quit':
            break
        
        main()
        
    except:
        print('下载失败，主要有以下原因：\n1. 不是网易云分享的原内容（如：分享葛东琪的单曲《悬溺》: http://163cn.tv/nhndX0 (来自@网易云音乐)）一个字都不能删除，直接复制粘贴就好。\n2.不是网易云的音乐。\n3.该音乐只有VIP才能试听。\n4.设置的目录有问题，可以运行命令  python repair.py   解决。（运行后不会填可以留空，直接回车）\n5.网络异常。\n6.没有安装bs4，requests模块\n\n联系作者，邮箱3469366353@qq.com ')
