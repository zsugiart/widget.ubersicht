## @@ TOUCHED BY AN ANGEL AT 2015-12-31T18:24:13
## DISK BARS

## ====================================================================================
## Command + Refresh Frequency
## ====================================================================================

# This is hardcoded, if there is a way of making this relative please let me know (zenfeed@twitter)
command: 'python "$HOME/Library/Application Support/Übersicht/widgets/ZENOSX.widget/DISK.widget/run.py"'

## how often to refresh, in milisecond

## manual refresh every 3 hour - see _SYS. Watcher thread will listen to diskUtil events
## and modify content of this file to trigger widget refresh, this stops aggressive polling
refreshFrequency: 10800000

## ====================================================================================
## CSS STYLE
## ====================================================================================

style: """
  bottom: 40px
  left: 30px
  width: 500px
  color: #fff

  .widgetLabel
    font: 15pt normal "Helvetica Neue"
    text-shadow: 0 0 1px rgba(#000, 0.5)
    font-weight: 100
    letter-spacing: 2px
    float:left
    width: 80px
    color: #fff

  .widgetControl
    float:left

  .c_barWrapper
    width:100px
    margin: 3px 30px 15px 0px
    float:left

  .c_barBg
    width: 100%
    background: rgba(#000,0.4)
    height: 5px
    border-radius: 5px
  
  .c_barFg
    background: #ccc
    height: 5px
    border-radius: 5px

  .c_val
    font: 8pt normal "Helvetica Neue"
	text-transform: lowercase
    padding-top: 3px
  
  .c_val .label
    float:left
    padding-right: 10px
  
  .c_val .value
    float: right

"""


## ====================================================================================
## RENDER
## ====================================================================================
## Below section will be completely overwritten with output from command
## So make sure whatever script/program being called will output a matching structure
## Below section only show the expected structure

render: -> """

<div class='widgetLabel'>
  LABEL PLACEHOLDER
</div>

<div class='widgetControl'>

  <!-- BAR + LABEL/VALUE -->
  <div class='c_barWrapper'>
    <div class='c_barBg'>
      <!-- c_barFG widh controls the progress bar -->
      <div class='c_barFg' style="width:80%"></div>
    </div>
    <div class='c_val'>
      <div class='label'>unit-label</div><div class='value'>80%</div> 
    </div>
  </div>

  <!-- ... REPEAT AS NECESSARY -->
</div>

"""

update: (output, domEl) ->
  $(domEl).html(output)
