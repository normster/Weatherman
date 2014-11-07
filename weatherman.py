import json
import requests

print('Finding location from IP address')

def get_temps(city, state):
	#send request with corrected args
	r2 = requests.get('http://api.wunderground.com/api/78c2f37e6d924b1b/hourly/q/%s/%s.json' % (state, city))
	forecast = json.loads(r2.text)
	windy = []
	
	for x in range(0, 12):
		civil = forecast['hourly_forecast'][x]['FCTTIME']['civil']
		wspd = int(forecast['hourly_forecast'][x]['wspd']['english'])
		if wspd >= 10:
			windy.append(civil)
		print('%8s  ' % civil, end = "")

	print('\n')
	for x in range(0, 12):
		temp = int(forecast['hourly_forecast'][x]['temp']['english'])
		print('  %3s°F   ' % temp, end = '')
		
	print('\n')
	for x in range(0, 12):
		feelslike = int(forecast['hourly_forecast'][x]['feelslike']['english'])
		print('  %3s°F   ' % feelslike, end = '')
	
	print('\n\nRow 1: Time\nRow 2: Actual temperature\nRow 3: Adjusted temperature (for wind chill)')
	if len(windy) > 0:
		print('\nIt sure is windy today! Higher than 10 mph winds today at: ', windy)
	
	print('\n')	
	
#use wundergound geolookup api
r1 = requests.get('http://api.wunderground.com/api/78c2f37e6d924b1b/geolookup/q/autoip.json')
location = json.loads(r1.text)
state = location['location']['state']
city = location['location']['city']

#make sure geo is correct
print('%s, %s' % (city, state))
correct = ''

while (correct != 'y') and (correct != 'n'):
	correct = input('\nIs this correct? y/n: ')
if correct == 'y':
	try:
		print('\nHere\'s how the next 12 hours look!\n\n')
		get_temps(city, state)
	except:
		print('Oops! Invalid city or state')
		
if correct == 'n': 
	try:
		city = input('Please input city: ')
		state = input('Please input state initials: ')
		print('\nHere\'s how the next 12 hours look!\n\n')
		get_temps(city.replace(' ', '_'), state)
	except:
		print('\nOops! Invalid city or state')