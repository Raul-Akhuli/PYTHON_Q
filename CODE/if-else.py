#11
# Wap to check whether the data is mutable or not.

col = eval(input('enter collection: '))

if type(col) in (str,tuple):
    print('entered collection is Immutable.')

else:
    print('entered collection is Mutable.')



#12
# Wap to check whether the given character is digit or not.

ch = eval(input('enter anything: '))

if type(ch) in (int,float):
    print('entered character is a digit')

else:
    print('entered character is not a digit')


#13
# Wap to check whether the given character is special or not.

ch = eval(input('enter character: '))

if 'A' <= ch >= 'Z' or 'a' <= ch >= 'z' or '0' <= ch >= '9':
    print(f'entered character {ch} is not a special character.')

else:
    print(f'entered character {ch} is a special character.')


#14
# Wap to check whether a list consists of middle value or not.

col = eval(input('enter collection: '))

if len(col)%2 == 0:
    print(f"entered collection {col} does't have a middle value. ")

else:
    print(f"entered collection {col} contain a middle value. ")


#15
# Wap to check whether the number is even or odd.

n = int(input('enter no: '))

if n%2 == 0:
    print(f'entered number {n} is even.')

else:
    print(f'entered number {n} is odd.')


#16
# Wap to check whether the given data is mutable or immutable

n = eval(input('enter the data'))

if type(n) in (str,tuple,int,float,complex,bool):
    print(f'entered data {n} is Immutable')
else:
    print(f'entered data {n} is Mutable')


#17
# Wap to check whether 2 values are pointing to the same memory or not.

a = eval(input('enter first value: '))
b = eval(input('enter second value: '))


if id(a) == id(b):  #a is b
    print('2 values are pointing to the same memory')
else:
    print('2 values are not pointing to the same memory')



#18
# Consider a tuple of length 2 and check whether the tuple is homogenous or not.

col = eval(input('enter collection of length 2: '))

if(type(col[0]) == type(col[1])):
    print('tuple is homogenous')
else:
    print('tuple is not homogenous')


#19
# Wap to check whether the string is palindrome or not.

str = input('enter string: ')

if str == str[::-1]:
    print('string is palindrome')
else:
    print('string is not palindrome')


#20
# Wap to check whether the number is positive or negative.

n = eval(input('enter number: '))

if n>0:
    print('number is positive')

else:
    print('number is negative')
