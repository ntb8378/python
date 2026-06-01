# danh sách đơn hàng
order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn: "))
    except:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    if choice == 1:
        # hiển thị danh sách đơn hàng
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                print(f"{i+1}. {order_list[i]}")

    elif choice == 2:
        # gán tài xế
        ma_don = input("Nhập mã đơn hàng: ").strip().upper()

        found = False

        for i in range(len(order_list)):
            if ma_don in order_list[i]:
                found = True

                if "PENDING" in order_list[i]:
                    order_list[i] = order_list[i].replace("PENDING", "ASSIGNED")
                    print("Gán tài xế thành công.")
                else:
                    print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")

                break

        if found == False:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == 3:
        # cập nhật trạng thái
        ma_don = input("Nhập mã đơn hàng: ").strip().upper()

        found = False

        for i in range(len(order_list)):
            if ma_don in order_list[i]:
                found = True

                if "ASSIGNED" in order_list[i]:
                    order_list[i] = order_list[i].replace("ASSIGNED", "DELIVERING")
                    print("Cập nhật thành công.")

                elif "DELIVERING" in order_list[i]:
                    order_list[i] = order_list[i].replace("DELIVERING", "COMPLETED")
                    print("Cập nhật thành công.")

                elif "PENDING" in order_list[i]:
                    print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")

                elif "COMPLETED" in order_list[i]:
                    print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")

                elif "CANCELLED" in order_list[i]:
                    print("Đơn hàng đã bị hủy, không thể cập nhật.")

                break

        if found == False:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == 4:
        # hủy đơn hàng
        ma_don = input("Nhập mã đơn hàng: ").strip().upper()

        found = False

        for i in range(len(order_list)):
            if ma_don in order_list[i]:
                found = True

                if "PENDING" in order_list[i]:
                    order_list[i] = order_list[i].replace("PENDING", "CANCELLED")
                    print("Hủy đơn hàng thành công.")

                elif "ASSIGNED" in order_list[i]:
                    order_list[i] = order_list[i].replace("ASSIGNED", "CANCELLED")
                    print("Hủy đơn hàng thành công.")

                elif "DELIVERING" in order_list[i]:
                    print("Đơn hàng đang được giao, không thể hủy.")

                elif "COMPLETED" in order_list[i]:
                    print("Đơn hàng đã hoàn tất, không thể hủy.")

                elif "CANCELLED" in order_list[i]:
                    print("Đơn hàng đã được hủy trước đó.")

                break

        if found == False:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == 5:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")