'''
Created on Oct 23, 2014

@author: tony
'''
import MySQLdb

def getRenderLinks():
        
    # Create DB connection
    conn = MySQLdb.connect("ec2-54-224-105-1.compute-1.amazonaws.com","developer","Dr@g0n^Fli","jobmanager")
    # Create cursor
    cur = conn.cursor()
    # Execute query
    
    
    queryString = "select concat( 'http://', replace(bindToInstanceId,'WIN-6NUR99I6N25__','') , '/get?jobid=' , id , '&file=render.log') as loglink \
    from renderjob \
    where designId like \"TonyTest%\" and id > 2730324 and processStatus = 2 and bindToInstanceId = \"WIN-6NUR99I6N25__ec2-54-83-58-127.compute-1.amazonaws.com\";"
    
    cur.execute(queryString)
    loglinks = cur.fetchall()

    return loglinks


if __name__ == '__main__':
    pass