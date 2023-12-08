t=int(input('Nhap so tien (Boi so cua 50000): '))
if t<0:
    print ('Loi')
    exit ()
if t%50000!=0:
    print ('Loi')
    exit ()
if t>=500000:
    t1=t//500000
    t=t%500000
    print ('So to 500000 la:',t1)
if t>=200000:
    t2=t//200000
    t=t%200000
    print ('So to 200000 la:',t2)
if t>=100000:
    t3=t//100000
    t=t%100000
    print ('So to 100000 la:',t3)
if t>=50000:
    t3=t//50000
    t=t%50000
    print ('So to 50000 la:',t3)

        

    
        
