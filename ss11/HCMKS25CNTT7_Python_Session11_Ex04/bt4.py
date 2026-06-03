product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
    },
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn của bạn: ").strip())
    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    match choice:
        case 1:
            if product_list:
                print("\nDanh sách sản phẩm hiện tại:")
                for i, p in enumerate(product_list, start=1):
                    if p["quantity"] == 0:
                        status = "Hết hàng"
                    elif p["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(
                        f"{i}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']} | "
                        f"Tồn kho: {p['quantity']} | Đã bán: {p['sold']} | Trạng thái: {status}"
                    )
            else:
                print("Danh sách sản phẩm hiện đang trống.")

        case 2:
            product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
            try:
                qty = int(input("Nhập số lượng khách mua: ").strip())
                if qty <= 0:
                    print("Số lượng mua không hợp lệ")
                    continue
            except ValueError:
                print("Số lượng mua không hợp lệ")
                continue

            found = False
            for p in product_list:
                if p["product_id"] == product_id:
                    found = True
                    if qty > p["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                    else:
                        p["quantity"] -= qty
                        p["sold"] += qty
                        total_price = qty * p["price"]
                        print(f"Bán thành công! Khách cần thanh toán: {total_price}")
                    break
            if not found:
                print("Không tìm thấy sản phẩm cần bán")

        case 3:
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
            try:
                qty = int(input("Nhập số lượng nhập thêm: ").strip())
                if qty <= 0:
                    print("Số lượng nhập kho không hợp lệ")
                    continue
            except ValueError:
                print("Số lượng nhập kho không hợp lệ")
                continue

            found = False
            for p in product_list:
                if p["product_id"] == product_id:
                    found = True
                    p["quantity"] += qty
                    print("Nhập kho thành công!")
                    break
            if not found:
                print("Không tìm thấy sản phẩm cần nhập kho")

        case 4:
            if any(p["sold"] > 0 for p in product_list):
                print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
                total_revenue = 0
                best_seller = None
                max_sold = 0
                for i, p in enumerate(product_list, start=1):
                    revenue = p["price"] * p["sold"]
                    total_revenue += revenue
                    print(
                        f"{i}. {p['product_name']} | Đã bán: {p['sold']} | Doanh thu: {revenue}"
                    )
                    if p["sold"] > max_sold:
                        max_sold = p["sold"]
                        best_seller = p["product_name"]
                print(f"\nTổng doanh thu: {total_revenue}")
                print(f"Sản phẩm bán chạy nhất: {best_seller}")
            else:
                print("Chưa có doanh thu phát sinh.")

        case 5:
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")