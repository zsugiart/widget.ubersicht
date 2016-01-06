import os
import sys

## COMMON SETUP

if not os.path.isfile(os.environ["US_ZENOSX_DIR"]+"/ZENOSX_VER"): os._exit(1)
sys.path.insert(0, os.environ["US_ZENOSX_DIR"])
from USZenOSXConfig import *
ZENOSX.setName("Z.WATCHER")

import subprocess
import time
from threading import Thread


#======================================================================================================
# Helpers
#======================================================================================================

"""
This thread counts the second, and then kills the entire camp 
after the time is up.
"""
def Suicider(secondMax):
    if( secondMax <= 0 ): os._exit(1)   # if secondMax is0 or less, exit immediately
    for i in range(0,secondMax):    
        time.sleep(1)                   # else, sleep for specified seconds
    ZENOSX.log_info("time is up! exiting")
    os._exit(1)                         # then exit the whole thing

"""
This thread listens to diskutil activity, when an activity is detected, it waits 2 second
and touch the file specified
"""
def DiskListener(fileToTouch):
    # move on 
    p = subprocess.Popen(args   = ['diskutil','activity'],
                             stdout = subprocess.PIPE,
                             universal_newlines=True)
        
    while p.poll() is None:
        data = p.stdout.readline()
        if "/Volumes/" in data:
            ZENOSX.log_debug(data.strip())
            
            time.sleep(3)
            ZENOSX.ubersicht_touch(fileToTouch)

def main():
    
    ZENOSX.log_info("*** Watcher process starting ***")
    
    ZENOSX.checkPID()
    
    # parse the parameters
    secondsToLive=int(sys.argv[1])
    fileToTouch=sys.argv[2]
    if not os.path.isfile(fileToTouch):
        print "! file not found: %s " % fileToTouch
        os._exit(1) # exit if file not found
    
    ZENOSX.log_info("*** secondsToLive=%s // fileToTouch=%s"  % (secondsToLive,fileToTouch))
        
    # starts the suicider
    Thread(target=Suicider, args=([secondsToLive])).start()
    Thread(target=DiskListener, args=([fileToTouch])).start()
    
    while 1:
        ZENOSX.log_debug("<HEARTBEAT>")
        time.sleep(15) # beats every 15 second

if __name__ == "__main__":
    main()
    
