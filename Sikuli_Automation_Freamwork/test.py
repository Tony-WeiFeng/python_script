# File name: test.py

import os
import time

# Create a testResult.html file to store the test result.
resultFilePath = os.getcwd() + '\\TestResult\\'
resultFileName = 'result_' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) +'.html'
fname =  resultFilePath + resultFileName
fobj = open(fname, 'w')

resultTemplate = '<font color="red">Hi,</font><br><br>\n\
<b>This is a test email, please ingore. :)</b><br><br>\n\
<table border="1">\n\
<tr>\n\
<th><b>TestCaseNO.</b></th>\n\
<th><b>TestResult</b></th>\n\
<th><b>TestExecuteTime</b></th>\n\
<th><b>Comments</b></th>\n\
</tr>\n\
</table><br><br>\n\
<i>Thanks,</i><br>\n\
<i>Tony</i>'

fobj.write(resultTemplate)
fobj.close()

#Traversal all files and subfolders in currect path, get the sikuli scripts.
currectPath = os.getcwd()
file_list = os.listdir(currectPath)
strSikuli = ".sikuli"
for testcase in file_list:
    # Check the folder is for sikuli script or not, if yes then run the sikuli script.
	if testcase.find(strSikuli) > 0 :
		command = "java -Dpython.path=Lib/ -jar C:\\Users\\Administrator\\Desktop\\Sikuli_command_test\\sikuli-script.jar C:\\Users\\Administrator\\Desktop\\Automation_Freamwork\\"
		command = command + testcase
		os.system(command)
	else:
             continue
print("end")
