import pandas
import seaborn as sns
import matplotlib.pyplot as plt

df = pandas.read_csv('data/clean_angelfire.csv')

def category_occurence():
  print(df['Category'].value_counts())

def guessed_letter_occurence():
  letters = df['Letters'].str.split(" ", n=3, expand=True)
  letters = letters.dropna()
  print(letters.stack().value_counts())

def puzzle_letter_occurence():  
  puzzles = df['Puzzle']
  print("A occurences: ", end='')
  print(puzzles.str.count('A').sum())
  print("B occurences: ", end='')
  print(puzzles.str.count('B').sum())
  print("C occurences: ", end='')
  print(puzzles.str.count('C').sum())
  print("D occurences: ", end='')
  print(puzzles.str.count('D').sum())
  print("E occurences: ", end='')
  print(puzzles.str.count('E').sum())
  print("F occurences: ", end='')
  print(puzzles.str.count('F').sum())
  print("G occurences: ", end='')
  print(puzzles.str.count('G').sum())
  print("H occurences: ", end='')
  print(puzzles.str.count('H').sum())
  print("I occurences: ", end='')
  print(puzzles.str.count('I').sum())
  print("J occurences: ", end='')
  print(puzzles.str.count('J').sum())
  print("K occurences: ", end='')
  print(puzzles.str.count('K').sum())
  print("L occurences: ", end='')
  print(puzzles.str.count('L').sum())
  print("M occurences: ", end='')
  print(puzzles.str.count('M').sum())
  print("N occurences: ", end='')
  print(puzzles.str.count('N').sum())
  print("O occurences: ", end='')
  print(puzzles.str.count('O').sum())
  print("P occurences: ", end='')
  print(puzzles.str.count('P').sum())
  print("Q occurences: ", end='')
  print(puzzles.str.count('Q').sum())
  print("R occurences: ", end='')
  print(puzzles.str.count('R').sum())
  print("S occurences: ", end='')
  print(puzzles.str.count('S').sum())
  print("T occurences: ", end='')
  print(puzzles.str.count('T').sum())
  print("U occurences: ", end='')
  print(puzzles.str.count('U').sum())
  print("V occurences: ", end='')
  print(puzzles.str.count('V').sum())
  print("W occurences: ", end='')
  print(puzzles.str.count('W').sum())
  print("X occurences: ", end='')
  print(puzzles.str.count('X').sum())
  print("Y occurences: ", end='')
  print(puzzles.str.count('Y').sum())
  print("Z occurences: ", end='')
  print(puzzles.str.count('Z').sum())

# set the background colour of the plot to white
sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
sns.set(rc={'figure.figsize':(11.7,8.27)})
# create a countplot
count_plot = sns.countplot(y='Category',data=df, order=df['Category'].value_counts().index)
# Remove the top and down margin
sns.despine(offset=10, trim=True)
# display the plotplt.show()

count_plot.figure.savefig("categories.png")
