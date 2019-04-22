import pickle

#Dump data in pickle files of S.I.R.
#Created by GreenGames

#Place name of file in between quote marks
FILE="password.pkl"
#Place Tempory Code Here

#Dumping
with open(FILE,'wb') as fileObject:
    pickle.dump('mvqelk',fileObject,pickle.HIGHEST_PROTOCOL)
    fileObject.close()

#Loading to Check
with open(FILE,'rb') as fileObject:
    print(pickle.load(fileObject))
