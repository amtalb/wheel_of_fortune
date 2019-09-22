import csv

with open('angelfire.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        new_file = open("clean_angelfire.csv", "a+")
        row_str = ','.join(row[1:4])
        if len(row_str) > 3:
          new_file.write(row_str + '\n')
          new_file.close()