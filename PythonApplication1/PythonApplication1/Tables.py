x = range(2,11)
y = range(1,11)
for n1 in x:
    print('='*20)
    for n2 in y:
        print('%d * %d = %d' %(n1,n2,n1*n2))
    print('='*20)
