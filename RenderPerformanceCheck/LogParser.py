'''
Created on Oct 1, 2014

@author: tony
'''
import re

class Parser:

    def parserQuality(self,logString):
        #logString = 'Render Options={"width":960,"height":540,"quality":"mid","template":"default","hdri":"urban","camera":"firstperson","type":"image","format":"png"}'
        p = re.findall(r'"quality":"([^"]+)"', logString)
        
        #print p[0]
        #using search:  print p.group(0)
        return p[0]
    
    def parserRenderingTime(self,logString):
        #logString = '||    RENDERING TIME: 0h 7m 34s'
        p = re.findall(r'RENDERING TIME: ([\w, ]+)', logString)
        
        #print p[0]
        return p[0]
    
    def parserJobID(self,logString):
        #logString = '||    FINISH RENDERING: c8beb831-7975-4db7-90c4-8c225e8fe2f3'
        p = re.findall('FINISH RENDERING: ([\S]+)', logString)
        
        #print p[0]
        return p[0]
        
    def parserLogDate(self,logString):
        #logString = 'Start Log: 9/28/2014 10:41:55 AM'
        p = re.findall('Start Log: ([^ ]+)', logString)
        
        #print p[0]
        return p[0]
    
    def parserContentLoadingTime(self,logString):
        #logString = '||    CONTENT LOADING TIME  : 0h 0m 16s'
        p = re.findall('CONTENT LOADING TIME  : ([\w, ]+)', logString)
        
        #print p[0]
        return p[0]
    
    def parserContentCount(self,logString):
        #logString = '||    CONTENT LOADING COUNT : 53'
        p = re.findall('CONTENT LOADING COUNT : ([\d]+)', logString)
        
        #print p[0]
        return p[0]
       
if __name__ == '__main__':
    '''
    a = Parser();
    a.parserQuality('ss')
    a.parserRenderingTime('ss')
    a.parserJobID('ss')
    a.parserLogDate('ss')
    a.parserContentLoadingTime('ss')
    a.parserContentCount('ss')
    '''
    pass