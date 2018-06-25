from urllib.request import urlopen
from bs4 import BeautifulSoup
#import re
#getUrl = 'http://www.google.co.in/'

'''
Write a program that takes website URL as input and print all the external links from that URL.
E.g. if URL is google.com, we should output all the external website links from google.com
'''
getUrl = input("Enter URL: ") # get the input URL from the user
req = urlopen(getUrl) # Request to the URL
readhtml = req.read() # Read HTML Code

soup = BeautifulSoup(readhtml, "lxml") # Use bs4 for the reading and pulling the data from the URL
linksURL = soup.find_all('a') # it is going to find all the hyperlinks
# loop to find the tags in using the list of <a> tags
for getTag in linksURL: 
    urlLinks = getTag.get('href',None) # get the URL using href
    if urlLinks is not None: 
        print(urlLinks)