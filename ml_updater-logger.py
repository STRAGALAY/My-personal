# file = open('new.txt', 'r')
# print(file.read())

file = open('data.json', 'r')
text = file.read()
print(text)

import json
print(json.loads(text))
