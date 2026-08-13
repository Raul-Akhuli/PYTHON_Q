# n = int(input('enter row: '))
# m = int(input('enter column: '))

# mid = n//2 +1

# for i in range (1, n+1):
#     for j in range(1, m+1):
#         if i+j >= mid+1 and j-i <= mid-1 and i-j <= mid-1 and i+j <= n+mid:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print()

# i+j >= mid+1 and j-i <= mid-1 and i-j <= mid-1 and i+j <= n+mid


n = int(input('enter row: '))
m = int(input('enter column: '))

mid = n//2 +1

for i in range (1, n+1):
    for j in range(1, m+1):
        if i+j >= mid+1 and j-i <= mid-1 and i-j <= mid-1 and i+j <= n+mid:
            print(i,j,end='')
        else:
            print(' ', end='')
    print()