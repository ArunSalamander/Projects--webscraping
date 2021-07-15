# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:37:22 2020

@author: Arun Vinodia
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html=urlopen('http://en.wikipedia.org/wiki/kevin_Bacon')
bsObj=BeautifulSoup(html,features='lxml')
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])