#########################
#What is web scrapping? Why it is needed?: ecommerce , Trivago, FLightbooking.
#Legal issue?: Linked in or facebook or twitter for fake profiles : illegal.
#Process of web scrapping: Load the doc/page >> Parsing >> Extraction >> Transformation.
####################
#Beautiful soup is web scarapper in pyhton..
#another module available in python are Scrapy , request, pattern, mechanize,xpath.

####################
#Installation and prerequists.
pip install beautifulsoup4
pip install requests 

################

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Method to get the hml code as string of any website. Normal Method without beautifulsoup . 
pagecontent = urlopen('https://www.moneycontrol.com/news/business/markets/share-market-live-updates-stock-market-today-august-19-latest-news-bse-nse-sensex-nifty-ajanta-pharma-niit-zee-entertainment-enterprises-hindustan-aeronautics-adani-enterprises-5725691.html').read()
print(pagecontent)
# BeautifulSoup Method which is having more powerfull features. Above code of normal parser using urlopen will not work for indiatimeswebsite and gives 403 error as FOrbidden but BeautifulSoup should work on all website.  
page = requests.get('https://economictimes.indiatimes.com/indices/sensex_30_companies?from=mdr') # To get the request page.
print(page)

## Amazon example:

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://www.amazon.in/s?k=samsung+m21&crid=3TA8Z3JOU5SJR&sprefix=sams%2Caps%2C587&ref=nb_sb_ss_i_1_4'
uclient=urlopen(url)
myhtml=uclient.read()
uclient.close()
my_soup=BeautifulSoup(myhtml, 'html.parser')
containers=my_soup.find_all('div',{'class': 'a-section a-spacing-medium'})
print(len(containers)) # total number no of products.
#print(BeautifulSoup.prettify(containers[0])) # to print the html in well formatted way.
#print(containers[0].div.img['alt'])
price=my_soup.find_all('div',{'class': 'a-price a-text-price'})
print(price[0].text)

### Example:
## PLease note you may get http 503 error "Service not available" due to internett/connection issue. Please retry. 

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://www.amazon.in/s?k=samsung+m21&crid=3TA8Z3JOU5SJR&sprefix=sams%2Caps%2C587&ref=nb_sb_ss_i_1_4'
uclient=urlopen(url)
myhtml=uclient.read()
uclient.close()
my_soup=BeautifulSoup(myhtml, 'html.parser')
#print(my_soup)
#containers=my_soup.find_all('div',{'class': 'a-section a-spacing-medium'})
#containers=my_soup.find_all('div',{'class': 's-include-content-margin s-border-bottom s-latency-cf-section'})
containers=my_soup.find_all('span',{'class': 'a-size-medium a-color-base a-text-normal'})
prices=my_soup.find_all('span',{'class': 'a-price-whole'})
print(len(containers)) # total number no of products.
for i in range(len(containers)):
  print("productname: ",str(containers[i])[65:123])
  print('*********Price is ********',prices[i].text)# details of first products.
#print(BeautifulSoup.prettify(containers[0])) # to print the html in well formatted way.
#print(containers[0].div.img['alt'])
#price=my_soup.find_all('div',{'class': 'a-price a-text-price'})
#print(price[0].text)


### Multi Threading: Perform different/multi task at same time. Downloading something and playing music. 

"""Multitasking: Multitasking is having 2 part. Multi Process and MultiThread.
Mutliprocess: multi process in same oS. smaallest task is process in same OS.
Multithreading: Same process and multiple thread. smallest unit is multi thread.

Thread: independent flow of execution.

### Multithreading can be achived in three ways:
1) Wihtout OOPs (Without class)
2) With Oops (BY extending thread class)
3) Without extendign thread class.
"""
#1) Without OOPS.

from threading import *
print(current_thread().getName())

def abc():
    print('Hello')
t1=Thread(target=abc) 
t1.start() # to run the thread.
t1.join() # to join the thread with another thred.

#Sleep
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

2) With OOPS.

from threading import *
class mythread(Thread):
    def run(self):
        for i in range(10):
            print('hi', current_thread().getName())
           
a=mythread()
#a.run() # normal menthod call with main thread execution.
a.start() # Threading concept used and execution will be in new thread. 
   
#Example:

from threading import *
print('Hello')
print(current_thread().getName())
print('Hi')
def abc():
    print('Hey',current_thread().getName())
t1=Thread(target=abc)
abc() # bydefault by main thread 
t1.start() # called with separate thread.   


## Example 2:
from threading import *
import time
print('Hello',current_thread().getName())
def abc():
    for i in range (10):
     print('Hey',current_thread().getName())
     time.sleep(1)
def pqr():
    for i in range (10):
     print('HeyHello',current_thread().getName())
     time.sleep(1)        
t1=Thread(target=abc)
t2=Thread(target=pqr)
t1.start()
t2.start()
t1.join()
print('Bye', current_thread().getName()) 









			
