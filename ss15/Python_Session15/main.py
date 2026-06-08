inventory_stock = 0
total_revenue = 0

def add_stock(amount: int):
    global inventory_stock
    inventory_stock += amount
    print(f"Tồn kho hiện tại: {inventory_stock}")

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

def print_report():
    """Print report for total revenue
    """    

    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")

while True:
    menu_title = f" TECHSTORE MANAGEMENT SYSTEM ".center(50, "=")
    user_choice = input(f"""
{menu_title}
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
{'='*len(menu_title)}
Chọn chức năng (1-4): """)
    
    match user_choice:
        case "1":
            while True:
                add_stock_input = input("Nhập vào số lượng hàng muốn thêm: ")
                
                if add_stock_input.isdigit():
                    add_stock(int(add_stock_input))
                    break
                    
                print("Giá trị không hợp lệ. Vui lòng nhập lại!!!")
        case "2":
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
Đã bán thành công!""")
                total_revenue += total_price - discount + vat
                inventory_stock -= quantity_input
        case "3":
            print_report()
        case "4":
            print("Thoát chương trình!!!")
            break
        case _:
            print("Không hợp lệ. Vui lòng nhập lại!!!")