sum_after_price=0
sum_before_price=int(input('nhập vào tổng số tiền ban đầu:'))
if(sum_before_price >= 500000):
    sum_after_price=sum_before_price*0.9
else:
    sum_after_price=sum_before_price

print(f"số tiền được giảm giá:{sum_before_price-sum_after_price}")
print(f'tổng số tiền khách phải trả: {sum_after_price}')