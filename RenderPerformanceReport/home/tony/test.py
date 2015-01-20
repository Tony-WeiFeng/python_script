'''
Created on Oct 4, 2014

@author: tony
'''
import sqlite3

#Create a table with DATE type and DATETIME type
'''
testString = "CREATE TABLE IF NOT EXISTS TEST(ID INTEGER PRIMARY KEY,\
                                         DATE DATE NOT NULL,\
                                         DATE_TIME DATETIME NOT NULL\
                                         );"

testString = "INSERT INTO TEST (ID,DATE,DATE_TIME)\
                SELECT NULL,RENDER_DATE,QUALITY from RENDERING_INFO"
'''
testString = "SELECT RENDER_DATE,HIGH,MID,LOW FROM AGG_AVG_RENDER WHERE RENDER_DATE >= DATE('2014-09-28','-7 day');"
try:
    # Connect Database. It will be created if it's not existed.
    DBConnection = sqlite3.connect("/home/tony/SqliteDB/RenderPerformance.db")

except sqlite3.Error,e:
    print "Failed to connect sqlite3 database!", "\n", e.args[0]
    #return

DBConnection.commit()

# Create a cursor for Database operation
cur = DBConnection.cursor()


try:
    cur.execute(testString)
    aa = cur.fetchall()
    print aa
except sqlite3.Error,e:
    print "Failed to query data from table!", "\n", e.args[0]
    #return
DBConnection.commit()
DBConnection.close()
    
    
if __name__ == '__main__':
    pass