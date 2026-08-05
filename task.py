s = eval(input('enter a collection: '))
out = {}
word = ''
reverse = ''
even_pas = ''
count = 0
idx = 0

for i in s:
    for j in i:
        if j != ' ':
            word += j
            reverse = j + reverse
            if j in 'aeiouAEIOU':
                count += 1
            if idx %2 == 0:
                even_pas += j
                idx += 1
        else:
            out[word] = [reverse, count, even_pas]
            reverse = even_pas = word = ''
            count = idx = 0
    out[word] = [reverse, count, even_pas]
    reverse = even_pas = word = ''
    count = idx = 0
    
print(out)
