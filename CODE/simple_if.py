#1
# To print the squre of a number only if it is even

n = int(input('enter number'))
if(n %2 == 0):
    print(n*n)


#2
# to check whethere the char is vowel or not

ch = input('enter character')
if ch in 'aeiouAEIOU':
    print(f'{ch} is a vowel')


#3
#to print  ascii value of a character only if it is upper case

ch = input('enter char')
if ch.isupper():
    print(ord(ch))

# another
#to print  ascii value of a character only if it is upper case

ch = input('enter char')
if 'A' <= ch <= 'Z':
    print(ord(ch))


#4
# Wap to print the cube of a number only if it is divisible by 9 or 6.

n = int(input('enter number: '))
if (n%9 == 0) or (n%6 == 0):
    print(f'cube of number {n} is {n**3}')


#5
# Wap to check whether the given integer is 3 Digit number

n = input('enter no: ')
if len(n) == 3:
    print(f'entered number {n} is a 3 digit number. ')

#another
# to check whether the given no is 3 digit or not

n = int(input('enter no'))

if(n >= 100 and n <= 999) or (n >= -100 and n <= -999):
    print('yes it is 3 digit')

#6
# Wap to check whether the last digit of a given number is 5.

n = int(input('enter no: '))
if n%10 == 5:
    print(f'entered number {n} has last digit 5.')



#7
# Wap to check whether the given data is float.

n = eval(input('enter number: '))

if type(n)== float:
    print('given data is float.')

else:
    print('given data is not float.')


#8

# Wap to check whether the data is single value data.

n = eval(input('enter the value: '))

if type(n) in (list,tuple,set,str,dict):
    print('not a single value data.')
else:
    print('single value data.')









