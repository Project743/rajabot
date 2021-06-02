


def clean(text):
	clean_txt = ''
	for ch in text.lower():
		if ch in 'qwertyuiopasdfghjklzxcvbnm':
			clean_txt += ch


	return clean_txt

	
def get_question(question):
	str_number = []
	que = []
	search_string = clean(question)
	with open("obsh.txt") as file:
		n = 0
		for line in file:
			n += 1
			if search_string in clean(line):
				str_number.append(n)
	#print(str_number)
	with open("obsh.txt") as file:
		line = file.readlines()
	for i in str_number:
		TXT = line[i-1]+line[i]
		que.append(TXT)
	answer = "".join(que)
	
	return answer
