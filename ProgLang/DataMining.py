import pprint as p
#open file to read
myfile = open('Stocks_DataMining.txt','r')

#read the data from file into a list
#listOfLines = myfile.read().splitlines()

p.pprint(myfile.read())