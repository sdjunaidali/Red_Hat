from bs4 import BeautifulSoup
import urllib.request
import feedparser
import html5lib
import requests
import urllib
import re



def feed_finder(url):

        """Function to find the feeds present in the given websites"""

        
        feeds=[]
        resp=urllib.request.urlopen(url)
        soup=BeautifulSoup(resp,"html5lib")
        for link in soup.find_all('a',href=True):
            links=link['href']
            if (links.startswith("atom") or links.startswith("rss") or links.endswith(".org/atom.xml") or links.endswith(".org/rss10.xml") or links.endswith(".org/rss20.xml")):
             feeds.append(links)
             #Searching for feed links,like atom.xml,rss.xml etc.
        if(len(feeds)==0):
            feed= url + "atom.xml"
        
        elif(feeds[0].startswith('http')):
            feed=feeds[0]

        else:
            feed = url + feeds[0]
            
        return feed



def linker(url):

       """Function to make list of links of post on given websites"""

       lin=[]
       #lin[] is for storing links associated with different blogs.
       feed= feed_finder(url)
       parser=feedparser.parse(feed)
       for post in parser.entries:
            lin.append(post.link)
       return lin


def link_finder(url):

         """Function to find hyperlinks present in blogs of given websites"""


         lin=[]
         #lin[] is for storing links associated with different blogs.
         lin = lin + linker(url)
         try:
               for i in lin:
                 print("\n")
                 print("LINKS IN POST {} ->".format(i))
                 resp=urllib.request.urlopen(i)
                 soup=BeautifulSoup(resp,"html5lib")
                 for link in soup.find_all('a',href=True):
                  links=link['href']
                  print(links)

         except urllib.error.HTTPError as e:
                 #for handling HTTP errors,such as request for authentication.
                 print("")

         except urllib.error.URLError as f:
                 #handlers raise this exception when they run into program.
                 print("\nNO LINK")
             
             
def image_finder(url):

         """Function to find links of images present in blogs of given websites"""


         lin=[]
         lin = lin + linker(url)
         try:
               for i in lin:
                 print("\n")
                 print("IMAGES PRESENT IN POST {} ->".format(i))
                 resp=urllib.request.urlopen(i)
                 soup=BeautifulSoup(resp,"html5lib")
                 for imgtag in soup.find_all('img'):
                  print(imgtag['src'])

         except urllib.error.HTTPError as e:
                 #for handling HTTP errors,such as request for authentication.
                 print("")

         except KeyError as e:
                 #raises whenever a dict() object is requested and key is not in dictionary.
                 print("")

         except urllib.error.URLError as f:
                 #handlers raise this exception when they run into program.
                 print("\nNO LINK")

                 
             
def prepare_output(url):

    """Function to prepare plain text report showing different aspects of website"""

    
    feed= feed_finder(url)
    parser=feedparser.parse(feed)

    for post in parser.entries:
              print("\n")
              print("AUTHOR & TITLE ->\t")
              print(post.title)
              print("\n\n")
              print("POST LINK ->\t")
              print(post.link)
              print("\n\n")
              
              print("\n---------------------------------------------------------")
    if(argument==1):
      print("\n\t\t***LIST OF BLOGS***\t\t")
      print("\n")
      blog1(url)
    elif(argument==2):
      print("\n\t\t***LIST OF BLOGS***\t\t")
      print("\n")
      blog2(url)
    elif(argument==3):
      print("\n\t\t***LIST OF BLOGS***\t\t")
      print("\n")
      blog3(url)
    else:
      print("\n\t\t***LIST OF BLOGS***\t\t")
      print("\n")
      blog4(url)
    print("\n\t\t***LIST OF HYPERLINKS IN POSTS***\t\t")
    print("\n")
    link_finder(url)
    print("\n\t\t***LINKS OF IMAGES PRESENT IN POSTS***\t\t")
    print("\n")
    image_finder(url)
    
              
def blog1(url):

    """Function to extract blogs of different users from the given website 1"""

    
    contents=[]
    #for storing different blogs present on website given.
    raw=[]
    feed= feed_finder(url)
    page = urllib.request.urlopen(url)
    parser=feedparser.parse(feed)
    r=requests.get(url)
    soup= BeautifulSoup(r.text,"html5lib")

    for hit in soup.find_all(attrs={'class' : 'blog-entry-post'}):#blog-entry-content
      if hit not in contents:
       contents.append(hit)

    len1=len(contents)

    for i in range(0,len1):
       print("POST {} ->".format(i+1))
       print("Post For",parser.entries[i].title)
       print("\n")
       print(contents[i].get_text())
       print("\n--------------------------------------------------------------------------")
       


