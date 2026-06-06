Parkings=[
    {'id': 1, 'type': 1, 'owner': "Nguyen Van A"},
    {'id': 2, 'type': 2, 'owner': "Tran Van B"}
]
id_new = 0
xoa=""
while True:
    print("\n==========================================")
    print(       "QUẢN LÝ BÃI XA - SMART PARKING       ")
    print("==========================================")
    print("1. Thêm xa mới vào bãi")
    print("2. Hiển thị danh sách xe trong bãi")
    print("3. Xóa xe khỏi bãi (khi xe ra)")
    print("4. Thoát chương trình")
    print("\n==========================================")
    choice= input("mời nhập lựa chọn:")
    if choice == "1":
        id_new += 1
        input_name = input("nhập tên khách:")
        if len(input_name) == 0:
            print("Chủ xe không được để trống")
            break
        while True:
                type_int = int(input("\nNhập loại xe :\n1. (Xe máy)\n2. (Ô tô)\nBạn chọn(1-2)? "))
                if type_int not in ("1, 2"):
                    print("Vui lòng chọn 1-2")
                    continue
                Parkings.append(
            {"id": id_new, "type": type_int, "owner": input_name }
        )
                print("đã thêm thành công")
                break
    if choice == "2":
        if len(Parkings) == 0:
            print("Bãi xe hiện đang trống!")
            continue
        print(f"{"ID":<5}| {"Loại xe":<10}| {"Chủ xe":<8}")
        print("------------------------------------------")
        for item in Parkings:
            if item["type"] == 1:
                type_text = "Xe máy"
            else:
                type_text = "Ô tô"
            print(
                f"{item["id"]:<5}| "
                f"{type_text:<10}| "
                f"{item["owner"]:<8}"
            )   
            break
    if choice == "3":
        search = int(input("nhập id cần xóa"))
        for item in Parkings:
            if search == item["id"]:
                Parkings.remove(item)
                print(f"đã xóa xe ID {item["id"]} thành công!")
            else:
                print("Không tim thấy xe để xóa")
                break
    if choice == "4":
        print("Đã thoát")
        break
                 

  