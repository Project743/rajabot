from datetime import datetime





def new_day():
	current_date = str(datetime.now().date())
	current_time = datetime.now().time()
	current_hour = int(current_time.hour)
	cyrrent_minute = int(current_time.minute)
	
	if current_hour == 9 and cyrrent_minute == 05:
		f = open('date.txt','r')
		save_date = f.read()

		if save_date == current_date:
			print(f.read())
		else:
			f = open('date.txt','w')
			f.write(current_date)
			print('date update')
		return 1
	else:
		return 2
	print(LABEL)
