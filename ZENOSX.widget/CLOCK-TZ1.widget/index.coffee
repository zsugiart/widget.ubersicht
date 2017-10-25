TZ1="Japan"

format = '%l:%M %p'
command: "TZ=#{TZ1} date +\"#{TZ1}: #{format}\""

# the refresh frequency in milliseconds
refreshFrequency: 30000

render: (output) -> """
  <h2>#{output}</h2>
"""

style: """
  color: #FFFFFF
  font-family: Helvetica Neue
  left:  30px
  bottom: 140px
  width: auto
  height: 30px

  h2
    font-size: 1.2em
    font-weight: 100
    margin: 0
    padding: 0px 0px 5px 0px
    width: auto

  .subtime
    float:left
    padding-right: 15px

  """
