# TODO compare actual guessed letters with best letters
# TODO write functions to print categories and letters
# TODO comment


import pandas
import matplotlib.pyplot as plt
from collections import Counter

df = pandas.read_csv('./data/clean_angelfire.csv')

def category_occurrence():
  count_list = df['Category'].value_counts()
  series = pandas.Series(count_list)

  return series

def guessed_letter_occurrence():
  letters = df['Letters'].str.split(" ", n=3, expand=True)
  letters = letters.dropna()
  print(letters.stack().value_counts())


def print_barh_graph(keys,values,savename="image.png",bar_colors='black',label=None):
  # instantiate figure and axes
  # also set figure size
  fig, ax = plt.subplots(figsize=(8,6))

  # set the axis labels
  ax.set_xlabel('Occurrences', fontsize=15)
  ax.set_ylabel('Letter', fontsize=15)

  # plot the plot
  plt.barh(keys,values,color=bar_colors)

  # set the title
  plt.title(savename, fontsize=18)

  # hide the top and right spines
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)

  # set prettier bounds on y axis
  ax.set_ylim((-1, len(keys)))
  y_placeholder = list(range(0,len(keys)))
  ax.set_yticks(y_placeholder)
  ax.set_yticklabels(keys)
  ax.spines['left'].set_bounds(0, (len(keys)-1))

  # set prettier bounds on x axis
  ax.margins(0)

  # adjust placement of axes
  ax.spines['bottom'].set_position(('axes', 0.02))
  ax.spines['left'].set_position(('axes', -0.01))

  # display the label
  if label:
    plt.text(0.85, 1.02, 'Most Frequent\n' + label, transform=plt.gca().transAxes)

  # invert the axis so A is on top and Z is on the bottom
  plt.gca().invert_yaxis()

  plt.savefig('graphs/'+savename+".png")
  plt.close()

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

# prints a graph that is the sum of all letter occurrences in all puzzles
def print_overall_letter_occurrence():
  puzzles = df['Puzzle']
  alphabet = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'O', 'P', 'Q', 'U', 'V', 'W', 'X', 'Y', 'Z']
  count_list = []

  # set bar colors
  bar_colors = ['#483D8B']*26
  # vowels are light blue
  light_blue = '#00BFFF' 
  # color vowels differently
  vowels = ['A','E','I','O','U']
  for i,letter in enumerate(alphabet):
    if letter in vowels:
      bar_colors[i] = light_blue

  # get values for plotting (x-axis)
  for letter in alphabet:
    count_list.append(puzzles.str.count(letter).sum())

  print_barh_graph(alphabet, count_list, savename="Letters", bar_colors=bar_colors)

# prints a graph for each Category displaying the frequency of each
# letter in the puzzles in that Category
def print_letter_occurrence_per_puzzle():
  # subclass Counter class
  class my_counter(Counter):
    # add method to check if a char exists, then remove it
    def remove_counter_character(self, char):
      if char in self:
        self.pop(char)

  # loop through each category in the dataframe
  for category in df['Category'].unique():
    # create a counter that counts every letter in the alphabet
    counter = my_counter(A=0, B=0, C=0, D=0, F=0, G=0, H=0, I=0, J=0, K=0, M=0, O=0, P=0, Q=0, U=0, V=0, W=0, X=0, Y=0, Z=0)
    puzzles = df.loc[df['Category'] == category, 'Puzzle']
    # count the letter occurrences in each puzzle
    for row in puzzles:
      counter.update(row)

    # remove all punctuation and given letters
    counter.remove_counter_character('?')
    counter.remove_counter_character('&')
    counter.remove_counter_character('\'')
    counter.remove_counter_character('-')
    counter.remove_counter_character(' ')
    counter.remove_counter_character('R')
    counter.remove_counter_character('S')
    counter.remove_counter_character('T')
    counter.remove_counter_character('L')
    counter.remove_counter_character('N')
    counter.remove_counter_character('E')

    # put 3 most common consonants and most common vowel
    # into a label to display on the graph
    mfc = get_most_frequent_consonants(counter)
    mfv = get_most_frequent_vowel(counter)
    label = ' '.join([str(elem) for elem in mfc]) 
    label += ' '
    label += ' '.join([str(elem) for elem in mfv]) 

    # extract keys and values from Counter object
    count_list = list(counter.items())
    count_list = [list(i) for i in count_list]
    count_list.sort()
    keys = [i[0] for i in count_list]
    values = [i[1] for i in count_list]

    # set bar colors
    bar_colors = ['#483D8B'] * 26
    # vowels are light blue
    light_blue = '#00BFFF' 
    # most common letters are red
    red = '#FF4C4C'
    # given letters are faded
    fade = '30'
    # lists
    vowels = ['A','E','I','O','U'] 
    for i,letter in enumerate(keys):
      if letter in vowels:
        bar_colors[i] = light_blue
      if letter in mfc or letter in mfv:
        bar_colors[i] = red
    
    print_barh_graph(keys,values,savename=category,bar_colors=bar_colors,label=label)

print_overall_letter_occurrence()
#print_category_occurrence()
print_letter_occurrence_per_puzzle()
#category_occurrence()
