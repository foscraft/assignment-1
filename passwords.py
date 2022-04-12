import string
import random

'''
password generator function in Python
'''

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate__password():

	random.shuffle(characters)
	password = [random.choice(characters) for _ in range(10)]
	random.shuffle(password)
	return "".join(password)



## invoking the function
print(generate__password())