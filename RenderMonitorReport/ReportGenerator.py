#!/usr/bin/python
'''
Created on Nov 5, 2014

@author: tony
'''
import datetime
import DBQuery

today = datetime.date.today()
    
def generateReportBody():    

    startDate = str(today - datetime.timedelta(days=7))
    endDate = str(today)
    
    queryString = """
    SELECT 
        CONCAT('<tr><td align="center">',
                render_date,
                # Rendering Quality and image size is fixed for now, so just comment this.
                #'</td><td align="center">',
                #width,
                #'*',
                #height,
                '</td><td align="center">',
                render_type,                
                '</td><td align="center">',
                total_number,
                '</td><td align="center">',
                success_number,
                '</td><td align="center">',
                failure_rate,
                '</td><td align="center">',
                max_total_time,
                '</td><td align="center">',
                avg_total_time,
                '</td><td align="center">',
                min_total_time,
                '</td><td align="center">',
                avg_render_time,
                '</td>')
    FROM
        (SELECT 
            result_Count.render_date AS render_date,
            result_Count.render_type AS render_type,
            result_Count.total_number AS total_number,
            result_Count.success_number AS success_number,
            result_Count.failure_rate AS failure_rate,
            ROUND(MAX(((rj.dispatchTime - rj.created) / 1000) + ji.renderTime),
                    0) AS max_total_time,
            ROUND(AVG(((rj.dispatchTime - rj.created) / 1000) + ji.renderTime),
                    0) AS avg_total_time,
            ROUND(MIN(((rj.dispatchTime - rj.created) / 1000) + ji.renderTime),
                    0) AS min_total_time,
            ROUND(AVG(ji.renderTime), 0) AS avg_render_time
        FROM
            jobinfo ji
                LEFT JOIN
            renderjob rj ON ji.jobid = rj.id
                LEFT JOIN
            (SELECT 
                total_jobs.render_request_date AS render_date,
                    total_jobs.rendering_type AS render_type,
                    total_jobs.total_job_number AS total_number,
                    success_jobs.success_job_number AS success_number,
                    CONCAT(ROUND(((total_jobs.total_job_number - success_jobs.success_job_number) / total_jobs.total_job_number * 100), 2), '%%') AS failure_rate
            FROM
                (SELECT 
                DATE(FROM_UNIXTIME(rj.created / 1000 + 28800)) AS render_request_date,
                    rj.type AS rendering_type,
                    COUNT(*) AS total_job_number
            FROM
                (SELECT 
                renderjob.*, b.type
            FROM
                renderjob
            LEFT JOIN (SELECT 
                CASE
                        WHEN renderopt LIKE '%%panorama%%' THEN 'panorama'
                        ELSE 'image'
                    END AS type,
                    id
            FROM
                jobcontent) AS b ON renderjob.contentId = b.id) AS rj
            LEFT JOIN jobinfo ji ON rj.id = ji.jobid
            WHERE
                (rj.created / 1000 + 28800) BETWEEN UNIX_TIMESTAMP('%s') AND UNIX_TIMESTAMP('%s')
            GROUP BY render_request_date , rendering_type) AS total_jobs
            LEFT JOIN (SELECT 
                DATE(FROM_UNIXTIME(rj.created / 1000 + 28800)) AS render_request_date,
                    rj.renderingType AS rendering_type,
                    COUNT(*) AS success_job_number
            FROM
                renderjob AS rj
            LEFT JOIN jobinfo ji ON rj.id = ji.jobid
            WHERE
                (rj.created / 1000 + 28800) BETWEEN UNIX_TIMESTAMP('%s') AND UNIX_TIMESTAMP('%s')
                    AND rj.imgS3Url IS NOT NULL
            GROUP BY render_request_date , rendering_type) AS success_jobs ON total_jobs.render_request_date = success_jobs.render_request_date
                AND total_jobs.rendering_type = success_jobs.rendering_type) AS result_Count ON result_Count.render_date = DATE(DATE_ADD(ji.endTime, INTERVAL 8 HOUR))
                AND result_Count.render_type = ji.resultType
        WHERE
            DATE(DATE_ADD(ji.endTime, INTERVAL 8 HOUR)) >= '%s'
                AND DATE(DATE_ADD(ji.endTime, INTERVAL 8 HOUR)) < '%s'
        GROUP BY render_date , render_type
        ORDER BY render_date DESC , render_type ASC ) AS result
    """%(startDate,endDate,startDate,endDate,startDate,endDate)
    
    queryResult = DBQuery.getRenderResult(queryString)
    
    tableConnectString = ""
    for row in queryResult:
        tableConnectString += row[0]
    
    tableString = '''
                <table border=\"1\">
                   <tr>
                    <th width=\"120\"> Render Date </th>
                    <!--
                    Rendering Quality and image size is fixed for now, so just comment this.
                    <th width=\"80\"> Image Size </th>
                    -->
                    <th width=\"80\"> Render Type </th>
                    <th width=\"80\"> Total Count </th>
                    <th width=\"80\"> Successful Count </th>
                    <th width=\"80\"> Failure Rate </th>
                    <th width=\"80\"> MAX Total Time </th>
                    <th width=\"80\"> AVG Total Time </th>
                    <th width=\"80\"> MIN Total Time </th>
                    <th width=\"100\"> AVG Render Time </th>
                   </tr>
                   %s
                </table><br>
                '''%(tableConnectString)
    message = '''
                Hi Team,<br><br>
                Here is the rendering performance monitor report for ezHome production in 7 days before <b><font color="green">%s.</font></b><br>
                Please see following table. <br><br>
                %s
                <small><font color="DodgerBlue">
                * The unit of time is second.<br>
                * Total time is the time from user submit a rendering request to user get the rendering completed picture.<br>
                Total time = queue time + Render time
                </font></small><br><br>
                Thanks,<br>
                Home QA Team
              '''%(str(today),tableString)
              
    return message

def generateReportTitle():
        #Building the subject for report email.
    title = "EZHome Rendering Performance Monitor Report: " + str(today)
    return title 

if __name__ == '__main__':
    pass