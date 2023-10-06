def main():
  '''
  Display the names of the first three presidents.
  '''
  file = 'AIP_05_Data Processing and File Access_data/FirstPresidents.txt'
  displayWithForLoop(file)
  print()
  displayWithListComprehension(file)
  print()
  displayWithReadline(file)

def displayWithForLoop(file):
  infile = open(file, 'r')
  for line in infile:
    print(line.rstrip())
  infile.close()

def displayWithListComprehension(file):
  infile = open(file, 'r')
  listPres = [line.rstrip() for line in infile]
  infile.close()
  print(listPres)

def displayWithReadline(file):
  infile = open(file, 'r')
  line = infile.readline()
  while line != "":
    print(line.rstrip())
    line = infile.readline()
  infile.close()

main()