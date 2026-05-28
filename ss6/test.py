# câu 1
# price= int(input("nhập đơn giá:"))
# quantity= int(input("nhập số lượng mua:"))
# total= price * quantity
# af_price= 0
# if(total >= 1000):
#     af_price= total * 0.9
# else:
#     af_price= total
# print(f"số tiền cuối cùng phải thanh toán: {af_price}")


# câu 2
# password = '123'
# count = 0
# for i in range(3):
#     password_input=input('nhập mk:')
#     if( password_input ==password):
#         print('đăng nhập thành công')
#         count += 1
#         break
#     else:
#         print("mật khẩu sai , vui lòng nhập lại")
# print('tài khoản đã bị khóa')
    

# câu 3
sum_ok_item= 0
chose=''
total_item=0
while (chose == '0'):
    print('nhập 0 để thoát' \
    '      nhập 1 để nhập')
    if(chose == '1'):
            thunghang= int(input('nhập số thùng hàng:'))
            for i in range(1,thunghang+1):
                motthung=int(input(f'số lượng thùng {i}'))
                if(motthung >= 0 ):
                    sum_ok_item +=1
                    total_item = total_item +motthung
    if(chose == '0'):
        print('thoát')
        break
print(f'tổng số lượng thùng hàng hợp lệ: {sum_ok_item}')
print(f'tổng số lượng sản phẩm thu được: {total_item}')