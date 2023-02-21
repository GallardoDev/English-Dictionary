import json
from difflib import get_close_matches
from translate import Translator

data = json.load(open('data.json'))
translator = Translator(from_lang='en', to_lang='es')

def translateFunction(word):
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input('Did tou mean %s instead? "Y" for yes or "N" for no: ' % get_close_matches(word, data.keys())[0]).lower()
		if yn == 'y':
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == 'n':
			return 'This word doesn`t exist'
		else:
			return 'Wrong letter...'
	else:
		return 'The word doesn`t exist'

word = input('Enter word: ').lower()
output = translateFunction(word)

if type(output) == list:
	for item in output:
		print('+ ',item)
else:
	print(output)

print('\n===================================\n')
trans = input('Do you want to translate it? "Y" or "N": ').lower()
try:
	if trans == 'y':
		tr = translator.translate(str(data[word])).split(',')
		for item in tr:
			print('+', item)
	elif trans == 'n':
		pass
	else:
		print('Wrong letter...')
except Exception as e:
	print('Error: ', e)