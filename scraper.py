#!/usr/bin/env python3
#! python3

#Web scraper to scrap a quote website goodreads

import requests  , random , pprint , bs4
#from bs4 import BeautifulSoup


site = requests.get('https://www.brainyquote.com/topics/linux')
site.raise_for_status()
#For dumping error message if any occurs

siteTextSoup = bs4.BeautifulSoup(site.text , "html.parser")
#.text is a attribute here and psses the response to bs4.BeautifulSoup object.
#html.parser is a parser which parses the html document ,  alternatively use lxml parser

####################################################################################################################################
#scraper.py:14: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
#
#The code that caused this warning is on line 14 of the file scraper.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.
#################################################################################################################################3

quote = siteTextSoup.select('a[title="view quote"]')
#A list is formed for every searched value

quoteList = []

for i in range(0,10):
	quoteList.append(quote[i].getText())

j = random.randint(1,10)

print(quoteList[j])
