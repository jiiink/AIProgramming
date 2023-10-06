def main():
  '''
  Create a text file containing the 50 states in alphabetical order.
  '''
  fileName = 'AIP_05_Data Processing and File Access_data/States.txt'
  sortedFileName = 'AIP_05_Data Processing and File Access_data/StatesAlpha.txt'
  statesList = createListFromFile(fileName)
  print('statesList', statesList)
  createSortedFile(statesList, sortedFileName)
  sortedStatesList = createListFromFile(sortedFileName)
  print('sortedStatesList', sortedStatesList)

def createListFromFile(fileName):
  infile = open(fileName, 'r')
  desiredList = [line.rstrip() for line in infile]
  infile.close()
  return desiredList

def createSortedFile(listName, fileName):
  listName.sort()
  for i in range(len(listName)):
    listName[i] = listName[i] + "\n"
  outfile = open(fileName, 'w')
  outfile.writelines(listName)
  outfile.close()

main()