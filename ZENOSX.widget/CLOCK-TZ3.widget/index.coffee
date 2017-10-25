TZ3="America/Los_Angeles"

format = '%l:%M %p'
command: "TZ=#{TZ3} date +\"#{TZ3}: #{format}\""

# the refresh frequency in milliseconds
refreshFrequency: 30000

render: (output) -> """
  <h2>#{output}</h2>
"""

style: """
  color: #FFFFFF
  font-family: Helvetica Neue
  left: 380px
  bottom: 140px
  width: auto
  height: 30px

  h2
    font-size: 1.2em
    font-weight: 100
    margin: 0
    padding: 0px 0px 6px 0px
    width: auto

  .subtime
    float:left
    padding-right: 15px

  """
