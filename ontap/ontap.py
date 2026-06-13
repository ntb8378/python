def menu():
    menu = ("""
--- quản lý danh sách giao dịch ---
1. Hiển thị nhật ký giao dịch
2. Ghi nhận giao dịch mới
3. Cập nhật chứng từ giao dịch
4. Xóa giao dịch lỗi
5. Tìm kiếm giao dịch
6. Thống kê tổng dòng tiền
7. Phân loại quy mô tự động
8. Thoát chương trình
""")
    print(menu)

def render_list():
    

def main():
    list= []
    while True:
        menu()
        choice = input("nhập lựa chọn:")
        match choice:
            case "1":
                pass
            case "1":
                pass
            case "1":
                pass
            case "1":
                pass
            case "1":
                pass
            case "1":
                pass
            case "1":
                pass
            case "8":
                print("đã thoát")
                break
            case _:
                print("lựa chọn k hợp lệ!")
main()