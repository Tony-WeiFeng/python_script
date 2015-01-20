'''
Created on Oct 2, 2014

@author: tony
'''
import re


class Calculator:
    
    def calculateAverageRenderTime(self,parserResultList):
        #parserResultList = [{'Render Time': '0h 7m 34s', 'Job ID': 'c8beb831-7975-4db7-90c4-8c225e8fe2f3', 'Render Quality': 'mid', 'Render Date': '9/28/2014'}, {'Render Time': '0h 7m 34s', 'Job ID': '0a7292f7-5624-4622-81d1-79182cefa745', 'Render Quality': 'mid', 'Render Date': '9/28/2014'}]

        if len(parserResultList) != 0:
            totalTimeSecond = 0
            count = 0
            for result in parserResultList:
                totalTimeSecond += self.timeStringToSecondInt(result['Render Time'])
                count += 1
            averageTimeSecond = totalTimeSecond//count
            averageTimeString = self.timeSecondIntToString(averageTimeSecond)
            
            return averageTimeString
        else:
            return "No Data"
        
    def timeStringToSecondInt(self,s):
        time = re.findall('[\d]+', s)
        hour = int(time[0])
        minute = int(time[1])
        second = int(time[2])
        
        timeSecond = hour*60*60 + minute*60 + second
        
        return timeSecond
    
    def timeSecondIntToString(self,timeSecond):
        second = timeSecond%60
        timeSecond = timeSecond//60
        minute = timeSecond%60
        hour = timeSecond//60
        
        timeString = str(hour) + 'h ' + str(minute) + 'm ' + str(second) + 's'
        return timeString
        
if __name__ == '__main__':
    pass
    #c = Calculator();
    #c.calculateAverageRenderTime(['1','2'])