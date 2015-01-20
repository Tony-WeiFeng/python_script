#!/usr/bin/python
'''
Created on Nov 5, 2014

@author: tony
'''
import MySQLdb

def getRenderResult(queryString):
    try:      
        # Create DB connection
        conn = MySQLdb.connect("DB_Server_Name","UserName","Password","DB_Name")
        # Create cursor
        cur = conn.cursor()
        # Execute query
        cur.execute(queryString)
        resultContent = cur.fetchall()
        return resultContent

    except:
        print "MySQL Error: DB execution failed!"

    conn.close()
    
if __name__ == '__main__':
    pass