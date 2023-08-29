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

#-----------------------------------------
def table():
    print('-'*120)
    print('| x\t|\t','y\t|\t','and x \t|\t','or x\t|\t', 'not x\t|\t','and y \t|\t','or y\t|\t', 'not y\t|\t' )
    print('-'*120)
    print('| T\t|\t','T\t|\t',' T\t|\t',' T\t|\t', ' F\t|\t',' T\t|\t',' T\t|\t', ' F\t|\t' )
    print('-'*120)
    print('| T\t|\t','F\t|\t',' F\t|\t',' T\t|\t', ' F\t|\t',' T\t|\t',' F\t|\t', ' F\t|\t' )
    print('-'*120)
    print('| F\t|\t','T\t|\t',' F\t|\t',' T\t|\t', ' T\t|\t',' F\t|\t',' T\t|\t', ' F\t|\t' )
    print('-'*120)
    print('| F\t|\t','F\t|\t',' F\t|\t',' F\t|\t', ' T\t|\t',' F\t|\t',' F\t|\t', ' T\t|\t' )
    print('-'*120)

table()

#----------------------------------------
def table():
    print('enter "true" value as = 1 \nand \nenter "false" value as = 0')
    x=int(input('enter "x" value : '))
    y=int(input('enter "y" value : '))
    if x == 1 and y == 1 :
        print('-'*120)
        print('| x\t|\t','y\t|\t','and x \t|\t','or x\t|\t', 'not x\t|\t','and y \t|\t','or y\t|\t', 'not y\t|\t' )
        print('-'*120)
        print('| T\t|\t','T\t|\t',' T\t|\t',' T\t|\t', ' F\t|\t',' T\t|\t',' T\t|\t', ' F\t|\t' )
        print('-'*120)
    elif x == 1 and y == 0 :
        print('-'*120)
        print('| x\t|\t','y\t|\t','and x \t|\t','or x\t|\t', 'not x\t|\t','and y \t|\t','or y\t|\t', 'not y\t|\t' )
        print('-'*120)
        print('| T\t|\t','F\t|\t',' F\t|\t',' T\t|\t', ' F\t|\t',' T\t|\t',' F\t|\t', ' F\t|\t' )
        print('-'*120)
    elif x == 0 and y == 1 :
        print('-'*120)
        print('| x\t|\t','y\t|\t','and x \t|\t','or x\t|\t', 'not x\t|\t','and y \t|\t','or y\t|\t', 'not y\t|\t' )
        print('-'*120)
        print('| F\t|\t','T\t|\t',' F\t|\t',' T\t|\t', ' T\t|\t',' F\t|\t',' T\t|\t', ' F\t|\t' )
        print('-'*120)
    elif x == 0 and y == 0 :
        print('-'*120)
        print('| x\t|\t','y\t|\t','and x \t|\t','or x\t|\t', 'not x\t|\t','and y \t|\t','or y\t|\t', 'not y\t|\t' )
        print('-'*120)    
        print('| F\t|\t','F\t|\t',' F\t|\t',' F\t|\t', ' T\t|\t',' F\t|\t',' F\t|\t', ' T\t|\t' )
        print('-'*120)        
        
    table()
