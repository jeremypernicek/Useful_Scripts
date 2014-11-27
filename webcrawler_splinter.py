
# Webcrawling Example using REQUESTS
# Dan Zaratsian
# Nov 2014
# Splinter  (https://splinter.readthedocs.org/en/latest/)
# Xpath     (http://scraping.pro/res/xpath-cheat/xpath_css_dom_recipes.pdf)


import time
from splinter import Browser 


#-------------------------------------------------------------------------------------------------------------
# Open Google Chrome and browse to URL (You can also change "chrome" to "firefox" if you want to use Firefox)
browser = Browser('chrome')
url     = 'http://www.reddit.com/search?q=python'
browser.visit(url)
#-------------------------------------------------------------------------------------------------------------


# Example Output #1 - Print Reddit questions
print '\n\nPrinting questions...\n\n'
time.sleep(2)
questions = browser.find_by_xpath("//*[contains(@class, 'title may-blank ')]")
for question in questions:
    print question.text


# Example Output #2 - Print authors
print '\n\nPrinting authors...\n\n'
time.sleep(2)
authors = browser.find_by_xpath("//*[contains(@class, 'author may-blank')]")
for author in authors:
    print author.text


#END