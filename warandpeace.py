# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:54:25 2020

@author: Arun Vinodia
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj=BeautifulSoup(html,features='lxml')
nameList=bsObj.findAll('span',{'class':'green'})
for name in nameList:
    print(name.get_text())