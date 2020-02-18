# TODO analyze based on category, note weird categories in README
# TODO compare actual guessed letters with best letters
# TODO write about best 3 consonants/1 vowel to guess in README
# TODO make graphs prettier
# TODO write functions to print categories and letters
# TODO organize code
# TODO comment


import pandas
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

def print_barh_graph(keys,values,savename="image.png",most_frequent_l=[]):
  plt.clf()
  light_blue = [0,0,1,0.15]
  bar_colors = ['blue']*20
  bar_colors[0] = light_blue
  bar_colors[7] = light_blue
  bar_colors[11] = light_blue
  bar_colors[14] = light_blue

  plt.barh(keys,values,color=bar_colors)

  if len(most_frequent_l)>0: 
    plt.text(0.75, 1.02, 'Most Frequent\n' + str(most_frequent_l), transform=plt.gca().transAxes)

  plt.gca().invert_yaxis()
  plt.savefig('graphs/'+savename)
  
def print_overall_letter_occurence():
  series = puzzle_letter_occurence()

def get_most_frequent_consonants(counter):
  consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
  most_frequent_l = Counter(counter).most_common(10)
  top_3_consonants = []
  counter = 0
  
  for letter in most_frequent_l:
    if counter > 2:
      break
    if letter[0] in consonants:
      top_3_consonants.append(letter[0])
      counter += 1

  return top_3_consonants

def get_most_frequent_vowel(counter):
  vowels = ['A','E','I','O','U']
  most_frequent_l = Counter(counter).most_common(10)
  top_vowel = []

  for letter in most_frequent_l:
    if letter[0] in vowels:
      top_vowel.append(letter[0])
      break
  
  return top_vowel

def print_letter_occurence_per_puzzle():
  def remove_counter_character(char):
    if char in counter:
      counter.pop(char)

  for category in df['Category'].unique():
    counter = Counter(A=0, B=0, C=0, D=0, F=0, G=0, H=0, I=0, J=0, K=0, M=0, O=0, P=0, Q=0, U=0, V=0, W=0, X=0, Y=0, Z=0)
    puzzles = df.loc[df['Category'] == category, 'Puzzle']
    for row in puzzles:
      counter.update(row)

    remove_counter_character('?')
    remove_counter_character('&')
    remove_counter_character('\'')
    remove_counter_character('-')
    remove_counter_character(' ')
    remove_counter_character('R')
    remove_counter_character('S')
    remove_counter_character('T')
    remove_counter_character('L')
    remove_counter_character('N')
    remove_counter_character('E')

    most_frequent_l = []
    most_frequent_l += get_most_frequent_consonants(counter)
    most_frequent_l += get_most_frequent_vowel(counter)

    count_list = list(counter.items())
    count_list = [list(i) for i in count_list]
    count_list.sort()
    keys = [i[0] for i in count_list]
    values = [i[1] for i in count_list]
    print_barh_graph(keys,values,savename=category+".png",most_frequent_l=most_frequent_l)

#print_overall_letter_occurence()
print_letter_occurence_per_puzzle()
