
def menu():
    choice = print("""
    ===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====
    1. Hiển thị danh sách bệnh nhân
    2. Tiếp nhận bệnh nhân mới
    3. Cập nhật chẩn đoán bệnh theo mã BN
    4. Tìm kiếm và thống kê theo tên bệnh
    5. Thoát chương trình
    ===========================================
""")

def output_list(patients):
    menu_title = f"DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ".center(80,"-")
    print(menu_title)
    for index, value in enumerate(patients):
        print (f"""{index+1}. "Mã:" {value[1]:<20} | "Giới tính:" {value[2]:<5} | "Bệnh": {value[3]}""")
        
def main():
    patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn:")
        match choice:
            case "1":
                output_list(patients)
                break
            case "1":
                pass
            case "1":
                pass
            case "1":
                pass
            case "1":
                print("đã thoát!")
                break
            case _:
                print("lựa chọn không hợp lệ!")
main()