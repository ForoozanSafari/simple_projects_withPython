mlS = [0]
mlO = [0]

while True :
    q = input('if you want to take a bread => "bread" * and if you want to leave the row => "leave"')
    
    if q.lower() == 'bread':
        x = input('which servive U want?(only one or several)')
        if x.lower() == 'several' :
            print ('please take a number : ')
            a = input('please enter your name : ')
            if a in mlS :
                print('you are already on the row and your number is : ',mlS.index(a))
            else :
                mlS.append(a)
                print('you are the ',mlS.index(a),'person on the "several bread" row')
        else :
            if x.lower() == 'only one' :
                print('when you want only one bread, you dont have to stay in the "several bread row" \
but you have to stay in "only one bread row" . please take a number :')
                z = input('please enter your name :')
                if z in mlO :
                    print('you are already on the row and your number is : ',mlO.index(z))
                else :
                    mlO.append(z)
                    print('you are the ',mlO.index(z),'person on the "only one bread" row')
    else :
            m = input('what row you where in ? (several or only one) ')
            if m.lower() == 'several':
                f = input('please enter your name :')
                if f in mlS :
                    mlS.remove(f)
                    print('dear', f, 'your name removed succesfuly')
                else :
                    print(f,'you werent in the several row with this name')
            else :
                v = input('please enter your name :')
                if v in mlO :
                    mlO.remove(v)
                    print('dear', v, 'your name removed successfuly')  
                else :
                    print(v,'you werent in the only one row with this name')
                
            
            
                
