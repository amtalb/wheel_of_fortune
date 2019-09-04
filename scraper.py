import requests
import urllib.request
import time
import csv
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://www.angelfire.com/mi4/malldirectories/wheel/wheelbonus.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")
for link in soup.findAll('a', href=True):
  if 'http://www.angelfire.com/mi4/malldirectories' in link.get('href'):
    year_url = link.get('href')
    year_response = requests.get(year_url)
    year_soup = BeautifulSoup(year_response.text, "html.parser")
    for month_link in year_soup.findAll('a', href=True):
      if 'http://www.angelfire.com/mi4/malldirectories' in month_link.get('href') and 'wheelbonus' not in month_link.get('href'):
        month_url = month_link.get('href')
        month_response = requests.get(month_url)
        month_soup = BeautifulSoup(month_response.text, "html.parser")
        tr_list = month_soup.findAll('tr', bgcolor="#663399")
        tr_list = tr_list[1:]
        for tr in tr_list:
          td = tr.findAll('td')
          if td[0].string is not None and td[1].string is not None and td[2].string is not None and td[3].string is not None:
            date = td[0].string
            category = td[1].string
            puzzle = td[2].string
            letters = td[3].string
            write_string = date + "," + category + "," + puzzle + "," + letters
            text_file = open("angelfire.csv", "a+")
            text_file.write(write_string +  '\n')
            text_file.close()
            print("written")
      time.sleep(1)