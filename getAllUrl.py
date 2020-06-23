# -*- coding: UTF-8 -*-
import re
import urllib
import os
def getHtml(url):
        page=urllib.urlopen(url)
        html=page.read()
        return html

def getMp4(html):
        filePath = './'
        downloaded = os.listdir(filePath)
        r=r"href=\"(\/watch.*list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv.*index=[0-9]+).*"
        re_mp4=re.compile(r)
        #print html

        #href="/watch?v=WabgjU4gELI&amp;list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&amp;index=1">
        

        mp4List=re.findall(re_mp4,html)
        print "--------"
        #print mp4List
        filename=0
        dest = "https://www.youtube.com"
        for mp4name in mp4List:
                if mp4name in downloaded:
                    pass
                else:
                    print mp4name
                    mp4url = dest+mp4name
                    urllib.urlretrieve(mp4url,"%s" %mp4name)
                    print 'file "%s" done' %mp4name
                filename+=1
        print 'totally "%s" files have been dowloaded' %filename
url = "https://www.youtube.com/watch?v=BSzOK6sH3wc&list=PLu3b11EPo_MfxhGAgO1LTJuDLTMCHIGLv&index=6"
html=getHtml(url)
getMp4(html)