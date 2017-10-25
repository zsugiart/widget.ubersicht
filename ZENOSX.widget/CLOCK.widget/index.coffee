format = '%a %b %d %l:%M %p'
command: "date +\"#{format}\""

# the refresh frequency in milliseconds
refreshFrequency: 30000

render: (output) -> """
  <h2>#{output}</h2>
"""

style: """
  color: #FFFFFF
  font-family: Helvetica Neue
  left: 30px
  bottom: 175px
  width: 600px

  h2
    font-size: 2.5em
    font-weight: 100
    margin: 0
    padding: 0px 0px 5px 0px
    width: 100%
    border-bottom: 3px solid rgba(#fff, 0.3)
    border-radius: 1px

  .subtime
    float:left
    padding-right: 15px

  """
