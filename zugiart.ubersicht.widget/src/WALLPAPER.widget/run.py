
## SETUP BLOCK

import traceback
import os,sys
if not os.path.isfile(os.environ["US_ZENOSX_DIR"]+"/ZENOSX_VER"): 
    print "ERROR: US_ZENOSX_DIR is not set correctly"
    os._exit(1)
sys.path.insert(0, os.path.join(os.environ["US_ZENOSX_DIR"],"_SYS"))
from USZenOSXConfig import *
ZENOSX.setName("Z.WPaper")

import random

_WP_CONFIG={'lastIndex':0}

_PARAM_METHOD=["random","sequence"]

def getNextSequence(listSize):
    global _WP_CONFIG
    try:
        _WP_CONFIG=ZENOSX.pickleRead("WP")
    except:
        traceback.print_exc() 
    idx = _WP_CONFIG['lastIndex']
    if idx<listSize-1: _WP_CONFIG['lastIndex']=idx+1
    else: _WP_CONFIG['lastIndex']=0
    ZENOSX.pickleWrite("WP",_WP_CONFIG)
    return idx
            
"Read a directory full of wallpaper, and select a wallpaper by returning a full path"
def main():
    ZENOSX.log_info("*** Starting Wallpaper ***")
    
    p_method=sys.argv[1]
    p_dir=sys.argv[2]
    
    ZENOSX.log_debug("method=%s // path=%s" % (sys.argv[1],sys.argv[2]))
    
    if p_method not in _PARAM_METHOD: raise Exception("Method (argv1) is not valid. Choose from: %s" % _PARAM_METHOD)
    
    wpList=[]
    
    for dirname, dirnames, filenames in os.walk(p_dir):
        # print path to all filenames.
        for filename in filenames:
            wpList.append(filename)
    
    wp=None
    if p_method == "random":
        wp= random.choice(wpList)
    elif p_method == "sequence":
        wp=wpList[getNextSequence(len(wpList))]
    else:
        raise Exception("ERROR")
    
    ZENOSX.log_debug("wp=%s"%os.path.join(p_dir,wp))
    print os.path.join(p_dir,wp)
    
if __name__ == "__main__":
    main()