import requests
import urllib.request
import time
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
          write_string = ""
          for cell in td:
            if cell.string is not None:
              write_string += cell.string.replace(',','')+','
          text_file = open("angelfire.csv", "a+")
          text_file.write(write_string[:-1] +  '\n')
          text_file.close()
          print("written")