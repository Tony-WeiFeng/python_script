'''
Created on Oct 1, 2014

@author: tony
'''
import urllib2


class LogContent:
    def getLogEntriesFromPage(self,j_id):
        #j_id = "0a7292f7-5624-4622-81d1-79182cefa745"
        url = "http://ec2-54-91-198-249.compute-1.amazonaws.com/get?jobid=" + j_id + "&file=render.log"
        #req = urllib2.Request(url)
        #resp = urllib2.urlopen(req)
        resp = urllib2.urlopen(url)
        allLines = resp.readlines()
        '''
        for line in allLines:
            print line
        '''
        return allLines
    
    def getLogEntriesFromFile(self,fileName):
        #fileName = "/home/tony/Desktop/RenderPerforanceReportRelated/1.log"
        try:
            fileContent = open(fileName,'r')
            allLines = fileContent.readlines()
        finally:
            fileContent.close()
        '''
        for line in allLines:
            print line
        '''
        return allLines
    
#if __name__ == '__main__':
    #a = GetContent()
    #a.getLogEntriesFromPage("0a7292f7-5624-4622-81d1-79182cefa745")
    #a.getLogEntriesFromFile("/home/tony/Desktop/RenderPerforanceReportRelated/1.log")