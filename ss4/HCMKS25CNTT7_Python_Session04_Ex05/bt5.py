i=1
count_big_bill =0
while True:
    cus_bill = int(input(f'khách hàng {i} - nhập giá trị hóa đơn:'))
    total = total + cus_bill;
    count_bill = i;
    if (cus_bill >= 1000000):
        count_big_bill += 1;
    want=input("có muốn nhập tiếp không? (C/K):")
    if(want.lower() == 'k'):
        print('thoát')
        break;
    i = i + 1;
    
print (" -- Báo cáo tổng doanh thu cuối ngày Rikkei Store -- ")
print ("Tổng hóa đơn đã xử lý:", count_bill);
print("Tong doanh thu ngày hôm nay:", total);
print("Tống hóa đơn lớn hơn 1 triệu:", count_big_bill);
print (f"Ti lệ hoa đơn lớn đạt {(count_big_bill / count_bill)*100}")
