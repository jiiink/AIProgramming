import csv
from itertools import groupby
first = lambda x: x[0]
fileName = 'AIP_05_Data Processing and File Access_data/UN.txt'

def getContinentList():
  contents = list()
  with open(fileName, 'r') as f_read:
    reader = csv.reader(f_read)
    for row in reader:
      contents.append(row)

  return set(map(first, groupby(contents, lambda x: x[1])))

def main():
  '''
  Display the countries in a specified continent.
  '''
  continent = input(f"Enter the name of a continent: {*getContinentList(),} ")
  continent = continent.title() # Allow for all lower
  if continent != "Antarctica": # case letters. (남극대륙)
    infile = open(fileName, 'r')
    for line in infile:
      data = line.split(',')
      if data[1] == continent:
        print(data[0])
    infile.close()
  else:
    print("There are no countries in Antarctica.")

main()