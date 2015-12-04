

# Hardware Validation:

**Create a python command line tool which will**

    #extracts posts from these websites using atom feeds.

        #Following websites:

            *http://fedoraplanet.org/

            *http://planetpython.org/

            *http://planet.openstack.org/

            *https://planetkde.org/

            *http://planet.gnome.org/

    # From extracted data, create a plain text report which will show:

        #Title having Feeds on <date>

         Followed by these sub-sections

        #Planet Name

            *Blog Title

            *Author

            *Contents

            *Comments - commentted by and no. of comments

            *Links from each post

            *Images from each post


## IMPLEMENTATION: **Python 3.4.3**


1)Take the given link and find the [Feeds] 

  (https://en.wikipedia.org/wiki/Web_feed) present in that link 

  (such as atom,rss etc and file with xml extension.


2)Select one of the feed and extract it using any parser such as 

  [feedparser](https://pypi.python.org/pypi/feedparser)(It only 

  work for feeds).


3)By using feedparser you can Extract many things such as 

  Title,date,link,feed,version,entries and status etc.


4)Extract other data such as Hyperlinks,image links,blogs etc by 

  some other python parser such as [Htmldom](https://pypi.python.org/pypi/htmldom),[urllib](https://docs.python.org/2/library/urllib.html),[Beautifulsoup](http://www.crummy.com/software/BeautifulSoup/) etc.


5)Prepare the simple text report showing different fields such as 

  Planet name,Date,Contents,Hyperlinks,Image links etc


## OUTPUT MENU->



**WEBSITE LIST**

-------------------------------------
 1 : http://fedoraplanet.org/ 
 2 : http://planetpython.org/ 
 3 : http://planet.openstack.org/ 
 4 : http://planet.gnome.org/

-------------------------------------

(*)Select a Website From List For Website Extraction Process: 













