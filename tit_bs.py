# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 08:50:27 2020

@author: Arun Vinodia
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs

def get_title(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=bs(html.read(),features='lxml')
        title=bsObj.body.h4
    except AttributeError as e:
        return None
    return title
title=get_title('http://versalgo.com')

if title is None:
    print('Tag not found')
else:
    print(title)
        