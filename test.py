dictionary = {}
dictionary = \
{
    'up': '↑',
    'left': '←',
    'down': '↓',
    'right': '→'
}

print (dictionary)
print(dictionary['left'])
print(dictionary['up'])
print(dictionary['down'])
print(dictionary['right'])

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))