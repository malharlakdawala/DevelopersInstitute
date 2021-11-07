# -*- coding: utf-8 -*-
"""
Zerodha kiteconnect automated authentication
"""

from kiteconnect import KiteConnect
from selenium import webdriver
import time
import os


cwd = os.chdir("D:\Developers Institute\DevelopersInstitute\Week7\Hackathon")

def autologin():
    token_path = "api_key.txt"
    key_secret = open(token_path,'r').read().split()
    kite = KiteConnect(api_key=key_secret[0])
    service = webdriver.chrome.service.Service('./chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options = options.to_capabilities()
    driver = webdriver.Remote(service.service_url, options)
    driver.get(kite.login_url())
    driver.implicitly_wait(10)
    username = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
    password = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
    username.send_keys(key_secret[2])
    password.send_keys(key_secret[3])
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
    pin = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input')
    pin.send_keys(key_secret[4])
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/button').click()
    time.sleep(15)
    request_token=driver.current_url.split('request_token=')[1][:32]
    with open('request_token.txt', 'w') as the_file:
        the_file.write(request_token)
    driver.quit()

autologin()

#generating and storing access token - valid till 6 am the next day
request_token = open("request_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
data = kite.generate_session(request_token, api_secret=key_secret[1])
with open('access_token.txt', 'w') as file:
        file.write(data["access_token"])

#https://127.0.0.1/?action=login&type=login&status=success&request_token=cgz6bV94L4QRjFEo6Pb0MFtzLYTq4o7c