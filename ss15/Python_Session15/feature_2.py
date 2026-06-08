inventory_stock = 50

def check_user_input_int(input_content: str):
    while True:
        value_receive = input(f"{input_content}: ")
    
        if value_receive.isdigit():
            return int(value_receive)
        
        print("Vui lòng nhập lại!!!")

def process_sale(quantity: int, price: int):
    if quantity_input > inventory_stock:
        return
    
    return calculate_final_price(quantity, price)

def calculate_final_price(quantity: int, price: int):
    total = quantity * price
    discount = 0
    
    if total >= 1000:
        discount = total * 0.1

    vat = (total - discount) * 0.08
    
    return total, discount, vat

quantity_input = check_user_input_int("Nhập vào số lượng sản phẩm muốn mua")
price_input = check_user_input_int("Nhập vào đơn giá của sản phẩm")

final_total = process_sale(quantity_input, price_input)

if final_total is None:
    print("Không đủ hàng trong kho")
    
else:
    total_price, discount, vat = final_total
    print(f"""
-> Hóa đơn chi tiết:
Số lượng: {quantity_input} | Đơn giá: ${price_input}
Tạm tính: ${total_price}
Giảm giá (10%): ${discount}
Thuế VAT (8%): ${vat}
Tổng thanh toán: ${total_price - discount + vat}
Đã bán thành công!      
""")
