print('*' * 10, 'TASK 1', 10 * '*')

letters = ''
numbers = ''

userPush = input('Enter a line from the keyboard: ')

for i in userPush:
    if i.isalpha():
        letters += i
    elif i.isdigit():
        numbers += i
print('Number of letters per line: ', len(letters))
print('Number of digits per line: ', len(numbers))

##################################################################

print('*' * 10, 'TASK 2', 10 * '*')

symbol = ''

userPush = input('Enter line: ')
search = input('Enter character to search string: ')

for i in userPush:
    if i.count(search):
        symbol +=i
print(f'Quantity symbols {search} in line: ', len(symbol))

##############################################################################


print('*' * 10, 'TASK 3', 10 * '*')

userPush = input('Enter line: ')
search = input('Enter a search word: ')
replacement = input('Enter a replacement word: ')

new = userPush.replace(search, replacement)
print('New line: ', new)

#######################################################################################

print('*' * 10, 'TASK 4', 10 * '*')

userPush = input('Enter line: ')

print('1) Third character of the line: ', userPush[2])
print('2) Penultimate character of the line: ', userPush[-2])
print('3) First five (5) characters of the line: ', userPush[0:5])
print('4) The entire line except the last two characters: ', userPush[0:-2])
print('5) All symbols with paired indices: ', userPush[ : : 2])
print('6) All characters with unpaired indices: ', userPush[1: :3])
print('7) Print all characters in reverse order: ', userPush[: :-1])
print('8) Print characters in reverse order one after another: ', userPush[ : :-2])
print('9) Length of the eighth (8) line : ', len(userPush[ : :-2]))
