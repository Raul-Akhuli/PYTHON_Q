#21
# Wap to check whether the char is uppercase, lowercase, digit or special char.

ch = input('enter character: ')

if ch.isupper():
    print('entered char is in uppercase.')
elif ch.islower():
    print('entered char is in lowercase.')
elif ch.isdigit():
    print('entered char is in digit.')
else:
    print('entered char is special character.')



#22
# Wap to check whether the given integer is single digit or two digits or three
#digits or more than three digits.

n = int(input('enter no: '))

if 0<= n <= 9:
    print('single digit')
elif 10<= n <= 99:
    print('two digit')
elif 100<= n <= 999:
    print('three digit')
else:
    print('more than three digit')




#23
# Wap to check the given points are lying in which quadrant.

a = int(input('enter one number: '))
b = int(input('enter another number: '))

if a>0 and b>0:
    print('they are in first quadrant')
elif a<0 and b>0:
    print('they are in second quadrant')
elif a<0 and b<0:
    print('they are in third quadrant')
else:
    print('they are in fourth quadrant')


#24
# Wap to find the greatest of 3 numbers.

a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = int(input('enter third number: '))

if a>b and a>c:
    print(f'{a} number is greater.')
elif a<b and c<b:
    print(f'{b} number is greater.')
elif c>a and c>b:
    print(f'{c} number is greater.')
else:
    print('invalid!!!')


#25
# Wap to find the smallest of 3 numbers..

a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = int(input('enter third number: '))

if a<b and a<c:
    print(f'{a} number is smaller.')
elif a>b and c>b:
    print(f'{b} number is smaller.')
elif c<a and c<b:
    print(f'{c} number is smaller.')
else:
    print('invalid!!!')


#26
# Wap to check the relation between two integer numbers.

a = int(input('enter first number: '))
b = int(input('enter second number: '))


if a>b:
    print(f'{a} number is greater.')
elif b>a:
    print(f'{b} number is greater.')
else:
    print('they are equal.')

#27
# Consider a character input if it is uppercase convert it into lowercase, if it is
#lowercase convert it into uppercase, if it is digit print the reminder when it is
#divided by 3 else if it is special character print it’s ASCII value


ch = input('enter character: ')

if ch.isupper():
    print(ch.lower())
elif ch.islower():
    print(ch.upper())
elif ch.isdigit():
    a= int(ch)
    print(a%3)
else:
    print(id(ch))


#another
a= input('enter no: ')

if 'A' <= a <= 'Z':
    print(chr(ord(a)+32))
elif 'a' <= a <= 'z':
    print(chr(ord(a)-32))
elif '0' <= a <= '9':
    print(int(a)%3)
else:
    print(ord(a))

#28
# Wap to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the
#given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of
#both 3 and 5.

n= int(input('enter no: '))

if n%5 == 0 and n%3 == 0:
    print('Fizzbuzz')
elif n%3 == 0:
    print('Fizz')
elif n%5 == 0:
    print('buzz')
else:
    print('Invalid!!!')


