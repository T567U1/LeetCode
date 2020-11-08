
c = 1
word = input('Please enter the next word: ')
if (word != 'STOP'):
    print('#' + str(c) + ': You entered ' + word)

if (word == 'STOP'):
    c = 0

word = input('Please enter the next word: ')
if (word != 'STOP'):
    c = c + 1

while (word != 'STOP'):
    print('#' + str(c) + ': You entered ' + word)
    word = input('Please enter the next word: ')
    c = c + 1

if (word == 'STOP'):
    c = c - 1

print('All done. ' + str(c) + ' words entered.')
