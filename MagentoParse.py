import urllib2

#DomainList.txt should looks like http://domain.com/admin
fileDomain = open("DomainList.txt")
fileMagento = open("DiscoveredMagento.txt","w")

for line in file:
    try:
        response = urllib2.urlopen(line[:-1])
        html = response.read()
        BufStr = str(html)
        BufSer = BufStr.find("Magento")
        if BufSer != -1:
            fileMagento.write(line+"\n")
            print line
    except:
         pass
#To do parse all versions
