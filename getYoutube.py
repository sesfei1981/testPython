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

    #youtube = YoutubeVideoDownload('/watch?v=fohmU9F_yfE&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=5')
    #youtube = YoutubeVideoDownload('/watch?v=A0MlVhJ1aNw&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=7')
    #youtube = YoutubeVideoDownload('/watch?v=WabgjU4gELI&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=1')
    #youtube = YoutubeVideoDownload('/watch?v=sukA8NGQ9Z0&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=2')
    #youtube = YoutubeVideoDownload('/watch?v=DNdvUKj4vRM&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=3')
    #youtube = YoutubeVideoDownload('/watch?v=mT1C_r4tpjM&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=4')
    #youtube = YoutubeVideoDownload('/watch?v=fohmU9F_yfE&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=5')
    #youtube = YoutubeVideoDownload('/watch?v=BSzOK6sH3wc&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=6')
    #youtube = YoutubeVideoDownload('/watch?v=A0MlVhJ1aNw&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=7')
    #youtube = YoutubeVideoDownload('/watch?v=XOrAA4wwuyY&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=8')
    #youtube = YoutubeVideoDownload('/watch?v=WSU0y3F94Bo&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=9')
    #youtube = YoutubeVideoDownload('/watch?v=ARUzKgLFjI8&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=10')
    #youtube = YoutubeVideoDownload('/watch?v=CrJ7QCCt7m8&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=11')
    #youtube = YoutubeVideoDownload('/watch?v=Q2SYU0pLj2E&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=12')
    #youtube = YoutubeVideoDownload('/watch?v=Tu3s2zttrvQ&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=13')
    #youtube = YoutubeVideoDownload('/watch?v=dVtUUR9ELSw&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=14')
    #youtube = YoutubeVideoDownload('/watch?v=s6iX1etiG_s&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=15')
    #youtube = YoutubeVideoDownload('/watch?v=f0W8ec3XMPI&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=16')
    #youtube = YoutubeVideoDownload('/watch?v=ZkzqeJ0VYTE&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=17')
    #youtube = YoutubeVideoDownload('/watch?v=0rN2pMhutmw&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=18')
    #youtube = YoutubeVideoDownload('/watch?v=gGK_S4W8j78&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=19')
    #youtube = YoutubeVideoDownload('/watch?v=BHm7dq0-mxQ&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=20')
    #youtube = YoutubeVideoDownload('/watch?v=lcBUG2zGjc4&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=21')
    #youtube = YoutubeVideoDownload('/watch?v=o3sU-u_3GvU&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=22')
    #youtube = YoutubeVideoDownload('/watch?v=aZLVMuWp6aw&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=23')
    #youtube = YoutubeVideoDownload('/watch?v=V8y9sREBTxs&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=24')
    #youtube = YoutubeVideoDownload('/watch?v=LfmkOhdkLCk&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=25')
    #youtube = YoutubeVideoDownload('/watch?v=-gIFJw0B82w&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=26')
    #youtube = YoutubeVideoDownload('/watch?v=sIqVdZkVXas&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=27')
    #youtube = YoutubeVideoDownload('/watch?v=DmvZdDHCeIk&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=28')
    #youtube = YoutubeVideoDownload('/watch?v=3qNc9An3DUY&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=29')
    #youtube = YoutubeVideoDownload('/watch?v=WUc9ehm7Kt8&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=30')
    #youtube = YoutubeVideoDownload('/watch?v=GIdOQW3RNdw&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=31')
    #youtube = YoutubeVideoDownload('/watch?v=qQ1SpUEheOM&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=32')

    youtube = YoutubeVideoDownload('https://www.youtube.com/watch?v=qQ1SpUEheOM&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=32') #先实例化该类，设置需要下载的url
    youtube.runDownload('./video/') #设置保存路径，并执行下载

