# ZENOSX.widget

Zen's OSX Übersicht Widget

## Meta

Author: Zen Sugiarto
Year: 2017 
WWW: [https://zugiart.com](zugiart.com)  
Github:  []()

## Requirements:

Übersicht v0.7: [http://github.com/felixhageloh/uebersicht/](http://github.com/felixhageloh/uebersicht/)
Tested on Macbook Air Early 2015, Yosemite

## Important Note

- This widget uses built in Python (2.7) in OSX, in theory it should just work :)
- However, the path to the directory must not change: this widget is expected to be placed in
  $HOME/Library/Application Support/Übersicht/widgets/ZENOSX.widget/
  Simply, I did not found a way to call the python script with relative path.
- the configuration is set at index.coffee of each folder (CAL.widget, DISK.widget, OS.widget)
