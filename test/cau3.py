
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