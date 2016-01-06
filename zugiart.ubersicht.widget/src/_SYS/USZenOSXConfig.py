import logging
import logging.handlers
import os
import signal
import datetime
import subprocess
import sys
import traceback

#
#======================================================================================================
# CONFIG
#======================================================================================================

def configLogger():
    loggerObj = logging.getLogger("")
    logfile = os.path.join(os.environ["US_ZENOSX_DIR"],'_LOG/ubersicht-ZENOSX.log')
    lh = logging.handlers.RotatingFileHandler(logfile, 
         maxBytes=10*1024,backupCount=0)
    lh.setFormatter(logging.Formatter('%(asctime)s | %(levelname)7s | %(message)s'))
    loggerObj.addHandler(lh)
    return loggerObj

_ZLOGGER = configLogger()
_ZLOGGER.setLevel(logging.DEBUG)

class ZENOSX:
    
    __ZENOSX_CONFIG={ 
    "name":"ZENOSX.Widget",
    "US_ZENOSX_DIR":os.environ["US_ZENOSX_DIR"]            
    }
    
    @staticmethod
    def setName(name):
        ZENOSX.__ZENOSX_CONFIG['name']=name
        
    @staticmethod
    def getName():
        return ZENOSX.__ZENOSX_CONFIG['name'] 
    
    @staticmethod
    def checkPID():
        pidFname = os.path.join(ZENOSX.getConfig("US_ZENOSX_DIR"),"_LOG/%s__PID__" % ZENOSX.getName())
        # a file is leftover, kill pid and remove it first
        if os.path.isfile(pidFname):
            f = open(pidFname)
            for line in f:
                pid=line.strip()
                ZENOSX.log_warn("PID %s detected - killing previous process" % (pid))
                try: cmdOutput = os.popen("kill -9 %s &> /dev/null" % pid)
                except: pass
            f.close() # close the file
            os.remove(pidFname) # remove it
            ZENOSX.log_warn("__PID__ file removed")
        f = open (pidFname,'a') # (re)open file
        f.write("%s\n"%os.getpid()) # write the pID of this process
        f.close() 
    
    @staticmethod 
    def log_info(msg): _ZLOGGER.info("%10s | %s " % (ZENOSX.getName(),msg))
    @staticmethod 
    def log_error(msg): _ZLOGGER.error("%10s | %s " % (ZENOSX.getName(),msg))
    @staticmethod 
    def log_warn(msg): _ZLOGGER.warn("%10s | %s " % (ZENOSX.getName(),msg))
    @staticmethod
    def log_debug(msg): _ZLOGGER.debug("%10s | %s " % (ZENOSX.getName(),msg))
    
    @staticmethod
    def getConfig(key):return ZENOSX.__ZENOSX_CONFIG[key]
    @staticmethod
    def setConfig(key,value): ZENOSX.__ZENOSX_CONFIG[key]=value
    
    @staticmethod
    def ubersicht_touch(fname, times=None):
        ## Because of the way Ubersicht detects changes, this magically buffers changes within the same second
        tstamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        ZENOSX.log_info("touching file: times=%s, fname=%s" % (times,fname))
        sub = subprocess.call(
            ['sed', '-i', '.bak', "s/^## @@.*/## @@ TOUCHED BY AN ANGEL AT "+tstamp+"/",fname])
        
    @staticmethod
    def signalHandler(signum, frame):
        ZENOSX.log_warn("received signal %s" %signum)
        ZENOSX.getTheFuckOut()
    
    @staticmethod
    def getTheFuckOut():
        ZENOSX.log_info("Termination: cleaning  up resources...")
        try:
            ZENOSX.log_debug("removing PID file %s " % os.path.join(ZENOSX.getConfig("US_ZENOSX_DIR"),"_LOG/__PID__"))
            os.remove(os.path.join(ZENOSX.getConfig("US_ZENOSX_DIR"),"__PID__"))
        except:
            ZENOSX.log_error("ERROR: %s" % traceback.format_exc())
            pass
        finally:
            print "TERMINATED"
            ZENOSX.log_info("Termination: complete. Exit now")
            os._exit(1)


# Register signal handler
    
signal.signal(signal.SIGTERM, ZENOSX.signalHandler)
signal.signal(signal.SIGINT, ZENOSX.signalHandler)

# Log setup

logging.info("Config initialized.")
logging.info("DIR: %s" % os.environ["US_ZENOSX_DIR"])

