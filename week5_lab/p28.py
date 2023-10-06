fileName = 'AIP_05_Data Processing and File Access_data/UN.txt'
outputFileName = 'AIP_05_Data Processing and File Access_data/UNbyArea.txt'

from enum import Enum
class Column(Enum):
  COUNTRY = 0
  CONTINENT = 1
  POPULATION = 2
  AREA = 3

def main():
  '''
  Create a file containing all countries and areas, ordered by area.
  Display first five lines of the file.
  '''
  countries = placeRecordsIntoList(fileName)
  countries.sort(key=lambda country: country[3], reverse=True) # sort by area

  displayFiveLargestCountries(countries)
  createNewFile(countries)

def placeRecordsIntoList(fileName):

  infile = open(fileName, 'r')
  listOfRecords = [line.rstrip() for line in infile]
  infile.close()
  for i in range(len(listOfRecords)):
    listOfRecords[i] = listOfRecords[i].split(',')
    listOfRecords[i][Column.POPULATION.value] = eval(listOfRecords[i][Column.POPULATION.value]) # population
    listOfRecords[i][Column.AREA.value] = eval(listOfRecords[i][Column.AREA.value]) # area

  return listOfRecords

def displayFiveLargestCountries(countries, n=5):
  print("{0:20}{1:9}".format("Country", "Area (sq. mi.)"))
  for i in range(n):
    print("{0:20}{1:9,d}".format(countries[i][0], countries[i][3]))

def createNewFile(countries):
  '''
  Create file of countries and their areas.
  '''
  outfile = open(outputFileName, 'w')
  for country in countries:
    outfile.write(country[Column.COUNTRY.value] + ',' + str(country[Column.AREA.value])+ "\n")
  outfile.close()

main()