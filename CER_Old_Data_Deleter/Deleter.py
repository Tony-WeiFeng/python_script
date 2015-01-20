'''
Created on Dec 9, 2013

@author: fengw
'''
import os
import re


class Deleter():
        
    def deleter( self, tPath ):
        fList = os.walk( tPath )
        pattern_1 = re.compile( r'.zip$' )
        pattern_2 = re.compile( r'.dump$' )
        totalSize = 0
        totalSize_GB = 0
        for root, subdirs, files in fList:
            files.extend( subdirs )
            files.sort()

            for file in files:
                match_1 = pattern_1.search( file )
                match_2 = pattern_2.search( file )
                if ( match_1 or match_2 ):
                    #print file
                    fullName = os.path.join( root, file ) 
                    fileSize = os.path.getsize( fullName )
                    totalSize = totalSize + fileSize
                    #fullName = os.path.realpath( file )
                    
                    os.remove( fullName )
                    print fullName, " has been removed!"
            #print f
        totalSize_GB = totalSize / 1024 / 1024 / 1024
        return totalSize_GB

#P = 'C:\\A\\5-2008'
#Deleter().deleter( P )
