products_list = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def menu():
    menu = ("""
=====================================
    QUẢN LÝ CỬA HÀNG - MINI STORE
=====================================
1. Xem danh sách sản phẩm hiện có
2. Thêm mới một sản phẩm
3. Cập nhật giá sản phẩm theo ID
4. Thoát chương trình
=====================================
""")
    print(menu)

def show_products(products_list):
    if len(products_list) == 0:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
    else:
        print("--- DANH SÁCH SẢN PHẨM ---")
        print(f"{'ID':<10} | {'Tên sản phẩm':<20} | {'Giá bán':<20}")
        print("--------------------------------------------------------")
        for item in products_list:
            print(f"{item['id']:<10} | {item['name']:<20} | {item['price']:<20}")
        print("--------------------------------------------------------")
    

def check_str(prompt):
    while True:
        value= input(prompt).strip()
        if value == "":
            print("không được để trống!")
            continue
        return value
    
def check_int(prompt):
    while True:
        try:
            value= int(input(prompt))
            if value <=0:
                print("phải lớn hơn 0!")
                continue
            return value
        except:
            print("sai định dạng")


def add_product():
    input_id = check_str("nhập mã sản phẩm (ID):")
    for item in products_list:
        if input_id.lower() == item["id"].lower():
            print("id đã tồn tại!")
            return
    else:
        input_name = check_str("nhập tên sản phẩm:")
        input_price = check_int("nhập giá bán:")
        
        list_new = {'id': input_id, 'name': input_name, 'price': input_price}
        
        products_list.append(list_new)
        print("Thêm sản phẩm thành công!")

def update_price():
    finding= False
    search_id = check_str("nhập mã sản phẩm cần sửa giá:")
    for item in products_list:
        if search_id.lower() == item["id"].lower():
            finding = True
            print(f"Tìm thấy sản phầm: {item['name']} (Giá hiện tại: {item['price']})")
            update_new_price = check_int("Nhập giá mới:")

            item["price"]= update_new_price

            print("cập nhật giá thành công!")
            return
    if not finding:
        notfind = (f"Không tìm thấy sản phẩm có mã {search_id} !")
        print(notfind)
        return


def main():
    while True:
        menu()
        choice = input("nhập lựa chọn:")
        match choice:
            case "1":
                show_products(products_list)
            case "2":
                add_product()
            case "3":
                update_price()
            case "4":
                print("Cảm ơn bạn đã sử dụng phần mềm!")
                print("[CHương trình đã kết thúc]")
                break
            case _:
                print("lựa chọn không hợp lệ!")
main()