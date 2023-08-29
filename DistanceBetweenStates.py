state_name = ['abadan','arak','ardebil']
distance = [[0 ,704 ,1401],
           [704 ,0 ,843],
           [1401 ,843 ,0]]

x = input('from where ? ')
y = input('to where ? ')

i = state_name.index(x)
j = state_name.index(y)

if i == j :
    print('no distance')
elif i < j:
    m = distance[i][i+j]
else :
    m = distance[i][j]
    
print('distance from',x,'to',y,'is',m)
