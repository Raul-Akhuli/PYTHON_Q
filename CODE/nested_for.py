# Wap to get the following output.
# S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
# Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’], ’org’:[‘www’]}



# without split
# out = {}

# site = eval(input('enter collection: '))
# val = ''

# for i in site:
#     key = ''
#     for j in i:
#         if j != '.':
#             key += j      #jiocinema  but in the second iteration key is present.
#         else:
#             val = key
#             key = ''
#     if key not in out:
#         out[key] = [val]  # convert this val into string format in order to as per the output.
#     else:
#         out[key] += [val]  # we can't concat with the string so need to convert into the list.

# print(out)




