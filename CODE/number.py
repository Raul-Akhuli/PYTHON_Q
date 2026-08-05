# palindrome number

num = int(input('enter number: ')) # 121
out = 0
temp = num #121

st = str(num) # '121'

while num > 0: # 121>0
    digit = num%10 # 121%10 = 1
    out = digit + out*10
    num = num//10
if out == temp:
    print('palindrome number')

else:
    print('not palindrome number')
    



# armstrong number

num = int(input('enter number: ')) # 121
out = 0
temp = num #121

st = str(num) # '121'

while num > 0: # 121>0
    digit = num%10 # 121%10 = 1
    out = out + digit**len(st) # 0+1^3 = 1
    num = num//10 # 121//10 = 12
if out == temp:
    print('armstrong number')

else:
    print('not armstrong number')
    



# prime number need to check


num = int(input('enter number: '))
i = 3

if num <= 1:
    print('not prime')
if num == 2:
    print('prime')
if num%2 == 0:
    print('not prime')
else:
    while i*i <= num:
        if num %i == 0:
            print('not prime')

    print('prime')
    i += 2

            
# xylem number
1234
1+4 == 3+2


# xylem number
##1234
##1+4 == 3+2

num = int(input('enter a number: '))
st = str(num)
n = len(st)

sum1 = 0
sum2 = 0

if n > 3:
    while num >0:
        digit = num%10
        
        if n == 1 or n == len(st):    
            sum1 += digit
        else:
            sum2 += digit
            
        num = num//10

        n -= 1

    if sum1 == sum2:
        print('xylem number.')
    else:
        print('not a xylem number.')
else:
    print('not a xylem number.')

# another
# # perfect number
##6
##1+2+3 = 6

num = int(input('enter number: '))
ld = num%10

num = num//10

avg = 0

while num > 0:
    rem = num%10
    avg += rem
    num = num//10

if avg-rem == ld+rem:
    print('xylem')
else:
    print('not xylem')

        
            
        
    

        
            
        
    


# perfect number
6
1*2*3 = 6
1+2+3 = 6

# # perfect number
##6
##1+2+3 = 6

num = int(input('enter number: '))
add = 0
i = 1

while i <= (num/2 +1):
    if num%i == 0:
        add += i
    i += 1

if add == num:
    print('perfect number.')
else:
    print('not a perfect number.')



# # perfect number
##6
##1+2+3 = 6

num = int(input('enter number: '))
ad = 0
st = {num}

while num != 1:
    while num>0:
        rem = num%10
        ad += rem **2
        num = num//10
    if ad in st:
        print('not happy no.')
        break

    if ad!= 1:
        num = ad
        st.add(ad)
    
    num = ad
    ad = 0
if num == 1:
    print('happy no.')
    




# moves zeros to end

# # moves zeros to end

col = eval(input('enter collection: '))
count = 0
i = 0

while i < len(col):
    if col[i] != 0:
        col[count] = col[i] # you should assign as index count not i
        count +=1
    i+=1
while count < len(col):
    col[count] = 0
    count+=1

print(col)
