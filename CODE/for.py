#1
# a = 'hello'

# for i in a:
#     print(i,end=' ')

#________________________________________________________

#2
# a = [10,20,30,40]
# for i in a:
#     print(i)

#_________________________________________________________

#3
#dict

# a = {'D':'Dance','C':'Couple','S':'Subhamoy'}

# for i in a:
#     print(i+ ':' +a[i])

#___________________________________________________________________

#4
# wap to remove duplicate from a list without using typecasting

# a = [1,2,3,1,2,3,4,5,6]
# out = [1,2,3,4,5,6]



# a = [1,2,3,1,2,3,4,5,6]
# out = []
# for i in a:
#     if i not in out:
#         out += [i]

# print(out)


#________________________________________________

#5
# a = 'Happy Hallowen'
# out = 'aaoe'


# a = 'Happy Hallowen'
# out = ''
# for i in a:
#     if i in 'aeiouAEIOU':
#         out += i

# print(out)

#___________________________________________________

#6
# a = [1,2,3,1,2,3,4,5,6]


# for i in range(len(a)):
#     j = i+1
#     while j < len(a):          # if you use for syntax should 'for j in range(len(a)-1)'
#         if a[i] == a[j]:
#             a.pop(j)
#         j+=1

# print(a)

#___________________________________
#7
#write a program to reverse a string without using any slicing
# a = input('enter string: ')
# out = ''

# for i in a:
#     out = i+out
# print(out)


#another
# a = 'hello'

# for i in range(len(a)-1,-1,-1):
#     print(a[i],end='')

#___________________________________

# S='power star'
# out = {'power':5,'star':4}
# dict = {}
# for i in S.split():
#     dict[i] = len(i)

# print(dict)
#/
# without split method.
# dict = {}
# word = ''

# for i in S:
#     if i != ' ':
#         word += i
#     else:
#         dict[word] = len(word)
#         word = ''
    
# dict[word] = len(word)

# print(dict)

#___________________________________

# S = input('enter string: ')
# dict = {}
# for i in S.split():
#     dict[i] = i[::-1]

# print(dict)


# without split.
# S = input('enter string: ')
# dict = {}
# word = ''

# for i in S:
#     if i != ' ':
#         word += i
#     else:
#         dict[word] = word[::-1]
#         word = ''
    
# dict[word] = word[::-1]

# print(dict)


# without slicing.

# S = input('enter string: ')
# dict = {}
# word = ''
# reverse = ''

# for i in S:
#     if i != ' ':
#         word += i
#         reverse = i+reverse
#     else:
#         dict[word] = reverse
#         word = ''
#         reverse = ''
    
# dict[word] = reverse

# print(dict)

#________________________________________

# S = 'always keep smiling'
# output = 'syawla peek gnilims'

# st = input('enter string: ')
# output = ''
# word = ''
# for i in st:
#     if i != ' ':
#         word = i+word
#     else:
#         output += word
#         word = ''
#         output +=' '

# output += word
# print(output.strip())   # strip is used to remove unwanted space from starting or ending.


#___________________________________



# Wap to get the following output.
# S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
# Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’], ’org’:[‘www’]}

#site = ['jiocinema.com','file.py','web.html','amazom.com','www.org','python.py']
# out = {}

# site = eval(input('enter collection: '))

# for i in site:
#     a = i.split('.')   #['jiocineam', com]
#     if a[-1] not in out:
#         out[a[-1]] = [a[0]]     #same key override the previous one.
#     else:
#         out[a[-1]] += [a[0]]

# print(out)


#_______________________________________________________

