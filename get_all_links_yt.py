import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib2
import json

#http = httplib2.Http()
#status, response = http.request('https://www.yahoo.com')
#
#for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#    print link
#    try:
#        if "<a" in str(link):
#            print "|||||||"
#            print "================="
#            print link['href']
#            print "================="
#    except Exception as e:
#        # print e
#        pass


#print "==========================================="


#request = urllib2.Request("https://www.yahoo.com")
#response = urllib2.urlopen(request)
#soup = BeautifulSoup(response)
#for a in soup.findAll('link'):
#    print "Hereeeeee============="
#    print a['href']
#print "==========================================="

#href=[]
#
#def fetch_links(link):
#    http = httplib2.Http()
#    status, response = http.request(link)
#
#    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#        try:
#            n_link = link['href']
#            if "<a" in str(link) and n_link not in href :
#                href.append(n_link)
#                print "==============="
#                print n_link
#                print "==============="
#                if "http" in n_link or "www" in n_link:
#                    fetch_links(n_link)
#        except Exception as e:
#            # print e
#            break
#
#
#fetch_links('https://www.google.com/')
print "==========================================="
href=[]

#def fetch_links(link):
#    http = httplib2.Http()
#    status, response = http.request(link)
#    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#        soup = BeautifulSoup(response)
#        try:
#            #if "<a" in str(link) and n_link not in href :
#            #    print link.findAll('a',{'class':'content-link spf-link yt-uix-sessionlink spf-link'})
#            #    if 'watch' in n_link:
#            #        #print n_link
#            #        #if "watch" in n_link or "youtube" in n_link:
#            #        href.append(n_link)
#            #        n_link = "https://www.youtube.com/"+str(n_link)
#            #        v=soup.findAll("div", { "class" : "watch-view-count" })
#            #        views = json.dumps(v[0].text)
#            #        views = views.split(" views")[0]
#            #        views = int(views.replace(',','').replace('"',''))
#            #        fetch_links(n_link)
#        except Exception as e:
#            print e
import sys
import random as r

def fetch_side_bar_links(l):
    http = httplib2.Http()
    status, response = http.request(l)
    soup = BeautifulSoup(response)
    s=soup.findAll("div", { "id" : "watch7-sidebar-modules"})
    for div in s:
        new_link = div.find('a')['href']
        if len(str(new_link)) == '20':
            new_link = "https://www.youtube.com"+str(new_link)
            print "=========================="
            print new_link
            fetch_links(new_link)
            break



f=open('1c_links.txt',"w")

def fetch_links(ln):
    http = httplib2.Http()
    status, response = http.request(ln)
    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        soup = BeautifulSoup(response)
        try:
            hr = link.get('href')
            if "watch" in hr:
                l= str(hr)
                if len(l) ==20: 
                    l="https://www.youtube.com"+l
                    if l not in href:
                        v=soup.findAll("div", { "class" : "watch-view-count" })
                        views = json.dumps(v[0].text)
                        views = views.split(" views")[0]
                        views = int(views.replace(',','').replace('"',''))
                        if len(href) == 0:
                            l = ln
                            f.write(l+ " +++++ " +str(views))
                            print l+ " +++++ " +str(views)
                        else:
                            if views > 100000000:
                                f.write(ln+ " +++++ " +str(views))
                                print ln+ " +++++ " +str(views)
                            else:
                                print ln+ " ====> " +str(views)
                        href.append(l)
                        fetch_links(l)
        except Exception as e:
            print e
            if "Only absolute URIs are allowed" in str(e):
                break
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
            fetch_side_bar_links(r.choice(l))

#fetch_links('https://www.youtube.com/watch?v=S9bCLPwzSC0')
fetch_links('https://www.youtube.com/watch?v=rrNbLBS1D2Q') #errortest
#fetch_side_bar_links('https://www.youtube.com/watch?v=S9bCLPwzSC0')
f.close()
