# -*- coding: utf-8 -*-
# Version: V1.0.0
# Brief: tool to scrapy youtube video
# Author: ytouch
# ModifyUpdate:
# VersionUpdateInfo:

#需要安装库 ：
#pip install pafy
#pip install youtube-dl

import pafy

class YoutubeVideoDownload():

    def __init__(self,url):
        self.download_url = url  #绑定到url

    def runDownload(self,save_path):
        self.save_path = save_path #设置保存路径
        #开始下载
        video = pafy.new(self.download_url)
        v_best =video.getbest() #下载最清晰画质
        v_best.download(self.save_path)

# 使用该类的方法
if __name__ == '__main__':

    youtube = YoutubeVideoDownload('https://www.youtube.com/watch?v=sukA8NGQ9Z0&list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&index=1') #先实例化该类，设置需要下载的url
    youtube.runDownload('./video/') #设置保存路径，并执行下载

