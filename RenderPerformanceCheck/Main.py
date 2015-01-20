'''
Created on Oct 2, 2014

@author: tony
'''
import GetContent
import LogFileProcess
import DataStore
import GetRenderLogFiles
#import Calculate

insertStringList = []

logLinks = GetRenderLogFiles.getRenderLinks()
for link in logLinks:
    
    lc = GetContent.LogContent()
    logFileLines = lc.getLogEntriesFromPage(link[0])
    p = LogFileProcess.Processer()
    insertString = p.processLogFile(logFileLines)
    insertStringList.append(insertString)
    renderDate = p.renderDate
    
#Generate the parameters for function DataStore.insertData()
DBName = "RenderPerformance.db"
createTableString = "CREATE TABLE IF NOT EXISTS RENDERING_INFO(ID INTEGER PRIMARY KEY,\
                                         JOB_ID VARCHAR(50) UNIQUE NOT NULL,\
                                         RENDER_DATE VARCHAR(32) NOT NULL,\
                                         QUALITY VARCHAR(10) NOT NULL,\
                                         RENDER_TIME INTEGER NOT NULL,\
                                         LOADING_TIME INTEGER NOT NULL,\
                                         CONTENT_COUNT INTEGER NOT NULL\
                                         );"

#Insert log file parser.                                                    
DataStore.insertData(DBName, createTableString, insertStringList)

#Calculate the average render time for each render quality in DB;
#Create a table for average render result. 
createTableString = "CREATE TABLE IF NOT EXISTS AVG_RENDER_RESULT(ID INTEGER PRIMARY KEY,\
                                         RENDER_DATE VARCHAR(32) NOT NULL,\
                                         QUALITY VARCHAR(10) NOT NULL,\
                                         TOTAL_RENDER_TIME INTEGER NOT NULL,\
                                         MAX_RENDER_TIME INTEGER NOT NULL,\
                                         AVG_RENDER_TIME INTEGER NOT NULL,\
                                         MIN_RENDER_TIME INTEGER NOT NULL,\
                                         TOTAL_LOADING_TIME INTEGER NOT NULL,\
                                         MAX_LOADING_TIME INTEGER NOT NULL,\
                                         AVG_LOADING_TIME INTEGER NOT NULL,\
                                         MIN_LOADING_TIME INTEGER NOT NULL,\
                                         CONTENT_COUNT INTEGER NOT NULL,\
                                         CONSTRAINT RDATE_QUALITY UNIQUE(RENDER_DATE,QUALITY)\
                                         );"
insertString = "INSERT INTO AVG_RENDER_RESULT (ID,\
                                               RENDER_DATE,\
                                               QUALITY,\
                                               TOTAL_RENDER_TIME,\
                                               MAX_RENDER_TIME,\
                                               AVG_RENDER_TIME,\
                                               MIN_RENDER_TIME,\
                                               TOTAL_LOADING_TIME,\
                                               MAX_LOADING_TIME,\
                                               AVG_LOADING_TIME,\
                                               MIN_LOADING_TIME,\
                                               CONTENT_COUNT\
                                               ) \
                SELECT NULL,\
                       RENDER_DATE,\
                       QUALITY,\
                       SUM(RENDER_TIME),\
                       MAX(RENDER_TIME),\
                       ROUND(AVG(RENDER_TIME),0),\
                       MIN(RENDER_TIME),\
                       SUM(LOADING_TIME),\
                       MAX(LOADING_TIME),\
                       ROUND(AVG(LOADING_TIME),0),\
                       MIN(LOADING_TIME),\
                       SUM(CONTENT_COUNT)\
                FROM RENDERING_INFO \
                   WHERE RENDER_DATE = DATE('" + renderDate + "') \
                GROUP BY RENDER_DATE,QUALITY;"
insertStringList = [insertString]

#Do the aggregation and insert the result in table AVG_RENDER_RESULT.
DataStore.insertData(DBName, createTableString, insertStringList)


