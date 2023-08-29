for i in range(1):
    print(' '*(10-i),'✯', end='')

for i in range(3):
    print(' '*(10-i),'*'*(i),'*'*(i), end='')
    
for i in range(5):  
    print(' '*(10-i),'*'*(i),'*'*(i), end='')

for i in range(8):  
    print(' '*(10-i),'*'*(i),'*'*(i))
for i in range (3):

     print(' '*(9),'|@|')


#----------------------------------------

n=10
for i in range(n//2 , n, 2):
    for j in range (1 ,n-i , 2):
        print(' ',end='')
    for j in range(1,i+1,1):
        print('*', end='')
    for j in range ( 1 , n-i+1 , 1):
        print(' ', end='')
    for j in range (1,i+1,1):
        print('*', end='')
    print()
for i in range(n,0,-1):
    for j in range(i,n,1):
        print(' ', end='')
    for j in range(1,i*2,1):
        print('*',end='')
    print()
