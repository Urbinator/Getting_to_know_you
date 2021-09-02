from datetime import datetime
date_format = '%m/%d/%Y'
today = datetime.today().strftime('%m/%d/%Y')
student = input('What\'s your name?')
bcn = input('Are you in Barcelona? (please answer with yes or no)')

if bcn == 'yes':
	arrival = input('What day did you arrive in Barcelona? (please answer as mm/dd/yyyy)')
	first_date  = datetime.strptime(arrival, date_format)
	sec_date = datetime.strptime(today, date_format)
	diff = sec_date - first_date
	diff = diff.days
	print(diff)
print('Please check the output file for the response')


with open('student_arrival.txt', 'a') as file:
	if bcn == 'yes':
		if diff >=100:
			print(f'Hi {student}, welcome to the program', file=file)
			print('Are you from Barcelona?', file=file)
		elif (diff>7) and (diff<100):
			print(f'Hi {student}, welcome to Barcelona. We hope you like the city so far', file=file)
		else:
			print(f'Welcome to Barcelona, {student}. We hope you are enjoying the first few days.', file=file)
	else:
		print('We hope to see you soon', file = file)	

