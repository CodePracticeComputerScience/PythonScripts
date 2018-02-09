
#current directory
#import os
#print(os.getcwd())

#we load the Iris Plants Database from an ARFF file

from scipy.io.arff import loadarff
with open("E:/workspace/MS/PythonScripts/ProgLang/data/iris.arff", "r") as f:
    data, meta = loadarff(f)


