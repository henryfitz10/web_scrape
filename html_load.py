from urllib2 import urlopen
import re
from bs4 import BeautifulSoup
import os

my_address =  "https://www.irishtimes.com/"
html_page = urlopen(my_address)
html_text = html_page.read()

soup = BeautifulSoup(html_text, "html.parser") # second param tells bs which parser to use

# scrape all images

images = []
images= soup.find_all("img")
for img in images:
    print img['src']






