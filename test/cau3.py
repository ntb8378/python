
# câu 3
sum_ok_item= 0
total_item=0
while True:
    print('nhập 0 để thoát, \
           nhập 1 để nhập')
    chose= input('mời nhập:')
    if(chose == '1'):
            thunghang= int(input('nhập số thùng hàng:'))
            for i in range(1,thunghang+1):
                motthung=int(input(f'số lượng thùng {i}'))
                if(motthung >= 0 ):
                    sum_ok_item +=1
                    total_item = total_item +motthung
            print(f'tổng số lượng thùng hàng hợp lệ: {sum_ok_item}')
            print(f'tổng số lượng sản phẩm thu được: {total_item}')
    if(chose == '0'):
        print('thoát')
        break
    