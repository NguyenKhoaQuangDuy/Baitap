#Bài 7
x= int(input('Nhap so dien su dung: '))
if x<0:
    print ('Lỗi')
elif x==0:
    t=0
    print ('Tiền điện phải trả là: ',t)
elif x<=50:
    t=1.1*(1484*x)
    print ('Tiền điện phải trả là: ',t)
elif x<=100:
    t=1.1*(50*1484+(x-50)*1533)
    print ('Tiền điện phải trả là: ',t)
elif x<=200:
    t=1.1*(50*1484+50*1533+(x-100)*1786)
    print ('Tiền điện phải trả là: ',t)
elif x<=300:
    t=1.1*(50*1484+50*1533+100*1786+(x-200)*2242)
    print ('Tiền điện phải trả là: ',t)
elif x<=400:
    t=1.1*(50*1484+50*1533+100*1786+100*2242+(x-300)*2503)
    print ('Tiền điện phải trả là: ',t)
else:
    t=1.1*(50*1484+50*1533+100*1786+100*2242+100*2503+(x-400)*2587)
    print ('Tiền điện phải trả là: ',t)
    
