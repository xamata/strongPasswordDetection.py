# strongPasswordDetection.py
'''
Write a function that uses regex to valid the password it is passed is strong.
Strong password: 
	-at least 8 characters long
	-contains BOTH uppercase and lowercase characters
	-at least 1 digit
--------GAMEPLAN-----------
1. create a function that passes a password through it
2. pass the password through a validator
3. if cannot pass through validator, function returns false

1. import re
2. create a function that passes a password through it
3. seperate the different regex for the future checks
	a. regexNumbers = one for 8 characters long [a-zA-Z0-9]
	b. regexLower = one for lower case letter [a-z]
	c. regexUpper = one for upper case letter[A-Z]
	c. regexDigit = one for one digit \d
3. create a validator:
	a. if regexNumbers len(group)<0 , valid is false
	b. if regexLower len(group)<0, valid is false
	c. if regexUpper len(group)<0, valid is false
	c. if regexDigit len(group)<0, valid is false
4. if valid is still true, return true. Meaning, password strength is good
'''
import re

def strongPassword(password):
	regexNumber = re.compile(r'[a-zA-Z0-9]+')
	regexUpper = re.compile(r'[A-Z]+')
	regexLower = re.compile(r'[a-z]+')
	regexDigit = re.compile(r'\d+')

	numberCheck = regexNumber.search(password)
	numberUpper = regexUpper.search(password)
	numberLower = regexLower.search(password)
	numberDigit = regexDigit.search(password)

	try:
		if len(numberCheck.group(0))>0 and len(numberUpper.group(0))>0 and len(numberLower.group(0))>0 and len(numberDigit.group(0))>0:
			print("Your password is strong enough.")
	except:
		print('Your password is not strong enough.')


password = 'dhaomdfasdS9'
strongPassword(password)