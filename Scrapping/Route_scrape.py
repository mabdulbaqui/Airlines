from bs4 import BeautifulSoup as bs
import requests
from joblib import dump
import os


def func(soup,Rou):
     
    link = 'https://www.greatcirclemapper.net/' + soup.find('a', class_='next')['href']  # NEXT
    return link, routs




    # 
    # soup = bs(requests.get('https://www.greatcirclemapper.net/en/routes.html').text)
    # cats = soup.find('table', class_='list').find('tr')
    # features = [i.text for i in cats.find_all('th')]
    # features.insert(3, 'DistanceKm')
    # features[2] = 'DistanceNm'
    # Routs = []
    # while (True):
    #     try:
    #         link, routs = func(soup)
    #         soup = bs(requests.get(link).text)
    #         print(link)
    #     except:
    #         break
    # 
    # dump(Routs, 'Routs.h5')