def blog2(url):

    """Function to extract blogs of different users from the given website 2"""

    
    contents=[]
    #for storing different blogs present on website given.
    raw=[]
    feed= feed_finder(url)
    page = urllib.request.urlopen(url)
    parser=feedparser.parse(feed)
    r=requests.get(url)
    soup= BeautifulSoup(r.text,"html5lib")

    for hit in soup.find_all(attrs={'id' : 'body-main'}):
      if hit not in contents:
       contents.append(hit)

    len1=len(contents)

    for i in range(0,len1):
       print("POST {} ->".format(i+1))
       print("Post For",parser.entries[i].title)
       print("\n")
       print(contents[i].get_text())
       print("\n--------------------------------------------------------------------------")

       

def blog3(url):

    """Function to extract blogs of different users from the given website 3"""

    
    contents=[]
    #for storing different blogs present on website given.
    raw=[]
    feed= feed_finder(url)
    page = urllib.request.urlopen(url)
    parser=feedparser.parse(feed)
    r=requests.get(url)
    soup= BeautifulSoup(r.text,"html5lib")

    for hit in soup.find_all(attrs={'class' : 'channelgroup'}):
      if hit not in contents:
       contents.append(hit)

    len1=len(contents)

    for i in range(0,len1):
       print("POST {} ->".format(i+1))
       print("Post For",parser.entries[i].title)
       print("\n")
       print(contents[i].get_text())
       print("\n--------------------------------------------------------------------------")

       

def blog4(url):

    """Function to extract blogs of different users from the given website 4"""

    
    contents=[]
    #for storing different blogs present on website given.
    raw=[]
    feed= feed_finder(url)
    page = urllib.request.urlopen(url)
    parser=feedparser.parse(feed)
    r=requests.get(url)
    soup= BeautifulSoup(r.text,"html5lib")

    for hit in soup.find_all(attrs={'class' : 'post'}):
      if hit not in contents:
       contents.append(hit)

    len1=len(contents)

    for i in range(0,len1):
       print("POST {} ->".format(i+1))
       print("Post For",parser.entries[i].title)
       print("\n")
       print(contents[i].get_text())
       print("\n--------------------------------------------------------------------------")

    
def title(url):

     """Function to title from different blogs of given websites"""

    
     content=urllib.request.urlopen(url).read()
     soup=BeautifulSoup(content,"html5lib")
     text=soup.get_text()
     title=soup.title.string
     
     return title
 
 
def author(url):

    """Function to extract list of authors from given websites"""

    
    page = urllib.request.urlopen(url)
    soup= BeautifulSoup(page,"html5lib")
    html=soup.prettify()
    author=re.findall('<div class="blog-entry (.*?)">',html,re.DOTALL)
    #searching in html tags using regular expression for authors.
    print(author)
    

def switch_case(argument):

    """Function for Menu"""

        
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

        """Main function for showing menu and perform other operations"""


        
        print("\n\t***WEBSITE LIST***")
        print("\n-------------------------------------")
        print(" 1 : http://fedoraplanet.org/ \n 2 : http://planetpython.org/ \n 3 : http://planet.openstack.org/ \n 4 : http://planet.gnome.org/")
        print("\n-------------------------------------")
        argument = int(input("\n\t(*)Select a Website From List For Website Extraction Process: "))
        if (argument>4):
            print("\nWrong Choice!!!")
        
        
        else:
             url=switch_case(argument)
             date=feedparser.parse(url).updated
             tit=title(url)
             #storing result of title() function in tit.
             print("\n----------------------------------------------------------------")
             print("\n\t\tREPORT OF {} : WEBSITE LINK : {}".format(tit,url))
             print("\n----------------------------------------------------------------")
             print("\n\t\t")
             print("\t\tPLANET NAME ->\t")
             print(tit)
             print("\t\t")
             print("\t\tLAST UPDATED ON ->")
             print(date)
             print("\n---------------------------------------------------------------")
                  
             prepare_output(url)
             #append(url)
             #blog(url)
             #print(lin)
             #author(url)
             #link_finder(url)
             #image_finder(url)
             
             
