import feedparser
from bs4 import BeautifulSoup
import html5lib
import urllib.request


def feed_finder(url):
        
        feeds=[]
        resp=urllib.request.urlopen(url)
        soup=BeautifulSoup(resp,"html5lib")
        for link in soup.find_all('a',href=True):
            links=link['href']
            if (links.startswith("atom") or links.startswith("rss") or links.endswith(".org/atom.xml") or links.endswith(".org/rss10.xml") or links.endswith(".org/rss20.xml")):
             feeds.append(links)
             #print(len(feeds))
             print(links)
        if(len(feeds)==0):
            feed= url + "atom.xml"
            print(feed)
        elif(feeds[0].startswith('http')):
            feed=feeds[0]
            print(feed)
        else:
            #url="http://planet.openstack.org/"
            feed = url + feeds[0]
            print(feed)
        return feed 
    


def prepare_output(url):
    
    feed= feed_finder(url)
    parser=feedparser.parse(feed)
    
        #length=len(parser['entries'])
        #print(length)
    with open("output.txt","a") as f:
            f.write("\n")
            for post in parser.entries:
              f.write("\n")
              f.write("TITLE ->\t")
              f.write(post.title)
              f.write("\n")
              f.write("POSTED ON : ->\t")
              f.write(post.date)
              f.write("\n")
              f.write("LINK ->\t")
              f.write(post.link)
              f.write("\n")
              f.write("\n---------------------------------------------------------------")
              
def p_output(url):
    
    feed= feed_finder(url)
    
              
    
def title(url):
    
     content=urllib.request.urlopen(url).read()
     soup=BeautifulSoup(content,"html5lib")
     text=soup.get_text()
     title=soup.title.string
     
     return title

def switch_case(argument):
    switcher = {
        1: 'http://fedoraplanet.org/',
        2: 'http://planetpython.org/',
        3: 'http://planet.openstack.org/',
        4: 'http://planet.gnome.org/',
        5: lambda: "five",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func

if __name__ == '__main__':
        #url= "http://planet.gnome.org/"
        print("\n\t***WEBSITE LIST***")
        print("\n-------------------------------------")
        print(" 1 : http://fedoraplanet.org/ \n 2 : http://planetpython.org/ \n 3 : http://planet.openstack.org/ \n 4 : http://planet.gnome.org/")
        print("\n-------------------------------------")
        argument = int(input("\n\tSelect a Website From List For Website Extraction Process: "))
        if (argument>4):
            print("\nWrong Choice!!!")
        
        
        else:
             url=switch_case(argument)
             date=feedparser.parse(url).updated
             tit=title(url)
             
             with open("output.txt","a") as f:
                  f.write("\n\t\t")
                  f.write("PLANET NAME ->\t")
                  f.write(tit)
                  f.write("\n\t\t")
                  f.write("DATE ->")
                  f.write(date)
                  f.write("\n---------------------------------------------------------------")
                  
             prepare_output(url)
             '''feed= feed_finder(url)
             prepare_output(feed)
             parser=feedparser.parse(feed)
        #length=len(parser['entries'])
        #print(length)
        with open("output.txt","a") as f:
            f.write("\n")
            for post in parser.entries:
              f.write("\n")
              f.write("TITLE ->\t")
              f.write(post.title)
              f.write("\n")
              f.write("LINK ->\t")
              f.write(post.link)
              f.write("\n")
              f.write("\n---------------------------------------------------------------")
        #print(parser)
        #title = parser['entries'][1].title
        #print(title)"""'''
