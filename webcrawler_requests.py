
# Webcrawling Example using REQUESTS
# Dan Zaratsian
# Nov 2014
# Requests      (http://docs.python-requests.org/en/latest/)
# BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


import requests, re, time
from BeautifulSoup import BeautifulSoup


# Create header with user-agent
headers = {'User-Agent': 'My User Agent 1.0'}

rawdata = requests.get("http://www.reddit.com/search?q=python", headers=headers)

# Check status for successful url request (200 is typically what you are looking for)
rawdata.status_code

soup = BeautifulSoup("".join(rawdata.text))


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