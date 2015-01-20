'''
Created on Oct 2, 2014

@author: tony
'''

import LogParser
import Calculate

class Processer:
    renderDate = ""
    #renderContentCount = ""
    def processLogFile(self,logContent):
        
        pa = LogParser.Parser()
        renderDate = ""
        renderQuality = ""
        renderTime = ""
        renderJobID = ""
        renderContentLoadingTime = ""
        renderContentCount = ""
        
        for line in logContent:
            if line.startswith("Start Log:"):
                renderDate = pa.parserLogDate(line)
            if line.startswith("Render Options="):
                renderQuality = pa.parserQuality(line)
            if line.startswith("||\tRENDERING TIME:"):
                renderTime = pa.parserRenderingTime(line)
            if line.startswith("||\tFINISH RENDERING:"):
                renderJobID = pa.parserJobID(line)
            if line.startswith("||\tCONTENT LOADING TIME  :"):
                renderContentLoadingTime = pa.parserContentLoadingTime(line)
            if line.startswith("||\tCONTENT LOADING COUNT :"):
                renderContentCount = pa.parserContentCount(line)
                
        '''  
        #Store the result in a dictionary parserResult and return it.
        parserResult = {"Job ID":renderJobID,"Render Date":renderDate,"Render Quality":renderQuality,"Render Time":renderTime}
        return parserResult
        '''
        
        #Insert the log file parser result into DB
        
        #Convert the renderTime from '0h 1m 2s' to seconds with string type, this if for create the insert string. 
        cal = Calculate.Calculator()
        renderTime = str(cal.timeStringToSecondInt(renderTime))
        renderContentLoadingTime = str(cal.timeStringToSecondInt(renderContentLoadingTime))
        
        # Convert the renderDate format from "9/28/2014" to "2014-09-28"
        d = renderDate.split("/")
        mo = int(d[0])
        da = int(d[1])
        ye = d[2]
        
        if mo < 10:
            mo = '0' + str(mo)
        if da < 10:
            da = '0' + str(da)
        renderDate = ye + "-" + str(mo) + "-" + str(da)
        Processer.renderDate = renderDate
        
        Processer.renderContentCount = renderContentCount;
        #Generate insert string
        insertDataString = "INSERT INTO  RENDERING_INFO VALUES(NULL," +\
                                                       "'" + renderJobID + "', " +\
                                                       "date('" + renderDate + "')," +\
                                                       "'" + renderQuality + "', " +\
                                                       renderTime + ", " +\
                                                       renderContentLoadingTime + ", " +\
                                                       renderContentCount +\
                                                       ");"
        return insertDataString
        
#    def storeResultToDB(self,DBName,createTableString,insertDataString):

if __name__ == '__main__':
    pass