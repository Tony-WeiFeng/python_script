'''
Created on Oct 2, 2014

@author: tony
'''
import GetContent
import LogFileProcess
from home.tony.database import DataStore
#import Calculate

JobIDList = ['c8beb831-7975-4db7-90c4-8c225e8fe2f3',
             '0a7292f7-5624-4622-81d1-79182cefa745',
             '2be25d9c-fd82-47f0-87d6-aea21b3213ed',
             '2f3cd4bd-39bf-4f23-8590-d4c0ab8f3459',
             '3aa215ef-e700-4377-b41f-a6ed2b0a0357',
             '3ab020bb-cfdc-4e38-85ca-850dfbb28974',
             '5eeef5c6-baeb-4952-aed8-e07daba379da',
             '6bcf0777-8011-4255-a13b-351618e398cc',
             '09be652c-fb75-4306-9fbf-f74590837fb8',
             '9d7122af-685c-4c68-a5fc-6bc8280d89b6',
             '9e6f0553-17f4-4576-bd70-6fb34f7dbb94',
             '82a01cee-a97e-41ae-9ad5-c6afaa7a721a',
             '168a23b1-b7ad-4ebb-8d51-a32937118c65',
             '863eabf2-4d32-4b26-91f4-cdcb7f60c791',
             '1154fc15-a5f7-4e75-8b84-7dc970a2f00e',
             '2104ddbb-b36b-427a-a112-53279033ff35',
             '8873e3a7-55c5-45b7-9623-a5a8e4fd85e6',
             '668021d7-adce-41c6-941f-16606ab7aadf',
             '2582669d-479c-43d6-adad-f8bbc5ae5ee1',
             '9769953b-bb4c-4b2c-aa37-9ffbaf40af7c',
             'bec8f7e4-7836-4d41-9301-5494000e02e5',
             'd1a34f9c-7f50-433d-919e-33cb3f4eb39b',
             'e9c22056-fdc5-44ce-ac63-3d2ebd8e6927',
             'ee384b16-5456-4669-a481-b8040e7389d9',
             'f19d9a29-2887-4838-9b1d-c1b150546251']
'''
renderHighList = []
renderMidList = []
renderLowList = []
'''
insertStringList = []
for jobID in JobIDList:
    
    lc = GetContent.LogContent()
    logFileLines = lc.getLogEntriesFromPage(jobID)
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