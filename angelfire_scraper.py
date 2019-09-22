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
        col0_span = 0
        col1_span = 0
        col2_span = 0
        col3_span = 0
        col4_span = 0
        col5_span = 0
        col0_value = ''
        col1_value = ''
        col2_value = ''
        col3_value = ''
        col4_value = ''
        col5_value = ''

        for tr in tr_list:
          td = tr.findAll('td')
          write_string = ""
          col_counter = 0

          while col_counter <= 6:
            if col0_span != 0 and col_counter == 0:
              write_string += col0_value.replace(',','')
              col0_span -= 1
              td.insert(col_counter, 0)
            elif col1_span != 0 and col_counter == 1:
              write_string += col1_value.replace(',','')
              col1_span -= 1
              td.insert(col_counter, 0)
            elif col2_span != 0 and col_counter == 2:
              write_string += col2_value.replace(',','')
              col2_span -= 1
              td.insert(col_counter, 0)
            elif col3_span != 0 and col_counter == 3:
              write_string += col3_value.replace(',','')
              col3_span -= 1
              td.insert(col_counter, 0)
            elif col4_span != 0 and col_counter == 4:
              write_string += col4_value.replace(',','')
              col4_span -= 1
              td.insert(col_counter, 0)
            elif col5_span != 0 and col_counter == 5:
              write_string += col5_value.replace(',','')
              col5_span -= 1
              td.insert(col_counter, 0)
            else:
              try:
                cell = td[col_counter]
                write_string += cell.string.replace(',','')

                if cell.get('rowspan') is not None:
                  if col_counter == 0:
                    col0_span = int(cell.get('rowspan'))-1
                    col0_value = cell.string
                  elif col_counter == 1:
                    col1_span = int(cell.get('rowspan'))-1
                    col1_value = cell.string
                  elif col_counter == 2:
                    col2_span = int(cell.get('rowspan'))-1
                    col2_value = cell.string
                  elif col_counter == 3:
                    col3_span = int(cell.get('rowspan'))-1
                    col3_value = cell.string
                  elif col_counter == 4:
                    col4_span = int(cell.get('rowspan'))-1
                    col4_value = cell.string
                  elif col_counter == 5:
                    col5_span = int(cell.get('rowspan'))-1
                    col5_value = cell.string
              except:
                pass

            write_string += ','
            col_counter += 1

          text_file = open("angelfire.csv", "a+")
          text_file.write(write_string[:-1] +  '\n')
          text_file.close()