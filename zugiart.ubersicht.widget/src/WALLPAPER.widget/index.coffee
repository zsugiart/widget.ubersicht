# The wallpaper folder path
# to replace this to other folder, create a symlink that replaces /WP
# example: ln -s <target_folder> WP
# Ubersicht can't load image file outside of the ubersicht widget folder

wallpaperFolder="ZENOSX.widget/WALLPAPER.widget/WP"

# Options are:
#  "random"   - picks one from the folder
#  "sequence" - move from one wallpaper to the next
#  if you only have one WP, leave this be

wallpaperRotate="random"

# The style of the wallpaper

wallpaperStyle:"center fixed"

# This is hardcoded, if there is a way of making this relative please let me know (zenfeed@twitter)

command: 'export US_ZENOSX_DIR="./ZENOSX.widget"; python "ZENOSX.widget/WALLPAPER.widget/run.py" '+wallpaperRotate+' "'+wallpaperFolder+'"'

## how often to refresh, in milisecond

refreshFrequency: 24*60*60*1000

## =====================================================================================
## CSS STYLE
## ====================================================================================

style: """
	/* bottom CSS is to protect against "auto hide menubar" */
	bottom: 0px
	left: 0px
	padding: 0px
	margin: 0px
	color: #fff
	z-index: -1000
	width: 1440px
	height: 990px
	
	/* The wallpaper itself */
	.wallpaper
		width: 100%
		height: 100%
		background: none /* see update() */
		
	/* The blurry part of the wallpaper */
	.bgmask
		position: absolute
		width: 100%
		height: 220px
		background: none /* see update() */
		-webkit-filter: blur(7px)
		bottom: 20px

	/* For colorizing the mask */
	.bgmaskColor
		width: 100%
		height: 100%
		background: rgba(#444,0.3)

"""

## ===================================================================================
## RENDER
## ===================================================================================
## Below section will be completely overwritten with output from command
## So make sure whatever script/program being called will output a matching structure
## Below section only show the expected structure

render: -> """
<div class='wallpaper'/>
<div class='bgmask'>
	<div class='bgmaskColor'/>
</div>
"""

update: (output, domEl) ->
	
	wpFile=output.replace /^\s+|\s+$/g, ""
	$(domEl).find('.wallpaper').hide()
	$(domEl).find('.wallpaper').css
		"background":"url('"+wpFile+"') "+@wallpaperStyle
	$(domEl).find('.bgmask').css
		"background":"url('"+wpFile+"') "+@wallpaperStyle
	$(domEl).find('.wallpaper').fadeIn("slow")
	