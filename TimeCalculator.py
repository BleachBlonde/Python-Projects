#seconds_in_day: 86400
#seconds_in_hour: 3600
#seconds_in_minute: 60

secondsTotal= int(input('Enter number of seconds: '))

if secondsTotal>=86400:
	days= int(secondsTotal/86400)
	hours= int((secondsTotal-(86400*days))/3600)
	minutes= int((secondsTotal-(86400*days+3600*hours))/60)
	seconds= int((secondsTotal-(86400*days+3600*hours+60*minutes)))
if secondsTotal<86400:
	days= 0
	hours= int(secondsTotal/3600)
	minutes= int((secondsTotal-(3600*hours))/60)
	seconds= int((secondsTotal-(3600*hours+60*minutes)))
if secondsTotal<3600:
	days= 0
	hours= 0
	minutes= int(secondsTotal/60)
	seconds= int((secondsTotal-(60*minutes)))
if secondsTotal<60:
	days= 0
	hours= 0
	minutes= 0
	seconds= int(secondsTotal)

print (days,'day(s),',hours,'hour(s),',minutes,'minute(s), and', seconds,'second(s).')

input('\nPlease press ENTER to exit.')
