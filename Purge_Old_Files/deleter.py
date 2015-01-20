'''
Created on Mar 31, 2014

@author: tony
'''

import os

class Deleter():
    '''
    classdocs
    '''
    
    def fileDeleter(self,fileName):
        os.remove(fileName)
        print fileName + " has been removed!"
