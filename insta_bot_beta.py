# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:40:07 2020

@author: Arun Vinodia
"""



from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def insta_bot(username,password):
    browser=webdriver.Firefox(executable_path=r'D:\Assets\geckodriver.exe')
    browser.get('https://instagram.com')
    time.sleep(5)

    usernameId=browser.find_element_by_name('username')
    usernameId.send_keys(username)
    passwordId=browser.find_element_by_name('password')
    passwordId.send_keys(password)
    time.sleep(2)
    button_login=browser.find_element_by_xpath("//button[@type='submit']")
    button_login.click()
    time.sleep(4)
    button_notNow=browser.find_element_by_xpath("//button[@type='button']")
    button_notNow.click()
#WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
    ui.WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

username=input('Username: ')
password=input('Password: ')

insta_bot(username,password)             
                     
