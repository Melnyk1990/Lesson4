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

print('*' * 10, 'TASK 2', 10 * '*')

symbol = ''

userPush = input('Enter line: ')
search = input('Enter character to search string: ')

for i in userPush:
    if i.count(search):
        symbol +=i
print(f'Quantity symbols {search} in line: ', len(symbol))