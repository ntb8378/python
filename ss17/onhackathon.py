list_trip = [
    {
        "id": "CX001",
        "route": "Sai Gon - Da Lat",
        "price": 300000,
        "empty_seat": 40,
        "total_seat": 40,
        "revenue": 0,
        "status": "E khach"
    }
]
def menu():
    menu = ("""
--- quản lý chuyến xe và đặt vé---
1. Hiển thị danh sách chuyến xe
2. Khai báo chuyến xe mới
3. Cập nhật đặt vé (Giảm ghế trống)
4. Hủy chuyến xe khỏi lịch trình
5. Tìm kiếm chuyến xe
6. Thống kê trạng thái chuyến xe
7. Phân loại trạng thái tự động
8. Thoát chương trình           
""")
    print(menu)

def render_list(list_trip):
    if len(list_trip) == 0:
        print("danh sách rỗng!")
    else:
        print("--- Chi tiết chuyến xe ---")
        header = (
    f"{'Mã chuyến xe':<20} | "
    f"{'Tuyến đường':<35} | "
    f"{'Giá vé':<20} | "
    f"{'Ghế trống':<20} | "
    f"{'Tổng ghế':<20} | "
    f"{'Doanh thu':<20} | "
    f"{'Trạng thái':<15}"
)
        print(header)
        for item in list_trip:
            print(
                f"{item['id']:<20} | "
                f"{item['route']:<35} | "
                f"{item['price']:<20,} | "
                f"{item['empty_seat']:<20} | "
                f"{item['total_seat']:<20} | "
                f"{item['revenue']:<20,} | "
                f"{item['status']:<15}"
            )
def input_new_trip():
    ma_chuyen =check_str("Nhập mã chuyến xe: ")
    for item in list_trip:
        if ma_chuyen.lower() == item["id"].lower():
            print("không được trùng id")
            return
    tuyen_duong = check_str("Nhập tuyến đường: ")
    gia_ve = check_int("Nhập giá vé: ")
    tong_so_ghe = check_int("Nhập tổng số ghế: ")

    so_ghe_trong = tong_so_ghe  
    so_ghe_da_ban = tong_so_ghe - so_ghe_trong  
    doanh_thu = gia_ve * so_ghe_da_ban  
    trang_thai = tinh_trang_thai(so_ghe_trong, tong_so_ghe)

    chuyen_xe = {
        "id": ma_chuyen,
        "route": tuyen_duong,
        "price": gia_ve,
        "empty_seat": so_ghe_trong,
        "total_seat": tong_so_ghe,
        "revenue": doanh_thu,
        "status": trang_thai
    }
    list_trip.append(chuyen_xe)
    print("Thêm chuyến xe thành công!")

def tinh_trang_thai(so_ghe_trong, tong_so_ghe):
    if so_ghe_trong == 0:
        return "Hết vé"
    ti_le = so_ghe_trong / tong_so_ghe
    if ti_le < 0.15:
        return "Hút khách"
    elif ti_le <= 0.8:
        return "Bình thường"
    else:
        return "Ế khách"

def update_booking():
    finding= False
    search_id= input("nhập mã CX:")
    for item in list_trip:
        if search_id.lower() == item["id"].lower():
            finding = True
            so_ve = int(input("Nhập số vé: "))
            if so_ve <= 0 or so_ve > item["empty_seat"]:
                print("Số vé không hợp lệ!")
                return
            item["empty_seat"] -= so_ve
            item["revenue"] += so_ve * item["price"]

            item["status"] = tinh_trang_thai(
                item["empty_seat"],
                item["total_seat"]
            )

            print("Đặt vé thành công")
            break
    if not finding:
        print("Không tìm thấy id!")
            

def cancle_trip():
    finding= False
    search_id= input("nhập mã CX:")
    for item in list_trip:
        if search_id.lower() == item["id"].lower():
            finding = True
            confirm = input("bạn có chắc muốn xóa (Y/N):").lower()
            if confirm == "y":
                list_trip.remove(item)
                print("đã xóa")
            else:
                print("hủy xóa")
            return
    if not finding:
        print("không tìm thấy id cần xóa")


def search_trip():
    finding= False
    search_id= input("nhập mã CX:")
    for item in list_trip:
        if search_id.lower() == item["id"].lower():
            finding = True
            print(
                f"{item['id']} | {item['route']} | {item['price']} | "
                f"{item['empty_seat']} | {item['total_seat']} | "
                f"{item['revenue']} | {item['status']}"
            )

    if not finding:
        print("Không tìm thấy chuyến xe!")

def statistic_trip():
    het_ve = 0
    hut_khach = 0
    binh_thuong = 0
    e_khach = 0

    for item in list_trip:
        if item["status"] == "Hết vé":
            het_ve += 1
        elif item["status"] == "Hút khách":
            hut_khach += 1
        elif item["status"] == "Bình thường":
            binh_thuong += 1
        else:
            e_khach += 1

    print("Hết vé:", het_ve)
    print("Hút khách:", hut_khach)
    print("Bình thường:", binh_thuong)
    print("Ế khách:", e_khach)

def recalc_status_all():
    for item in list_trip:
        item["status"] = tinh_trang_thai(
            item["empty_seat"],
            item["total_seat"]
        )

    print("Đã cập nhật trạng thái toàn bộ chuyến xe!")

def check_str(prompt):
    while True:
        vlue= input(prompt).strip()
        if vlue == "":
            print("không được để trống!")
            continue
        return vlue
    
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

def main():
    while True:
        menu()
        choice = input("nhập lựa chọn:")
        match choice:
            case "1":
                render_list(list_trip)
            case "2":
                input_new_trip()
            case "3":
                update_booking()
            case "4":
                cancle_trip()
            case "5":
                search_trip()
            case "6":
                statistic_trip()
            case "7":
                recalc_status_all()
            case "8":
                print("đã thoát")
                break
            case _:
                print("lựa chọn không hợp lệ!")
main()