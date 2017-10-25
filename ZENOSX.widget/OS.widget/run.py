import os

def renderWidgetHostnameUptime(hostname,uptime,wifi):
  print "<!-- WIDGET hostname, uptime -->"
  print "<div class='widgetSection hostnameWrapper'>"
  print "<div class='widgetSection hostname'>%s</div>" % hostname
  print "<div class='widgetSection uptime'>%s<br />%s</div>" % (uptime, wifi)
  print "</div>"


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
  _title="OS"
  _barControls=[]

  wifi = "WIFI: N/A"

  # CMD: work out WIFI
  # tested on Yosemite MAC OSX 2015
  try:
    wifiRec = os.popen("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep -E ' SSID'").read().strip().split()
    wifi = "WIFI: %s" %wifiRec[1]
  except: pass #do nothing

  # CMD: work out hostname and uptime
  hostname   = os.popen("hostname").read().strip()  
  uptimeCmd  = os.popen("uptime").read().strip()
  uptime     = (uptimeCmd.split(',')[0][6:]).split(':')[0]+"+"
  if "day" not in uptime and "mins" not in uptime: 
      uptime = uptime+" hr" 

  # RENDER hostname & uptime HTML
  renderWidgetHostnameUptime(hostname,uptime,wifi)

  # CMD: Total CPU utilization
  cmdOutput = os.popen("top -l 1 | grep 'CPU usage' | cut -d':' -f2").read()
  rec=cmdOutput.strip().split(',')
  idlePct=float(rec[2].split()[0][:-1])
  _barControls.append({"label":"cpu","pct":100.0-idlePct})

  # CMD: Total RAM utilization
  cmdOutput = os.popen("memory_pressure | grep 'free per' | cut -d' ' -f5").read()
  rampct = 100.0 - float(cmdOutput.strip()[:-1])
  _barControls.append({"label":"ram","pct":rampct})

  # CMD: Battery
  cmdOutput = os.popen("pmset -g batt | grep -o '[0-9]*%'").read()
  _barControls.append({"label":"power","pct":float(cmdOutput.strip()[:-1])})
  
  # Render
  renderWidgetBarHTML(_title,_barControls)

if __name__ == "__main__":
    main()