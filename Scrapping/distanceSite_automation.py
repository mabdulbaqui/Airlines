import pandas as pd
from selenium import webdriver
from time import sleep
from joblib import dump


def func(df, filename):
    pagesrc = []
    for src in df['Route'].unique():
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome('/usr/bin/chromedriver')  # ,chrome_options=chrome_options)
        driver.get('https://www.distance.to/' + src)
        x = driver.page_source
        pagesrc.append(x)
        driver.close()
        sleep(15)
        dump(pagesrc, 'filename')
