import os


# Method for rendering the widget HTML 
# in the structure for ZENOSX Ubersicht BAR Widget
def renderWidgetBarHTML(title,controlModels):

  print "<!-- WIDGET TITLE -->"
  print "<div class='widgetLabel'>%s</div>" % title
  
  print "<!-- WIDGET CONTROLS -->"
  print "<div class='widgetControl'>"

  for control in controlModels:
    print """ 
    <div class='c_barWrapper'>
      <div class='c_barBg'>
        <div class='c_barFg' style="width:%d%%"></div>
      </div>
      <div class='c_val'>
        <div class='label'>%s</div><div class='value'>%d%%</div> 
      </div>
    </div>
    """ % (control['pct'],control['label'],control['pct'])

  print "</div> <!-- end widgetControl -->"
   

def main():
  _title="DISK"
  _barControls=[]

  cmdOutput = os.popen("df -h | grep '/dev/'").read()
  for diskLine in cmdOutput.strip().split('\n'):
    
    diskRec=diskLine.split()

    diskLabel="OS"
    if "/" != diskRec[8]: diskLabel=diskRec[8].strip().split('/')[-1]

    _barControls.append({"label":diskLabel,"pct":float(diskRec[7][:-1])})


  renderWidgetBarHTML(_title,_barControls)

if __name__ == "__main__":
    main()