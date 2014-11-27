
# Webcrawling Example using URLLIB2
# Dan Zaratsian
# Nov 2014
# urllib2       (https://docs.python.org/2/library/urllib2.html)
# BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


import urllib2, re, time
from BeautifulSoup import BeautifulSoup


rawdata = urllib2.urlopen("http://www.reddit.com/search?q=python").read()

soup = BeautifulSoup("".join(rawdata))


# Example Output #1 - Print Reddit questions
print '\n\nPrinting questions...\n\n'
time.sleep(2)
for question in soup.findAll("a", {"class": "title may-blank "}):
    print question.text


# Example Output #2 - Print authors
print '\n\nPrinting authors...\n\n'
time.sleep(2)
for author in soup.findAll("a", {"class": re.compile(r'author may-blank .+')}):
    print author.text


#END