## ZEN OSX CALENDAR
## Ver1.0.4

## CONFIG

# how many month to show 
monthToShowAhead=3
		
## ====================================================================================
## Command + Refresh Frequency
## ====================================================================================

# This is hardcoded, if there is a way of making this relative please let me know (zenfeed@twitter)
command: 'export US_ZENOSX_DIR="$PWD/ZENOSX.widget"; python "ZENOSX.widget/CAL.widget/cal.py" '+monthToShowAhead+' "ZENOSX.widget/CAL.widget/HOLIDAYS/offdays.csv"'

## 1 hour rate
refreshFrequency: 3600000

## ====================================================================================
## CSS STYLE
## ====================================================================================

style: """
	bottom: 50px
	left: 520px
	width: 660px
	color: #fff
	font-family: "Helvetica Neue"
	font-size: 9pt

	.calbox
		float:left
		padding:15px 20px 0px 0px

	h2
		font-size: 17pt
		font-weight: 100
		padding-left: 5px
		margin: 0px

	.calWeek
		color: rgba(#99ccff,0.3)
		padding-left: 5px
		text-align: center
		font-size: 8pt
		text-transform: italic

	.calDate
		padding: 3px
		text-align: center

	.today
		border-radius: 15px
		background: rgba(#aaa,0.5)

	.notThisMonth
		color: rgba(#888,0)

	.holiday
		color: rgba(#f00,0.9)

"""


## ====================================================================================
## RENDER
## ====================================================================================
## Below section will be completely overwritten with output from command
## So make sure whatever script/program being called will output a matching structure
## Below section only show the expected structure

render: -> """

<!-- THIS HTML WILL BE REPLACED BY CAL.PY OUTPUT
THIS IS ONLY PLACEHOLDER -->

<div class='calbox'>
		<h2>December 2015</h2>
		<table class='caltable'>
			<tr>
				<th class='calWeek'></th>
				<th class='calDate'>Mo</th>
				<th class='calDate'>Tu</th>
				<th class='calDate'>We</th>
				<th class='calDate'>Th</th>
				<th class='calDate'>Fr</th>
				<th class='calDate'>Sa</th>
				<th class='calDate'>Su</th>
			</tr>
			<tr>
				<td class='calWeek'>49</td>
				<td class='calDate notThisMonth'>7</td>
				<td class='calDate'>1</td>
				<td class='calDate'>2</td>
				<td class='calDate'>3</td>
				<td class='calDate'>4</td>
				<td class='calDate'>5</td>
				<td class='calDate'>6</td>
			</tr>
			<tr>
				<td class='calWeek'>50</td>
				<td class='calDate'>7</td>
				<td class='calDate'>8</td>
				<td class='calDate'>9</td>
				<td class='calDate'>10</td>
				<td class='calDate'>11</td>
				<td class='calDate'>12</td>
				<td class='calDate'>13</td>
			</tr>
			<tr>
				<td class='calWeek'>51</td>
				<td class='calDate'>14</td>
				<td class='calDate'>15</td>
				<td class='calDate'>16</td>
				<td class='calDate'>17</td>
				<td class='calDate'>18</td>
				<td class='calDate'>19</td>
				<td class='calDate'>20</td>
			</tr>
			<tr>
				<td class='calWeek'>52</td>
				<td class='calDate'>21</td>
				<td class='calDate'>22</td>
				<td class='calDate'>23</td>
				<td class='calDate'>24</td>
				<td class='calDate'>25</td>
				<td class='calDate'>26</td>
				<td class='calDate'>27</td>
			</tr>
			<tr>
				<td class='calWeek'>53</td>
				<td class='calDate today'>28</td>
				<td class='calDate'>29</td>
				<td class='calDate'>30</td>
				<td class='calDate'>31</td>
				<td class='calDate notThisMonth'>8</td>
				<td class='calDate notThisMonth'>9</td>
				<td class='calDate notThisMonth'>3</td>
			</tr>
		</table>
	</div>
	<!-- end calbox -->

"""

update: (output, domEl) ->
  $(domEl).html(output)