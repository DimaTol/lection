



with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
    data.write('Вот еще третья строчка 3\n')


colors = ['а теперь добавляем это']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()


path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+



