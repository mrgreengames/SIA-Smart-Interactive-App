import cPickle as pickle
import os.path

#Replace string with name of Pickle file i.e. file.pickle

_FILE_NAME_ = 'password.pickle'

if os.path.exists(_FILE_NAME_):
    with open(_FILE_NAME_, 'w') as file_object:
        # Replace string with data you want to dump into _FILE_NAME_
        pickle.dump("yay", file_object)
    
