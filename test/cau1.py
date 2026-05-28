# câu 1
price= int(input("nhập đơn giá:"))
quantity= int(input("nhập số lượng mua:"))
total= price * quantity
af_price= 0
if(total >= 1000):
    af_price= total * 0.9
else:
    af_price= total
print(f"số tiền cuối cùng phải thanh toán: {af_price}")


