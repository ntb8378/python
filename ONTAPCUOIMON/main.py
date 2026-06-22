class Store:
    def __init__(self, id, name, revenue_day, open_days, bonus) :
        self.id = id
        self.name = name
        self.revenue_day = revenue_day
        self.open_days = open_days
        self.bonus = bonus
        self.calculate_net_revenue()
        self.classify_performance()

    def calculate_net_revenue(self):
        self.net_revenue = (self.revenue_day * self.open_days) + self.bonus
        
    def classify_performance(self):
        if self.net_revenue >= 30000000:
            self.performance_type = "Cao"
        elif self.net_revenue >= 15000000:
            self.performance_type = "Khá"
        elif self.net_revenue >= 9000000:
            self.performance_type = "Trung bình"
        else: self.performance_type = "Thấp"

class StoreManager:
    def __init__(self):
        self.stores = []

    def add_store(self):
        store_id = input ("Nhap vao mã Cửa hàng: ")
        store_name = input("Nhập vao tên cửa hang: ")
        store_revenue = int(input("Nhập vào doanh thu trên 1 ngày: "))  
        store_open_days = int(input("Nhap vao so ngay công: "))
        store_bonus = int(input("Nhap vao số tiền thưởng: "))
    # xem lại phần này
    # tại sao phải khởi tạo đối tượng new_store
        # new_store = Store(store_id, store_name, store_revenue, store_open_days, store_bonus)
        # new_store.calculate_net_revenue()
        # new_store. classify_performance()
        # print ("Them cửa hang thanh công!")
    # làm như v thì các đối tượng sẽ bị cùng tên nên thay thế bằng cái này
        new_store = Store(store_id, store_name, store_revenue, store_open_days, store_bonus)
        self.stores.append(new_store)
        print("Them cửa hàng thành công!")


    def show_store(self):
        print(f"{'MÃ CH':<5} | {'Tên cửa hàng':<20} | {'Doanh thu ngày':<20} | {'Số ngày mở':<10} | {'Thưởng':<10} | {'Doanh thu thuần':<15} | {'Hiệu năng':<10}")
        for store in self.stores:
            print(f"{store.id:<5} | {store.name:<20} | {store.revenue_day:<20} | {store.open_days:<10} | {store.bonus:<10} | {store.net_revenue:<15} | {store.performance_type:<10}")


    def update_store(self):
        store_id = input ("Nhap vao mã cua hang cần cap nhật: ")
        found = False
        for store in self.stores:
            if (store_id == store.id):
                
                store_revenue_day = int(input("Nhap vao doanh thu ngày mới: "))
                store_open_days = int(input("Nhap vao số ngay mo cửa moi: "))
                store_bonus = int(input("Nhap vao thưởng mới: "))
                store. revenue_day = store_revenue_day
                store. open_days = store_open_days
                store.bonus = store_bonus

                store.calculate_net_revenue()
                store.classify_performance()

                found = True

                print("Cập nhật thành công!")
                break
        if not found:
            print("Không tìm thấy")

    def delete_store(self):
        store_id = input("nhập mã cửa hàng muốn xóa")
        found = False
        for store in self.stores:
            if (store_id == store.id):
                found = True
                confirm= input("Bạn có chắc muốn xóa cửa hàng này không? (Y/N)")
                if confirm.lower() == "y":
                    self.stores.remove(store)
                    break
        if not found:
            print("không tìm hất id cần xóa!")

    def search_store(self):
        search = input("nhập id hoặc tên cửa hàng cần tìm").lower()
        found = False
        for store in self.stores:
            if (search.lower() in store.name.lower()) or (search.lower() == store.id):
                found = True
                print(f"{'MÃ CH':<5} | {'Tên cửa hàng':<20} | {'Doanh thu ngày':<20} | {'Số ngày mở':<10} | {'Thưởng':<10} | {'Doanh thu thuần':<15} | {'Hiệu năng':<10}")
                print(f"{store.id:<5} | {store.name:<20} | {store.revenue_day:<20} | {store.open_days:<10} | {store.bonus:<10} | {store.net_revenue:<15} | {store.performance_type:<10}")
                break
        if not found:
            print("không tìm hất id cần xóa!")

    def statistics(self):
        thap = 0
        trungbinh = 0
        kha = 0
        cao = 0
        for store in self.stores:
            if store.performance_type == "Cao":
                cao += 1
            elif store.performance_type == "Khá":
                kha += 1
            elif store.performance_type == "Trung bình":
                trungbinh += 1
            elif store.performance_type == "Thấp":
                thap += 1
        print(f"thấp: {thap}")
        print(f"trung bình: {trungbinh}")
        print(f"khá: {kha}")
        print(f"cao: {cao}")


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách cửa hàng
2. Thêm cửa hàng mới
3. Cập nhật thông tin cửa hàng
4. Xóa cửa hàng
5. Tìm kiếm cửa hàng
6. Thống kê hiệu năng
7. Thoát
=====================================""")
    
def main():
    store_manager = StoreManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "2":
                store_manager.add_store()
            case "1":
                store_manager.show_store()
            case "3":
                store_manager.update_store()
            case "4":
                store_manager.delete_store()
            case "5":
                store_manager.search_store()
            case "6":
                store_manager.statistics()
            case "7":
                print("đã thoát!")
                break
            case _:
                print("lựa chọn không hợp lệ")
if __name__ == "__main__":
    main()
        

