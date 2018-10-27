#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:16:34 2018

@author: kia
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

userName = "Enter username"
password = "Enter Password"

print("\033[1;32;40m ------------------------------------------")
print("\033[1;32;40m -             INSTAGRAM LIKER            -")
print("\033[1;32;40m -               version 1.0              -")
print("\033[1;32;40m -                                        -")
print("\033[1;32;40m -                                        -")
print("\033[1;32;40m -                                        -")
print("\033[1;32;40m -                Kia Hamedi              -")
print("\033[1;32;40m -          kia.arta9793@gmail.com        -")
print("\033[1;32;40m ------------------------------------------")
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver = webdriver.Chrome('/home/kia/Downloads/chromedriver')
driver.maximize_window()
driver.get(url)
time.sleep(2)
print("\033[1;32;40m-->Start")
driver.find_element_by_xpath("//input[@name='username']").send_keys(userName)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button').click()
time.sleep(8)
print("\033[1;32;40m-->Login")
driver.find_element_by_xpath('./html/body/div[2]/div/div/div/div[3]/button[1]').click()
time.sleep(1)
rand = random.randrange(2,10)
print("\033[1;32;40m-->"+str(rand)+" Post Selected")
for i in range(1,rand):
	likeElement = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[1]/div/article['+str(i)+']/div[2]/section[1]/span[1]/button')
	time.sleep(1)
	#driver.execute_script("return arguments[0].scrollIntoView(true);", likeElement)
	likeElement.click()
	time.sleep(2)
	print("\033[1;32;40m-->"+str(i)+" Post Liked")
	
print("\033[1;32;40m-->Finish")
time.sleep(2)
driver.close()


	
