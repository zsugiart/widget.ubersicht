## Comment

command: "find ZENOSX.widget/WALLPAPER.widget/WP -name '*' -type f"

## how often to refresh, in milisecond

# 1 hour = 3600000ms, gives 5 second breathing space for ramp down
refreshFrequency: 360000000

## ====================================================================================
## CSS STYLE
## ====================================================================================

style: """
	top: 0px
	left: 0px
	padding: 0px
	margin: 0px
	color: #fff
	z-index: -2000
	
	.wallpaper
		width: 1440px
		height: 990px
		background: url('ZENOSX.widget/WALLPAPER.widget/WP/wp.jpg') center fixed
		
	.bgmask
		width: 1440px
		height: 220px
		position: absolute
		bottom: 270px
		left: 0px
		background: url('ZENOSX.widget/WALLPAPER.widget/WP/wp.jpg') center fixed
		-webkit-filter: blur(10px)

	.bgmaskColor
		width: 100%
		height: 100%
		background: rgba(#444,0.1)

"""

## ====================================================================================
## RENDER
## ====================================================================================
## Below section will be completely overwritten with output from command
## So make sure whatever script/program being called will output a matching structure
## Below section only show the expected structure

render: -> """
<div class='wallpaper'/>
<div class='bgmask'>
	<div class='bgmaskColor'/>
</div>
"""

  		