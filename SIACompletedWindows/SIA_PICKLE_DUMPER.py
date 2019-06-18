import pickle

#Dump data in pickle files of S.I.A.
#Created by GreenGames

#Place name of file in between quote marks
FILE=".pkl"
#Place Tempory Code Here

#Dumping
with open(FILE,'wb') as fileObject:
    pickle.dump('',fileObject,pickle.HIGHEST_PROTOCOL)
    fileObject.close()

#Loading to Check
with open(FILE,'rb') as fileObject:
    print("Testing to see if it has been dumped")
    print(pickle.load(fileObject))
