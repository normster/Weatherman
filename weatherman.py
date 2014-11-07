import json
import requests

print('Finding location from IP address')

def get_temps(city, state):
	r2 = requests.get('http://api.wunderground.com/api/78c2f37e6d924b1b/hourly/q/%s/%s.json' % (state, city))
	forecast = json.loads(r2.text)
	for x in range(0, 35):
		civil = forecast['hourly_forecast'][x]['FCTTIME']['civil']
		temp = int(forecast['hourly_forecast'][x]['temp']['english'])
		bars = round(temp / 5)
		feelslike = forecast['hourly_forecast'][x]['feelslike']['english']
		wspd = forecast['hourly_forecast'][x]['wspd']['english']
		if temp > int(forecast['hourly_forecast'][x+1]['temp']['english']):
			print('%8s: %3s°F, feels like %3s°F, with %2s mph winds' % (civil, temp, feelslike, wspd), ' ' * bars,'/')
		elif temp == int(forecast['hourly_forecast'][x]['temp']['english']):
			print('%8s: %3s°F, feels like %3s°F, with %2s mph winds' % (civil, temp, feelslike, wspd), ' ' * bars, '|')
		elif temp < int(forecast['hourly_forecast'][x]['temp']['english']):
			print('%8s: %3s°F, feels like %3s°F, with %2s mph winds' % (civil, temp, feelslike, wspd), ' ' * bars, '\\')
	
#use wundergound geolookup api
r1 = requests.get('http://api.wunderground.com/api/78c2f37e6d924b1b/geolookup/q/autoip.json')
location = json.loads(r1.text)
state = location['location']['state']
city = location['location']['city']

#make sure geo is correct
#print('%s, %s' % (city, state))
print(city)
print(state)
correct = ''

while (correct != 'y') and (correct != 'n'):
	correct = input('\nIs this correct? y/n: ')
if correct == 'y':
	try:
		get_temps(city, state)
	except:
		print('Oops! Invalid city or state')
		
if correct == 'n': 
	try:
		city = input('Please input city: ')
		state = input('Please input state initials: ')
		get_temps(city.replace(' ', '_'), state)
	except:
		#r3 = requests.get('http://autocomplete.wunderground.com/aq?query=%s+%s' % (city, state))
		print('\nOops! Invalid city or state')