'''
No need, we can get the final result from table AVG_RENDER_RESULT, so comments this piece of code.

#--------------------------------------------------------------------------------------#
#Aggregation: Change the average render result from longitudinal table to cross table.
#This aggregation is for result comparing and reporting.
#--------------------------------------------------------------------------------------#
#Longitudial Table:
#    1|2014-09-28|high|103|53
#    2|2014-09-28|low|105|75    
#    3|2014-09-28|mid|455|22
#Cross Table:
#    1|2014-09-28|103|455|105|55|75|22
#--------------------------------------------------------------------------------------#

#Create a new cross table for the average render result aggregation
createTableString = "CREATE TABLE IF NOT EXISTS AGG_AVG_RENDER(ID INTEGER PRIMARY KEY,\
                                         RENDER_DATE VARCHAR(32) UNIQUE NOT NULL,\
                                         RENDER_AVG_HIGH INTEGER NOT NULL,\
                                         RENDER_AVG_MID INTEGER NOT NULL,\
                                         RENDER_AVG_LOW INTEGER NOT NULL,\
                                         RENDER_MAX_HIGH INTEGER NOT NULL,\
                                         RENDER_MAX_MID INTEGER NOT NULL,\
                                         RENDER_MAX_LOW INTEGER NOT NULL,\
                                         RENDER_MIN_HIGH INTEGER NOT NULL,\
                                         RENDER_MIN_MID INTEGER NOT NULL,\
                                         RENDER_MIN_LOW INTEGER NOT NULL,\
                                         CONTENT_COUNT_HIGH INTEGER NOT NULL,\
                                         CONTENT_COUNT_MID INTEGER NOT NULL,\
                                         CONTENT_COUNT_LOW INTEGER NOT NULL\
                                         );"
#
insertString = "INSERT INTO AGG_AVG_RENDER (ID,\
                                            RENDER_DATE,\
                                            RENDER_MAX_HIGH,\
                                            RENDER_MAX_MID,\
                                            RENDER_MAX_LOW,\
                                            RENDER_AVG_HIGH,\
                                            RENDER_AVG_MID,\
                                            RENDER_AVG_LOW,\
                                            RENDER_MIN_HIGH,\
                                            RENDER_MIN_MID,\
                                            RENDER_MIN_LOW,\
                                            CONTENT_COUNT_HIGH,\
                                            CONTENT_COUNT_MID,\
                                            CONTENT_COUNT_LOW \
                                            ) \
                    SELECT NULL,\
                           RENDER_DATE,\
                           SUM(CASE QUALITY WHEN 'high' THEN AVG_RENDER_TIME ELSE 0 END) AS HIGH,\
                           SUM(CASE QUALITY WHEN 'mid' THEN AVG_RENDER_TIME ELSE 0 END) AS MID,\
                           SUM(CASE QUALITY WHEN 'low' THEN AVG_RENDER_TIME ELSE 0 END) AS LOW \
                    FROM AVG_RENDER_RESULT \
                        WHERE RENDER_DATE = DATE('" + renderDate + "') \
                    GROUP BY RENDER_DATE;"

insertStringList = [insertString]

DataStore.insertData(DBName, createTableString, insertStringList)
'''
print "Done"

'''
    #Log file parser results are stored in DB, so need not get the result to do the calculate.
    #The aggregation will be done on DB side.
    result = p.processLogFile(lc.getLogEntriesFromPage(jobID))
    
    if result['Render Quality'] == 'high':
        renderHighList.append(result)
    if result['Render Quality'] == 'mid':
        renderMidList.append(result)
    if result['Render Quality'] == 'low':
        renderLowList.append(result)
'''    
#print renderHighList
#print renderMidList
#print renderLowList

#renderResultList = [renderHighList,renderMidList,renderLowList]

'''
#Using the function calculateAverageRenderTime of Calculate class 
#to calculate the average render time for each render quality.
#The out put type will be String, like "1h 2m 3s"
cal = Calculate.Calculator()
highRenderAverageTime = cal.calculateAverageRenderTime(renderHighList)
minRenderAverageTime = cal.calculateAverageRenderTime(renderMidList)
lowRenderAverageTime = cal.calculateAverageRenderTime(renderLowList)

print highRenderAverageTime
print minRenderAverageTime
print lowRenderAverageTime
'''

#Using the function timeStringToSecondInt of Calculate class to convert render time from string to integer.
#This is for store rendering time to DB, and convenient for calculating average render time in DB.


if __name__ == '__main__':
    pass