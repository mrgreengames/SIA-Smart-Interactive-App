import pickle

#Dump data in pickle files of S.I.R.
#Created by GreenGames

#Place name of file in between quote marks
FILE="topics.pkl"
#Tempory Code
topics=["maths","ngm"]
#NGM=Number Guessing Game

#Dumping
with open(FILE,'wb') as fileObject:
    pickle.dump(topics,fileObject,pickle.HIGHEST_PROTOCOL)
    fileObject.close()

#Loading to Check
with open(FILE,'rb') as fileObject:
    print(pickle.load(fileObject))
