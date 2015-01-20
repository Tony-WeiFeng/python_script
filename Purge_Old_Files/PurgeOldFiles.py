import os
import time
import string
import deleter

d = deleter.Deleter()
path = r'O:'
fileList = os.walk( path )
count = 0
for root, subdirs, files in fileList:
    files.extend( subdirs )
    files.sort()
    
    for file in files:
        
        fullName = os.path.join( root, file )
        
        if os.path.isfile( fullName ):
    
            createTime = os.path.getctime( fullName )
            year = time.strftime('%Y',time.localtime(createTime))
            
            if  string.atoi(year) <= 2012 :
                d.fileDeleter( fullName )
                count = count + 1

print "There are ", count , " files have been removed!"
            
