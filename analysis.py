import pandas
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

df = pandas.read_csv('./data/clean_angelfire.csv')

def category_occurence():
  count_list = df['Category'].value_counts()
  series = pandas.Series(count_list)

  return series

def guessed_letter_occurence():
  letters = df['Letters'].str.split(" ", n=3, expand=True)
  letters = letters.dropna()
  print(letters.stack().value_counts())

def puzzle_letter_occurence():
  puzzles = df['Puzzle']
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  count_list = []

  for letter in alphabet:
    count_list.append(puzzles.str.count(letter).sum())

  series = pandas.Series(count_list, index=alphabet)
  return series

def print_barh_graph(series,savename="image.png"):
  series.plot.barh()
  plt.gca().invert_yaxis()
  plt.savefig(savename)

def print_letter_occurence_per_puzzle():
  for category in df['Category'].unique():
    counter = Counter()
    puzzles = df.loc[df['Category'] == category, 'Puzzle']
    for row in puzzles:
      counter.update(row)
    count_list = list(counter.items())
    count_list.sort()
    if count_list[0][0] == " ":
      del count_list[0]
    series = pandas.Series((int(i[1]) for i in count_list), index=(i[0] for i in count_list))
    series = series.rename(category)
    print_barh_graph(series,savename=series.name+".png")

print_letter_occurence_per_puzzle()
