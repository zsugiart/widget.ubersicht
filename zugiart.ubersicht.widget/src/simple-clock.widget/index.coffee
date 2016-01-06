format = '%a %b %d %l:%M %p'
command: "date +\"#{format}\""

# the refresh frequency in milliseconds
refreshFrequency: 30000

render: (output) -> """
  <h1>#{output}</h1>
"""

style: """
  color: #FFFFFF
  font-family: Helvetica Neue
  left: 30px
  bottom: 170px
  width: 460px

  h1
    font-size: 2.5em
    font-weight: 100
    margin: 0
    padding: 0px 0px 5px 0px
    width: 100%
    border-bottom: 3px solid rgba(#fff, 0.3)
    border-radius: 1px

  """
