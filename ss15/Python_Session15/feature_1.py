inventory_stock = 0

def add_stock(amount: int):
    global inventory_stock
    inventory_stock += amount
    print(f"Tồn kho hiện tại: {inventory_stock}")

while True:
    add_stock_input = input("Nhập vào số lượng hàng muốn thêm: ")
    
    if add_stock_input.isdigit():
        add_stock(int(add_stock_input))
        break
        
    print("Giá trị không hợp lệ. Vui lòng nhập lại!!!")
