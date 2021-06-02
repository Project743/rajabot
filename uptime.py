#парсер времени UTC

import requests
from bs4 import BeautifulSoup


user_agent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36')

url = 'https://time.is/UTC'
def time_UTC():
	response = requests.get(url, headers={'User-Agent':user_agent})
	soup = BeautifulSoup(response.text, 'lxml')
	quotes = soup.find_all('div', id="clock0_bg")

	for quote in quotes:
		time = int(quote.text.replace(':',''))//100	
	return time

print(time_UTC())

def day_UTC():
	response = requests.get(url, headers={'User-Agent':user_agent})
	soup = BeautifulSoup(response.text, 'lxml')
	quotes = soup.find_all('div', id="dd")
	

	for quote in quotes:
		day = quote.text	
	return day

print(day_UTC())