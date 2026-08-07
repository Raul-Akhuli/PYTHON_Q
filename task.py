# 117
# Wap to get the following output
# In=[100,200,50,400,300]
# N=300
# Out=[[100,200],[300]]


col = eval(input('enter collection: '))
n = int(input('enter number: '))
num = set()
out = []
for i in col:
    rem = n - i
    if i not in num:
        if rem in col:
            num.add(i)
            num.add(rem)
            out.append(list(num))
            out.append(n)

print(out)

