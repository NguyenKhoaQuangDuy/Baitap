#Bài 4
nam=int(input('Nhap nam: '))
if nam%4==0:
    if nam%100==0:
        if nam%400==0:
            print ('Nam nhuan')
        else:
            print ('Khong phai nam nhuan')
    else:
        print ('Nam nhuan')
else:
    print ('Khong phai nam nhuan')
