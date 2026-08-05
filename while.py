'''
#Q100.Write a program to print ‘Thank you’ for n times
a=input('Enter String : ')
n=int(input('Enter how many Times : '))
i=0
while i < n:
    print(a)
    i+=1

#Q99.Write a program for number game 
actual_number=111001
num=int(input('Enter number: '))  
while num!=actual_number:
    num=int(input('Enter number : '))
print(f"{num} matches with {actual_number}")      

#Q98.Write a program to reverse the given list
a=eval(input('Enter data: '))
i=0
res=[]
while i < len(a):
    res.insert(0,a[i])
    i+=1
print(res)    

#Q97.Write a program to get the following output - 
# Input='hai hello how are you' 
# output='hai**hello**how**are**you'
a=input('Enter string : ')
out=''
i=0
while i < len(a):
    if a[i]!= ' ':
      print(a[i],end='') 
    
    else:
       print('**',end='')
    i+=1

#Q96.Write a  program to extract all the non default values from the list
a=eval(input('Enter data: '))
i=0
b=[]
c=[]
while i < len(a):
    if a[i] != []:
        b.append(a[i])
    else:
        c.append(a[i])
    i+=1    
print(b) 

#Q95.Write a program to extract all integer data items from tuple
a=eval(input('Enter data: '))
i=0
while i < len(a):
    if type(a[i]) != int:
        print(a[i],end=' ')
    i +=1    

#Q94.Write a program to whether the entered username  and password is correct or not if not correct print enter again 
actual_un='DIYA11'
actual_pw='DIYE'
un=input('Enter username: ')
pw=input('Enter password: ')
while un!=actual_un and pw!=actual_pw:
    un=input('Enter username: ')
    pw=input('Enter password: ')
print('login successfully')

#Q93:Write a program to find length of collection without using len function 
a=eval(input('Enter data: '))
i=0
count=0
while i < len(a):
    count+=1
    i+=1
print(count)                   

#Q92. Write a program to return the positions of vowels present in the given string 
a=input('Enter data: ')
i=0
while i < len(a):
    if a[i] in 'aeiouAEIOU':
        print(i,end=' ')
    i+=1

#Q91.Write a program to check weather the given collection is having nested collection or not 
a=eval(input('Enter data: '))
i=0
count=0
while i < len(a):
    if type(a[i])==list or type(a[i])==tuple or type(a[i])==set or type(a[i])==dict:
        count+=1
    i+=1 
print(f'Yes {count} times')       

#Q90.Write a program to check weather the given tuple is palindrome or not
a=eval(input('Enter data: '))
i=0
og=a
b=list(a)
out=[]
while i < len(a):
    out.insert(0,a[i])
    i+=1
res=tuple(out)    
if res==og:
    print('palindrome')
else:
    print('Not - Palindrome')        

#Q89.Write a program to check the type of data entered by the users 
a=eval(input('Enter data: '))
i=0
while i < len(a):
    if type(a[i])==int:
        print('int')
    elif type(a[i])==float:
        print('float')
    elif type(a[i])==complex:
        print('complex')
    elif type(a[i])==list:
        print('list')
    elif type(a[i])==tuple:
        print('tuple')
    elif type(a[i])==set:
        print('set')
    elif type(a[i])==dict:
        print('dict')
    else:
        print('Invalid')                            
    i+=1

#Q88.Write a program to count number of consonants in the given string s=input('enter the str:')
a="s=input('enter the str:')"
count=0
i=0
while i < len(a):
    if a[i] in 'aeiouAEIOU':
        count+=1
    i+=1    
print(f'the {count} number of vowels present in this statement')        
'''
#Q87.Write a program to find the length of the longest word
a=eval(input('Enter data'))
i=0
while i < len(a):
    



            