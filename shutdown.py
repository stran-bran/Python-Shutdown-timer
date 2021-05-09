import math
import os
import sys
from datetime import datetime
from datetime import timedelta

def getTime():
    # convert decima time to hh/mm/ss
    time = input('Set timer (hrs): ')
    stime = float(time)*3600
    hrs = math.floor(float(time))
    min = (float(time)*60) % 60
    sec = (float(time)*3600) % 60
    # get current time and shutdown time
    # Thisget current time and shutdown time
    now = datetime.now()
    endTime = now + timedelta(hours=hrs,minutes=min,seconds=sec)
    # this convert time to format
    pCurrent = now.strftime("%H:%M:%S")
    pEnd = endTime.strftime("%H:%M:%S")
    # this set shutdown timer
    os.system(f'shutdown /s /t {int(stime)}')
    #outputs
    print("!!!Shutdown timer set!!!")
    print("System shutdown in: " + "%d:%02d:%02d" % (hrs, min, sec))
    print("Current Time :", pCurrent)
    print("Shutdown time :", pEnd)
    #cancel command
    killTimer()
    
def killTimer():
    cancel = input('Enter "KILL" to cancel timer: ')
    while(cancel != "KILL"):
        print("!!!ERROR: unknowcommand. Re enter!!!")
        cancel = input('Enter "KILL" to cancel timer: ')
    os.system('shutdown /a')
    input("Timer cacelled. \n Press Enter to exit........")

getTime()