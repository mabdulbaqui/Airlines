import pandas as pd
from selenium import webdriver
from time import sleep
from joblib import dump
from  bs4 import  BeautifulSoup as bs

def func(df, filename):
    pagesrc = {}
    for src in df:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome('/usr/bin/chromedriver')  # ,chrome_options=chrome_options)
        driver.get('https://www.distance.to/' + src)
        pagesrc.update({src : driver.page_source})
        driver.close()
        sleep(15)
        dump(pagesrc, filename)
