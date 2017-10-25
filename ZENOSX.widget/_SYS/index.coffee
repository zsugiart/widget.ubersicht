## BAR-OS
## Ver1.0.2++++

ZENOSX_HOME="$PWD/ZENOSX.widget"

# This is hardcoded, if there is a way of making this relative please let me know (zenfeed@twitter)
# runs the watcher process for 12 hours - should be long enough to survive most sleeps
#command: "export US_ZENOSX_DIR=\""+ZENOSX_HOME+"\"; python \"ZENOSX.widget/_SYS/watcher.py\" 43200 \"ZENOSX.widget/DISK.widget/index.coffee\""

command: "echo DISABLED"

## how often to refresh, in milisecond

# 1 hour = 3600000ms, gives 5 second breathing space for ramp down
refreshFrequency: 6000000000

## ====================================================================================
## CSS STYLE
## ====================================================================================

style: """
	top: 100px
	left: 30px
	width: 500px
	color: #fff
	display:none
"""

## ====================================================================================
## RENDER
## ====================================================================================
## Below section will be completely overwritten with output from command
## So make sure whatever script/program being called will output a matching structure
## Below section only show the expected structure

render: -> """
# WHATEVER 2
"""

update: (output, domEl) ->
  $(domEl).html(output)