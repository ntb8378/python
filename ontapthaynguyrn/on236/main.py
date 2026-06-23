import sys
class Product:
    def __init__(self, id, name, import_price, quantity, storage_fee):
        self.id = id
        self.name = name
        self.import_price = import_price
        self.quantity = quantity
        self.storage_fee = storage_fee 
        self.total_value = 0
        self.stock_status = "chưa tính"

    def calculate_total_value(self):
        self.total_value = (self.import_price  * self.quantity ) + self.storage_fee 

    def classify_stock_status(self):
        if self.total_value >= 30000000:
            self.stock_status = "Rất cao"
        elif self.total_value >= 15000000:
            self.stock_status = "Cao"
        elif self.total_value >= 9000000:
            self.stock_status = "Trung bình"
        else:
            self.stock_status = "Thấp"

class ProductManager:
    def __init__(self):
        self.products = []

    def add_store(self):
        input_id = input("Nhập mã SP: ").strip()
        if not input_id:
            print("Mã SP không được để trống!")
            return
        for pro in self.products:
            if input_id.lower() == pro.id.lower():
                print("Mã SP đã tồn tại!")
                return
        input_name = input("Nhập tên sản phẩm: ").strip()
        if not input_name:
            print("Tên sản phẩm không được để trống!")
            return
        
        try:
            input_import_price = int(input("Nhập giá nhập sản phẩm: "))
        except ValueError:
            print("giá nhâp phải là số nguyên!")
            return
        if input_import_price < 0:
            print("giá nhập không được âm!")
            return
        
        try:
            input_storage_fee = int(input("Nhập chi phí kho: "))
        except ValueError:
            print("chi phí kho phải là số nguyên!")
            return
        if input_storage_fee < 0:
            print("chi phí kho không được âm!")
            return
        
        try:
            input_quantity  = int(input("Nhập Số lượng tồn kho: "))
        except ValueError:
            print("Số lượng tồn kho phải là số nguyên!")
            return
        if (input_quantity  < 0 or input_quantity > 1000):
            print("giá nhập phải nằm trong đoạn từ 0 đến 1000!")
            return
        
        new_pro = Product(input_id, input_name, input_import_price, input_quantity, input_storage_fee)
        new_pro.calculate_total_value()
        new_pro.classify_stock_status()
        self.products.append(new_pro)
        
        print("Thêm thành công!")

    def show_all(self):
        if not self.products:
            print("Kho đang trống!")
        else:
            print(f"{'Mã SP':<10} | {'Tên sản phẩm':20} | {'Giá nhập':<10} | {'Số lượng':<10} | {'Chi phí kho':<15} | {'Tổng giá trị':<15} | {'Trạng thái':<20} ")
            for pro in self.products:
                print(f"{pro.id:<10} | {pro.name:20} | {pro.import_price:<10} | {pro.quantity:<10} | {pro.storage_fee:<15} | {pro.total_value:<15} | {pro.stock_status:<20} ")

    def update_product(self):
        search_id = input("Nhập mã SP cần cập nhật: ").strip()
        found = False
        for pro in self.products:
            if (search_id.lower() == pro.id.lower()):
                found = True
                try:
                    update_import_price = int(input("Nhập giá nhập sản phẩm: "))
                except ValueError:
                    print("giá nhâp phải là số nguyên!")
                    return
                if update_import_price < 0:
                    print("giá nhập không được âm!")
                    return
                
                try:
                    update_quantity  = int(input("Nhập Số lượng tồn kho: "))
                except ValueError:
                    print("Số lượng tồn kho phải là số nguyên!")
                    return
                if (update_quantity  < 0 or update_quantity > 1000):
                    print("giá nhập phải nằm trong đoạn từ 0 đến 1000!")
                    return
                
                try:
                    update_storage_fee = int(input("Nhập chi phí kho: "))
                except ValueError:
                    print("chi phí kho phải là số nguyên!")
                    return
                if update_storage_fee < 0:
                    print("chi phí kho không được âm!")
                    return
                
                pro.import_price = update_import_price
                pro.quantity = update_quantity
                pro.storage_fee = update_storage_fee 
                pro.calculate_total_value()
                pro.classify_stock_status()

                print("đã cập nhật thành công!")

        if not found:
            print(f"Không tìm thấy sản phẩm có id {search_id} !")

    def delete_product(self):
        search_id = input("Nhập mã SP cần xóa: ").strip()
        found = False
        for pro in self.products:
            if (search_id.lower() == pro.id.lower()):
                found = True
                confirm = input("Bạn có chắc muốn xóa sản phẩm này khỏi hệ thống không? (Y/N): ")
                if confirm.lower() == "y":
                    self.products.remove(pro)
                    print("đã xóa thành công!")
                    break
                elif confirm.lower() == "n":
                    print("đã hủy chức năng xóa!")
                    return
                else: 
                    print("chỉ được nhập y và n thôi!")
                    return

        if not found:
            print("không tìm thấy mã sản phẩm này!")

    def search_product(self):
        search_name = input("Nhập tên SP cần tim: ").strip()
        found = False
        for pro in self.products:
            if (search_name.lower() in pro.name.lower()):
                found = True
                print(f"{'Mã SP':<10} | {'Tên sản phẩm':20} | {'Giá nhập':<10} | {'Số lượng':<10} | {'Chi phí kho':<15} | {'Tổng giá trị':<15} | {'Trạng thái':<20} ")
                print(f"{pro.id:<10} | {pro.name:20} | {pro.import_price:<10} | {pro.quantity:<10} | {pro.storage_fee:<15} | {pro.total_value:<15} | {pro.stock_status:<20} ")
        if not found:
            print("không tìm thấy mã sản phẩm này!")

def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
======================================
""")
    
def main():
    Product_Manager = ProductManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                Product_Manager.show_all()
            case "2":
                Product_Manager.add_store()
            case "3":
                Product_Manager.update_product()
            case "4":
                Product_Manager.delete_product()
            case "5":
                Product_Manager.search_product()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng!")
                sys.exit(0)
            case _:
                print("lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()