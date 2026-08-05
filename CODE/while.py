
# a = [10,23,25,16,18,19]
# o/p = [10,16,18]


a = [10,23,25,16,18,19]
out = []
i = 0
while i < len(a):
    if a[i]% 2 == 0:
        out.append(a[i])    #
    i+=1;
print(out)



#

a = "happy Grilfriend's Day"

out = ''
i = 0
while i < len(a):
    if a[i] in 'aeiouAEIOU':
        out += a[i]
    i+=1
print(out)
        


# 39.Wap to print python for 5 times.

i = 0

while i <6:
    print('python')
    i += 1


# 40.Wap to print n natural numbers.

n = int(input('enter no: '))

i = 1

while i <= n:
    print(i, end=' ')
    i += 1


# 41.Wap to print multiplication table for n.

n = int(input('enter no: '))

i = 1

while i <= 10:
    print(n*i)
    i += 1


# 42.Wap to find the sum of n natural numbers.

n = int(input('enter no: '))

i = 0
add = 0

while i <= n:
    add += i
    i += 1

print(add)



# 43. Wap to find the product of n natural numbers or factorial of a number.

num = int(input('enter no: '))

i = 1
fact = 1

while i <= num:
    fact *= i
    i += 1
print(fact)



# 44.Wap to print all the characters of a string.

st = input('enter string: ')

i = 0

while i < len(st):
    print(st[i], end = ' ')
    i += 1



# 45.Wap to print all the characters present at even index of a string.

st = input('enter string: ')

i = 0

while i < len(st):
    if i%2 == 0:
        print(st[i], end = ' ')
    i += 1



