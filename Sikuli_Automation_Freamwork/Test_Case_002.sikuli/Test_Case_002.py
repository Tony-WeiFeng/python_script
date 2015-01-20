import os
import time

#Clear this machine
#Delete UI folder
os.system('rd /s/q C:\\ProgramData\\Autodesk\\SampleApp_test')
os.system('rd /s/q C:\\ProgramData\\Autodesk\\MC3')

#Delete UD folder
os.system('rd /s/q C:\\Users\\Administrator\\AppData\\Roaming\\Autodesk\\SampleApp_test')
os.system('rd /s/q C:\\Users\\Administrator\\AppData\\Roaming\\Autodesk\\MC3')

#Delete Registry
os.system('reg delete HKEY_CURRENT_USER\Software\Autodesk\MC3 /f')

def getCurrentTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

#Creat log file
ls = os.linesep
entry = getCurrentTime() + "  ==================Test_Case_002 Log Started==================\n"

#all.append(entry)
fobj = open('C:\Users\Administrator\Desktop\log.txt','a')
#fobj = writelines(['%s%s' % (x,ls) for x in all])
fobj.writelines(entry)
fobj.close()

#First time launch Sample
doubleClick("1369121536135.png")
click("InitMC3DemoU-1.png")
click("N0.png")

#DA init dialog pops up, click OK button to opt-in
click("OK.png")

all = []
entry = getCurrentTime() + "  DA optted-in."
all.append(entry)

click(Pattern("OK-1.png").similar(0.81))

#Invoke CIP dialog
click("Help.png")
click("CustomerInvo.png")

#Opt-in CIP
click(Pattern("YesIwouldlik.png").targetOffset(-115,-1))
click("OK-2.png")

entry = getCurrentTime() + "  CIP optted-in."
all.append(entry)

fobj = open('C:\Users\Administrator\Desktop\log.txt','a')
fobj.writelines(['%s%s' % (x,ls,) for x in all])
fobj.close()

click("Cancel.png")
click("OK-3.png")

#for i in range(250):  #comments this line for demo
for i in range(1):

    fobj = open('C:\Users\Administrator\Desktop\log.txt','a')
    fobj.writelines(getCurrentTime() + "  Loop  %s has been started...\n" %(i+1))
    fobj.close()
    click("InitMC3DemoU-1.png")
    click("N0.png")
    click("OK-5.png")
    
    #wait(150)   #comments this line for demo
	
    all = []
    entry = getCurrentTime() + "  Avro log has been sent out."
    all.append(entry)
    click(Pattern("Cancel.png").similar(0.81))
    click("OK-3.png")
    click(Pattern("DSampleApp.png").targetOffset(292,0))
    
    
    os.system('copy C:\\Users\\Administrator\\AppData\\Roaming\\Autodesk\\SampleApp_test\\2006\\{5783F2D7-5001-0409-0000-0060B0CE6BBA}\\1.1.0.0\\MC3\\Avro\\*.avro C:\\Users\\Administrator\\Desktop\\Avro_bak')
    entry = getCurrentTime() + "  Avro log of this session has been backed up."
    all.append(entry)

    fobj = open('C:\Users\Administrator\Desktop\log.txt','a')
    fobj.writelines(['%s%s' % (x,ls,) for x in all])
    fobj.close()

fobj = open('C:\Users\Administrator\Desktop\log.txt','a')
fobj.writelines(getCurrentTime() + "  ==================Test_Case_002 Complete==================\n")
fobj.close()


