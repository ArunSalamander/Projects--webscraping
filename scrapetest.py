# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:53:47 2020

@author: Ravi Vinodia
"""
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html.read(),features='lxml')
        title=bsObj.body.h1
    except AttributeError as e:
        return None
title=getTitle('http://pythonscraping.com/exercises/exercise1.html')
if title==None:
    print('title could not be found')
else:
    print(title)