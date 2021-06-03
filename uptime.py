from datetime import datetime



def time_UTC():
	current_time = str(datetime.now().time()).replace(':','')
	time = int(current_time[:current_time.find('.')])//100-300	
	return time


def day_UTC():
	current_date = str(datetime.now().date())
	if datetime.now().weekday() == 0:
		day = 'понедельник'
	elif datetime.now().weekday() == 1:
		day = 'вторник'
	elif datetime.now().weekday() == 2:
		day = 'среда'
	elif datetime.now().weekday() == 3:
		day = 'четверг'
	elif datetime.now().weekday() == 4:
		day = 'пятница'
	elif datetime.now().weekday() == 5:
		day = 'суббота'
	elif datetime.now().weekday() == 6:
		day = 'воскресенье'
	current_day = day + ',' + current_date
	return current_day
print(time_UTC())
print(day_UTC())
