'''
Created on Oct 3, 2014

@author: tony
'''
import sqlite3

#This function createDB will be included in the function createTable and insertData
def createDB(sqliteDBName):

    # Sqlite Database name
    #DBName = "RenderPerformance.db"
    '''
    Description: Create a DB to store render result.
    '''
    
    try:
        # Connect Database. It will be created if it's not existed.
        DBConnection = sqlite3.connect("/Users/tony/SqliteDB/" + sqliteDBName)
        DBConnection.commit()
    
    except sqlite3.Error,e:
        print "Failed to connect sqlite3 database!", "\n", e.args[0]
        return
    
    DBConnection.close();

#This function createTable will be included in the function insertData
def createTable(DBName,tableCreateString):
    # Create DB Connection
    DBConnection = createDB(DBName)
    
    # Create a cursor for Database operation
    cur = DBConnection.cursor()
    """
    # Create table RENDERING_INFO for store the rendering information for each logs.
    tableCreateString = '''CREATE TABLE IF NOT EXISTS RENDERING_INFO(ID INTEGER PRIMARY KEY, 
                                                 JOB_ID VARCHAR(50),
                                                 RENDER_DATE VARCHAR(32),
                                                 QUALITY VARCHAR(10),
                                                 RENDER_TIME INTEGER
                                                 );'''
    """
    try:
        cur.execute(tableCreateString)
        # For sqlite3 DB, after every execution, need call the function of the connection.  
        DBConnection.commit()
    except sqlite3.Error,e:
        print "Failed to create table!", "\n", e.args[0]
        return

    DBConnection.close()

#This function createDB will be included in the function createTable and insertData
#Changed the third parameter from instertString to insertStingList, so the type input parameter must be a List.
#This change is for create a transaction for each insert execution, 
#so using list we can include all insert execution in on transaction to reduce DB operation.
def insertData(DBName,tableCreateString,insertStringList):
    # Create DB Connection
    try:
        # Connect Database. It will be created if it's not existed.
        DBConnection = sqlite3.connect("/Users/tony/SqliteDB/" + DBName)
    
    except sqlite3.Error,e:
        print "Failed to connect sqlite3 database!", "\n", e.args[0]
        return
    DBConnection.commit()
    
    # Create a cursor for Database operation
    cur = DBConnection.cursor()
    
    # Create table if it's not exist.
    try:
        cur.execute(tableCreateString)
        DBConnection.commit()
    except sqlite3.Error,e:
        print "Failed to create table!", "\n", e.args[0]
        return
    
    # Insert data into the table
    for insertString in insertStringList:
        try:
            cur.execute(insertString)
        except sqlite3.Error,e:
            print "Failed to insert data to table!", "\n", e.args[0]
            return
    DBConnection.commit()
    DBConnection.close()

def executeSQL(DBName,SQLString):
        # Create DB Connection
    try:
        # Connect Database. It will be created if it's not existed.
        DBConnection = sqlite3.connect("/Users/tony/SqliteDB/" + DBName)
    
    except sqlite3.Error,e:
        print "Failed to connect sqlite3 database!", "\n", e.args[0]
        return
    DBConnection.commit()
    
    # Create a cursor for Database operation
    cur = DBConnection.cursor()
    
    # Create table if it's not exist.
    try:
        cur.execute(SQLString)
        DBConnection.commit()
    except sqlite3.Error,e:
        print "Failed to execute the SQL:" + SQLString, "\n", e.args[0]
        return
    
    DBConnection.close()

if __name__ == '__main__':
    pass