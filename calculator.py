print('ask five questions:')
h=[]
for i in range(1,6):
    print('question',i,':')
    a=float(input('enter number i:'))
    opr=input('operation:(+/-/x/div/%/rem/(q) to quit):')
    if opr=='q':
        print('knew you couldnt do math dumbo :p bye')
        result='quit'
        h.append(f'{result}')
        break
    elif opr not in ['+','-','x','div','%','rem']:
        print('error: invalid operation')
        continue
    else:
        b=float(input('enter number ii:'))
# return input('operation:(+/-/x/div/%):')

    if opr=='+':
        result=a+b
        h.append(f'{a} {opr} {b} = {result}')
        print(a+b)
    elif opr=='-':
        print(a-b)
        result=a-b
        h.append(f'{a} {opr} {b} = {result}')
    elif opr=='x':
        print(a*b)
        result=a*b
        h.append(f'{a} {opr} {b} = {result}')
    elif opr=='div':
        if b==0:
            print('ERROR!!! YOU CANT DIVIDE A NUMBER BY ZERO DUMBASS')
            result='error'
            h.append(f'{a} {opr} {b} = {result}')
        else:
            print(a/b)
            result=(a/b)
            h.append(f'{a} {opr} {b} = {result}')
    elif opr=='%':
        print((a/100)*b)
        result=(a/100)*b
        h.append(f'{a} {opr} {b} = {result}')
    elif opr=='rem':
        if b==0:
            print('ERROR!!! YOU CANT DIVIDE A NUMBER BY ZERO DUMBASS')
            result='error'
            h.append(f'{a} {opr} {b} = {result}')
        else:
            print(a%b)
            result=a%b
            h.append(f'{a} {opr} {b} = {result}')
    print('\n')
#-------------------------------------------------------------------------------------------------
if i==5:
    print('good job!')
last=input('press h for history  OR  press q to exit:')
if last=='h':
    for item in h:
        print(item)
    c=input('press c to clear history / press any key to skip')
    if c=='c':
        h.clear()
        print('history cleared')
elif last=='q':
    print('bye')


