class Store:
    def __init__(self, id, name, revenue_day, open_days, bonus):
        self.id = id
        self.name = name
        self.revenue_day = revenue_day
        self.open_days = open_days
        self.bonus = bonus
        self.net_revenue = 0
        self.performance_type = ""
    
    def calculate_net_revenue(self):
        self.net_revenue = (self.revenue_day * self.open_days) + self.bonus

    def classify_performance(self):
        if self.net_revenue >= 30000000:
            self.performance_type = "Cao"
        elif self.net_revenue >= 15000000:
            self.performance_type = "Khá"
        elif self.net_revenue >= 9000000:
            self.performance_type = "Trung bình"
        else:
            self.performance_type = "Thấp"

class StoreManager:
    def __init__(self):
        self.stores = []

    def add_store(self):
        input_id = input("Nhập mã CH: ").strip()
        if not input_id:
            print("Mã CH không được để trống!")
            return
        for store in self.stores:
            if input_id.lower() == store.id.lower():
                print("Mã CH đã tồn tại!")
                return
        input_name = input("Nhập tên cửa hàng: ").strip()
        if not input_name:
            print("Tên cửa hàng không được để trống!")
            return
        try:
            input_revenue_day = int(input("Nhập doanh thu ngày: "))
        except ValueError:
            print("Doanh thu ngày phải là số nguyên!")
            return
        if input_revenue_day < 0:
            print("Doanh thu ngày không được âm!")
            return
        try:
            input_open_days = int(input("Nhập số ngày mở cửa: "))
        except ValueError:
            print("Số ngày mở cửa phải là số nguyên!")
            return
        if input_open_days < 0 or input_open_days > 31:
            print("Số ngày mở cửa phải nằm trong khoảng từ 0 đến 31!")
            return
        try:
            input_bonus = int(input("Nhập doanh thu thưởng: "))
        except ValueError:
            print("Doanh thu thưởng phải là số nguyên!")
            return
        if input_bonus < 0:
            print("Doanh thu thưởng không được âm!")
            return
        new_store = Store(
            input_id,
            input_name,
            input_revenue_day,
            input_open_days,
            input_bonus
        )
        new_store.calculate_net_revenue()
        new_store.classify_performance()
        self.stores.append(new_store)
        print("Đã thêm cửa hàng thành công!")

    def show_all(self):
        if not self.stores:
            print("DANH SÁCH RỖNG!")
            return
        print(f"{'MÃ CỬA HÀNG':<10} | {'TÊN CỬA HÀNG':<20} | {'DOANH THU MỤC TIÊU MỘT NGÀY':<25} | {'SỐ NGÀY MỞ CỬA HOẠT ĐỘNG TRONG THÁNG':<25} | {'DOANH THU THƯỞNG THÊM':<25} | {'TỔNG DOANH THU THUẦN':<25} | {'PHÂN LOẠI HIỆU NĂNG':<20}")
        for store in self.stores:
            print(f"{store.id:<10} | {store.name:<20} | {store.revenue_day:<25} | {store.open_days:<25} | {store.bonus:<25} | {store.net_revenue:<25} | {store.performance_type:<20}")

    def update_store(self):
        search_id = input("Nhập mã CH cần sửa: ").strip()
        found = False
        for store in self.stores:
            if search_id.lower() == store.id.lower():
                found = True
                try:
                    new_revenue_day = int(input("Nhập doanh thu ngày: "))
                except ValueError:
                    print("Doanh thu ngày phải là số nguyên!")
                    return
                if new_revenue_day < 0:
                    print("Doanh thu ngày không được âm!")
                    return
                try:
                    new_open_days = int(input("Nhập số ngày mở cửa: "))
                except ValueError:
                    print("Số ngày mở cửa phải là số nguyên!")
                    return
                if new_open_days < 0 or new_open_days > 31:
                    print("Số ngày mở cửa phải nằm trong khoảng từ 0 đến 31!")
                    return
                try:
                    new_bonus = int(input("Nhập doanh thu thưởng: "))
                except ValueError:
                    print("Doanh thu thưởng phải là số nguyên!")
                    return
                if new_bonus < 0:
                    print("Doanh thu thưởng không được âm!")
                    return

                store.revenue_day = new_revenue_day
                store.open_days = new_open_days
                store.bonus = new_bonus
                store.calculate_net_revenue()
                store.classify_performance()
                print("cập nhật thành công!")
                break


        if not found:
            print("Mã cửa hàng không tồn tại!")

    def delete_store(self):
        search_id = input("Nhập mã CH cần xóa: ").strip()
        found = False
        for store in self.stores:
            if search_id.lower() == store.id.lower():
                found = True
                confirm = input("Bạn có chắc muốn xóa cửa hàng này không? (Y/N)").lower()
                if confirm == "y":
                    self.stores.remove(store)
                    print("đã xóa thành công!")
                    break
                else:
                    print("đã hủy bỏ thao tác!")
                    break
        if not found:
            print("Mã cửa hàng không tồn tại!")

    def search_store(self):
        search = input("Nhập tên CH cần tìm: ").strip()
        if not search:
            print("Không được để trống!")
            return
        found = False
        for store in self.stores:
            if search.lower() in store.name.lower():
                if not found:
                    print(f"{'MÃ CỬA HÀNG':<10} | {'TÊN CỬA HÀNG':<20} | {'DOANH THU MỤC TIÊU MỘT NGÀY':<25} | {'SỐ NGÀY MỞ CỬA HOẠT ĐỘNG TRONG THÁNG':<25} | {'DOANH THU THƯỞNG THÊM':<25} | {'TỔNG DOANH THU THUẦN':<25} | {'PHÂN LOẠI HIỆU NĂNG':<20}")
                found = True
                print(f"{store.id:<10} | {store.name:<20} | {store.revenue_day:<25} | {store.open_days:<25} | {store.bonus:<25} | {store.net_revenue:<25} | {store.performance_type:<20}")
        if not found:
            print("Không tìm thấy cửa hàng phù hợp")
        
    def statistics(self):
        if not self.stores:
            print("DANH SÁCH RỖNG!")
            return
        low = 0
        standard = 0
        good = 0
        high = 0
        for store in self.stores:
            if store.performance_type == "Cao":
                high += 1
            elif store.performance_type == "Khá":
                good += 1
            elif store.performance_type == "Trung bình":
                standard += 1
            elif store.performance_type == "Thấp":
                low += 1

        print(f"{'Hiệu năng':<10} | {'Số lượng':<10}")
        print(f"{'-'*20}")
        print(f"{'Thấp':<10} | {low:<10}")
        print(f"{'Trung bình':<10} | {standard:<10}")
        print(f"{'Khá':<10} | {good:<10}")
        print(f"{'Cao':<10} | {high:<10}")

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
======================================
""")
    
def main():
    Store_Manager = StoreManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                Store_Manager.show_all()
            case "2":
                Store_Manager.add_store()
            case "3":
                Store_Manager.update_store()
            case "4":
                Store_Manager.delete_store()
            case "5":
                Store_Manager.search_store()
            case "6":
                Store_Manager.statistics()
            case "7":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý cửa hàng & doanh thu!")
                break
            case _:
                print("lựa chọn không hợp lệ!")
    
main()
