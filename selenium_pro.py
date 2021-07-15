# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:22:47 2020

@author: Ravi Vinodia
"""

from selenium import webdriver
import time
browser=webdriver.Firefox(executable_path=r'D:\Assets\geckodriver.exe')
browser.get('https://instagram.com')
emailElem=browser.find_element_by_id('identifierId')
emailElem.send_keys('arunsalamander@gmail.com')
#passwordElem=browser.find_element_by_id('Passwd')
#passwordElem.send_keys('12345')
#passwordElem.submit()
browser.find_element_by_id('identiferNext').click()
time.sleep(1)
#try:
#    linkElem=browser.find_element_by_link_text('The beginning- Art formation')
#    linkElem.click()
#except:
#    print('not found')