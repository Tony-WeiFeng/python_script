import os

def addTestResult(testCaseName,testResult,testExecuteTime,Comments):
    caseName = testCaseName
    result = testResult
    excuteTime = testExecuteTime
    comment = Comments
    
    resultFilePath = os.getcwd()
    # Get parent path
    resultFilePath = os.path.dirname(resultFilePath)

    resultFilePath = resultFilePath + '\\TestResult\\'
    print(resultFilePath)

    files = os.listdir(resultFilePath)
    lastFileCTime = 0
    lastFile = ''
    for f in files:
        f = resultFilePath + f
        ctime = os.path.getctime(f)
        if ctime > lastFileCTime:
            lastFileCTime = ctime
            lastFile = f
    print'The last file is: ', lastFile


    addContent = '<tr>\n\
    <th align="left">' + CERLinux_UI_002 + '</th>\n\
    <th><font color="red">Failed</font></th>\n\
    <th>2013/7/8 2:48:31 PM</th>\n\
    <th>breaked off</th>\n\
    </tr>\n\
    </table><br><br>\n'

    fobj_input = open(lastFile,'r')
    lines = fobj_input.readlines()
    fobj_input.close()

    fobj_output = open(lastFile,'w')
    for line in lines:
        if line.startswith('</table><br><br>'):
            fobj_output.write(addContent)
            print addContent
        else:
            fobj_output.write(line)
            print line
    fobj_output.close()
