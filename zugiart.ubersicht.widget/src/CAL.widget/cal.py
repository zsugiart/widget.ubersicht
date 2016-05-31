
## SETUP BLOCK

import traceback
import os,sys
if not os.path.isfile(os.environ["US_ZENOSX_DIR"]+"/ZENOSX_VER"): 
    print "ERROR: US_ZENOSX_DIR is not set correctly"
    os._exit(1)
sys.path.insert(0, os.path.join(os.environ["US_ZENOSX_DIR"],"_SYS"))
from USZenOSXConfig import *
ZENOSX.setName("Z.CAL")

from datetime import datetime, date

"""
This python script parse the output of ncal -w and transpose it to the cal format, with week numbers on the leftmost column
the parsed ncal is kept in two dimensional array
"""

_NOW = datetime.now()
_NOW_DATE = date(_NOW.year,_NOW.month,_NOW.day)

class DateCell:
    cssClass=""
    value=""
    
    def __init__(self,dateObj):
        self.value=dateObj
        
        if( dateObj is None ):
            self.value="N/A"
            return
        
        if ( self.value.year == _NOW_DATE.year and
             self.value.month== _NOW_DATE.month and
             self.value.day  == _NOW_DATE.day ):
            self.addClass("today")
    
    def addClass(self,cssClass):
        self.cssClass+=" %s"%cssClass
        
    def __str__(self):
        return "%d" % int(datetime.strftime(self.value,'%d')) if isinstance(self.value,date) else self.value
    
    def __repr__(self):
        return self.__str__()
    
    # given parameter of weekNum, dayShortAbbr(mo, tu, th..).
    # month, and year - work out the date and fill it into
    # this object. Will also add cssClass "notThisMonth"
    def resolve(self,year,weekNum,dayShortAbbr):
        #print ("resolving: year=%d weekNum=%s day=%s " % (year, weekNum, dayShortAbbr)),
        dayLookup = { "Su":0,"Mo":1 ,"Tu":2,"We":3,"Th":4,"Fr":5,"Sa":6 }
        dayNum = dayLookup[dayShortAbbr.strip()]
        # weekNum expected from datetime strptime starts from 0
        resolveStr="%s %02d %s"%(year,int(weekNum)-1,dayNum)
        self.value=datetime.strptime(resolveStr,"%Y %W %w")
        #print "==> %s" % self.value
        self.addClass("notThisMonth")
        

"""
Parse a CSV file with list of holidays in the format of [0] date, [1] description
"""

def parseHoliday(filePath):
    f = open(filePath)
    holSet={}
    for line in f:
        if '#' in line[0:5]: continue # ignore comments
        rec=line.strip().split(",")
        ZENOSX.log_debug("parsing holiday: %s" % rec)
        # check to see if date format is OK?
        date = datetime.strptime(rec[0],"%Y-%m-%d")
        holSet[rec[0]]=rec
    return holSet


"""
Parses output of ncal-w [month] [year] into a 2 dimensional array in the format of 'cal'
@return: [calendarTitle,calendarMatrix] for the given month and year
format of the matrix is: 
[
  ['Mo','Tu','We','Th','Fr', '' ],
  [    , 1  , 2  , 3  , 4  , 32 ],
  [ 5  , 6  , 7  , 8  , 9  , 33 ],
  ...
]

Each calendar node in the array is a DateCell object

@param month month number (1-12)
@param year year number (2015)
@param holidaySet - {"yyyy-mm-dd":["yyyy-mm-dd","holidayDescription"],...}

"""
def parseNCAL(month,year,holidaySet):
    
    ZENOSX.log_debug("parsing: month=%s year=%s holidaySet=%s" %(month,year,holidaySet))
    
    cmdOutput = os.popen("ncal -w %d %d" % (month,year)).read().strip()
    # print cmdOutput
    
    rec = cmdOutput.split('\n')
    
    calTitle    = rec[0]
    # cut out first bit
    rec=rec[1:len(rec)]
    

    # hold data here
    matrix=[]
    
    ## work out the week number as header
    weekRec=rec[-1].split()
    weekRec.insert(0,"") # add header
    
    # parse everything except the week numbers
    for i in range(0,len(rec)-1):
        mrec=[]
        
        # first column is always day name
        dayHeader = rec[i][0:2]
        mrec.append( dayHeader)
        
        columnIter=1 #
        # rest are values
        for j in range (3,3*len(weekRec),3):
            strDate=rec[i][j:j+2]
            dateVal=DateCell(None)
            
            ZENOSX.log_debug(">>> j=%d/%d Wk=%s(%d) Day=%s date=%s " % (j,len(rec[i]), weekRec[columnIter],columnIter, dayHeader, strDate))
           
            # if no dates (last/next month) add None
            if strDate.strip() != "":
                dateNum= int(strDate)
                dateVal= DateCell(datetime.strptime('%d %d %d' % (year,month,dateNum), '%Y %m %d' ))
                holKey="%d-%0.2d-%0.2d" % (year,month,dateNum)
                try: 
                    ZENOSX.log_debug("holiday: %s" % holidaySet[holKey])
                    dateVal.addClass("holiday")
                except: pass # not holiday 
            else:
                dateVal.resolve(year,weekRec[columnIter],dayHeader)
                
            mrec.append(dateVal)
            columnIter+=1
            
        matrix.append(mrec) 
        
    matrix.append(weekRec)   
    
    # transpose the array matrix into cal format
    transpose=zip(*matrix)
    return calTitle,transpose

def renderCalHTML(calTitle, calArray):
    
    ## DISPLAY PART
    
    print "<div class='calbox'>"
    print "<h2>%s</h2><table class='caltable'>" % calTitle
    for ri in range(0,len(calArray)):
        # if first row, use TH instead of td
        tag = "th" if ( ri == 0 ) else "td"
        print"<tr>"
        for di in range(0,len(calArray[ri])):
            
            # first cell is always a calWeek
            cellClass = "calDate" if (di<len(calArray[ri])-1) else "calWeek" 
            cellVal = calArray[ri][di]
            
            # print it out
            print("  <%(tag)s class='%(class)s'>%(val)s</%(tag)s>" % {
                            'val':cellVal,
                            'tag':tag,
                            'class':cellClass+cellVal.cssClass if isinstance(cellVal,DateCell) else cellClass }),
        print ("\n</tr>")
    print "</table></div><!-- end calbox -->"
            
def main():

    ZENOSX.log_info("*** Starting Calendar Job ***")
    
    monthIter=1
    # how many calendar ahead to show
    try: 
        monthIter=int(sys.argv[1])
    except: pass
    if monthIter <= 0 or monthIter == None: monthIter=1
    
    try:
        holidaySet=parseHoliday(sys.argv[2])
    except Exception:
        traceback.print_exc()
        ZENOSX.log_error("Error parsing holiday file: %s" % sys.argv[2])
        holidaySet = {}
    
    nextMonth=_NOW_DATE.month; nextYear =_NOW_DATE.year
    for i in range(0,monthIter):
        # parse NCAL result for the month
        parseResult=parseNCAL(nextMonth,nextYear,holidaySet)
        # render the parsed data
        renderCalHTML(parseResult[0],parseResult[1])
        # move on to the next month
        if nextMonth==12: nextMonth=1; nextYear+=1
        else: nextMonth+=1

if __name__ == "__main__":
    main()