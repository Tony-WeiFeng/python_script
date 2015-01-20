'''
Created on Oct 6, 2014

@author: tony
'''
import datetime
import sqlite3

class ReportGenerator:
    
    title = ""
    messageString = ""
    
    def generateEmailConnect(self):
        #Get the today's date, and convert it to string.
        today = str(datetime.date.today())
        
        #Fetch the average render results in 10 days from AGG_AVG_RENDER table.
        DBName = "RenderPerformance.db"
        qualityList = ['high','mid','low']
        allTablesString = ""
        for quality in qualityList:
            SQLString = "SELECT '<tr><td align=\"center\">' || RENDER_DATE || '</td>\
                                     <td align=\"center\">' || TOTAL_RENDER_TIME || '</td>\
                                     <td align=\"center\">' || MAX_RENDER_TIME || '</td>\
                                     <td align=\"center\">' || AVG_RENDER_TIME || '</td>\
                                     <td align=\"center\">' || MIN_RENDER_TIME || '</td>\
                                     <td align=\"center\">' || TOTAL_LOADING_TIME || '</td>\
                                     <td align=\"center\">' || MAX_LOADING_TIME || '</td>\
                                     <td align=\"center\">' || AVG_LOADING_TIME || '</td>\
                                     <td align=\"center\">' || MIN_LOADING_TIME || '</td>\
                                     <td align=\"center\">' || CONTENT_COUNT || '</tr>'\
                        FROM AVG_RENDER_RESULT\
                            WHERE QUALITY = '" + quality + "'\
                              AND RENDER_DATE >= DATE('" + today + "', '-15 day')\
                        ORDER BY RENDER_DATE DESC;"
            try:
                # Connect Database. It will be created if it's not existed.
                DBConnection = sqlite3.connect("/home/tony/SqliteDB/" + DBName)
            
            except sqlite3.Error,e:
                print "Failed to connect sqlite3 database!", "\n", e.args[0]
                #return
            DBConnection.commit()
            
            # Create a cursor for Database operation
            cur = DBConnection.cursor()
            
            try:
                cur.execute(SQLString)
                queryResult = cur.fetchall()
            
            except sqlite3.Error,e:
                print "Failed to query data from table!", "\n", e.args[0]
                #return
            DBConnection.commit()
            DBConnection.close()
            
            #Building the html string for report tables.
            
            tableConnectString = ""
            for row in queryResult:
                tableConnectString += row[0]
                
            #Building the table string for presenting average render time.
            #tableString = "<table border=\"1\" cellspacing=\"0px\" style=\"border-collapse:collapse\">\
            tableString = "<b><u><font size=\"12px\">Render Result for Quality </font></u><font color=\"red\">" + quality + "</font></b><br>\
                          <table border=\"1\">\
                           <tr>\
                            <th width=\"120\"> Render Date </th>\
                            <th width=\"80\"> Total Render Time </th>\
                            <th width=\"80\"> Maximum Render Time </th>\
                            <th width=\"80\"> Average Render Time </th>\
                            <th width=\"80\"> Minimum Render Time </th>\
                            <th width=\"80\"> Total Render Time </th>\
                            <th width=\"80\"> Maximum Render Time </th>\
                            <th width=\"80\"> Average Render Time </th>\
                            <th width=\"80\"> Minimum Render Time </th>\
                            <th width=\"80\"> Content Count </th>\
                           </tr>" \
                           + tableConnectString +\
                           "</table><br><br>"
                           
            allTablesString += tableString
                
        #Building the subject for report email.
        ReportGenerator.title = "Render Performance Report: " + today            
        #Building the message for report email.
        ReportGenerator.messageString = "Hi Team,<br><br>\
                         Here is the render performance report for each quality in 15 days before <b><font color=\"green\">" + today +"</font></b>. \
                         Please see following tables. <br><br>" + \
                         allTablesString + \
                         "Thanks,<br> \
                         Home QA Team."


if __name__ == '__main__':
    pass