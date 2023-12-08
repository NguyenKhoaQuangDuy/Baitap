#Bài 5
dtb= float(input('Nhap diem: '))
if dtb<0:
    print ('Loi')
    exit ()
if dtb>10:
    print ('Loi')
    exit ()
if dtb<3.5:
    print ('Kém')
elif dtb<5.0:
    print ('Yếu')
elif dtb<6.5:
    print ('Trung bình')
elif dtb<8:
    print ('Khá')
elif dtb<=9:
    print ('Giỏi')
else:
    print ('Xuất sắc')
