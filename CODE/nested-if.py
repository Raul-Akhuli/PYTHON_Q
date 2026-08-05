
# 29 Wap to login into the Instagram with valid username and password.(enter
#password only if the user name is valid)

username = 'akhuli'
password = 'akhuli@1234'

ch = input('enter username: ')

if ch == username:
    passw = input('enter password: ')
    if passw == password:
        print('login successfully.')
    else:
        print('enter valid password.\nlogin failed!!!')
else:
    print('Invalid username!!!')




# 30 wap to print the middle value of a list only if it is string.

col = eval(input('enter the collection: '))

middle_value = col[int(len(col)/2)]

if type(col) == list:
    if len(col)%2 != 0:
        if type(middle_value) == str:
            print(f'middle value is {middle_value}')
        else:
            print('entered collection is list but middle element is not string.')
    else:
        print("entered collection is list but does't have any middle value")
else:
    print('enter collection is not list.')


# 31 Wap to check whether the character is vowel or consonant.

char = input('enter the char: ')

if 'A'<= char >='Z' or 'a'<= char>='z':
    if char in 'aeiouAEIOU':
        print('entered character is vowel.')
    else:
        print('entered character is consonant.')
else:
    print('Invalid input!!!')


# 32.Wap to find the greatest of 4 numbers.

a = int(input('enter first no: '))
b = int(input('enter second no: '))
c = int(input('enter third no: '))
d = int(input('enter fourth no: '))

if a>b:
    if a>c:
        if a>d:
            print(f'{a} is greater.')
if b>a:
    if b>c:
        if c>d:
            print(f'{b} is greater.')

if c>b:
    if c>a:
        if c>d:
            print(f'{c} is greater.')

else:
    print(f'{d} is greater')





