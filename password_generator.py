import sys
import random
import string

def joiner(x):
	return (''.join(x))

def password_generator(x=14):
	
		lengthList = []
		i = 0	
		x = int(x)
		while i < (x):
			lengthList.extend(random.choice(string.ascii_lowercase))
			i += 1
			if i == (x):
				break
			lengthList.append(random.choice(string.ascii_uppercase))
			i += 1
			if i == (x):
				break
			lengthList.append(random.choice(string.punctuation))
			i += 1
			if i == (x):
				break
			lengthList.append(random.choice(string.digits))
			i += 1
		pw3 = joiner(lengthList)
		return (pw3)