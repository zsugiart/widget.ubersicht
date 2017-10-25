## BAR-OS
## Ver1.0.2
		
## ====================================================================================
## Command + Refresh Frequency
## ====================================================================================


# This is hardcoded, if there is a way of making this relative please let me know (zenfeed@twitter)
command: ''

## how often to refresh, in milisecond

refreshFrequency: 15000


## ====================================================================================
## CSS STYLE
## ====================================================================================

style: """
  bottom: 25px
  left: 0px
  width: 100%
  height: 220px
  color: #fff
  background: rgba(#000,0.55)
  z-index: -999
"""


## ====================================================================================
## RENDER
## ====================================================================================
## Below section will be completely overwritten with output from command
## So make sure whatever script/program being called will output a matching structure
## Below section only show the expected structure

render: -> """

<div class='bgBar'>
</div>

"""

update: (output, domEl) ->
  $(domEl).html(output)
