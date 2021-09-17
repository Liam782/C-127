from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(executable_path=r"./chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

headers = ["name", "distance", "mass", "radius", "luminosity"]
star_data_list = []

def scrape():
    soup = BeautifulSoup(browser.page.text, "html.parser")
    temp_list = []

    sTable = soup.find('table')
    tRows = sTable.find_all('tr')
    for tr in tRows:
        td = tr.find_all('td')
        for i in td:
            temp_list.append(i)

    '''for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")'''

    star_data_list.append(temp_list)