# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:58:43 2020

@author: Arun Vinodia
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

file_links=open('link_kevinBacon.txt','w')
html=urlopen('http://en.wikipedia.org/wiki/kevin_Bacon')
bsObj=BeautifulSoup(html,features='lxml')
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        file_links.write(link.attrs['href'])
        file_links.write('\n')

file_links.close()
