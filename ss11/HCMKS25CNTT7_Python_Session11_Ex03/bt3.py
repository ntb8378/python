product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    choice = input("mời nhập một số:")
    if choice == "1":
        if(len(product_list) == 0):

            print("\n==================================")
            print("danh sách sản phẩm hiện đang trống")
            print("==================================\n")

        else:    
            for i in range(len(product_list)):
                print(f"{i} Mã SP: {product_list[i]['product_id']} | Tên: {product_list[i]['product_name']} | Giá: {product_list[i]['price']} | Số lượng: {product_list[i]['quantity']}")
    if choice == "2":

        input_id = input("Nhập mã sản phẩm: ").strip().upper()
        input_name = input("Nhập tên sản phẩm: ")
        input_price = int(input("Nhập giá sản phẩm: "))
        input_quantity = int(input("Nhập số lượng sản phẩm: "))

        if input_price <= 0 or input_quantity <= 0:
            print("Giá/Số lượng không hợp lệ")

        else:
            duplicate = False

            for product in product_list:
                if product["product_id"] == input_id:
                    duplicate = True

            if duplicate:
                print("Mã sản phẩm bị trùng")

            else:
                new_product = {
                    "product_id": input_id,
                    "product_name": input_name,
                    "price": input_price,
                    "quantity": input_quantity
                }

                product_list.append(new_product)
                print("Thêm sản phẩm thành công")
    if choice == "3":

        update_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == update_id:

                found = True

                new_name = input("Nhập tên mới: ")
                new_price = int(input("Nhập giá mới: "))
                new_quantity = int(input("Nhập số lượng mới: "))

                if new_price <= 0 or new_quantity <= 0:
                    print("Giá/Số lượng không hợp lệ")

                else:
                    product["product_name"] = new_name
                    product["price"] = new_price
                    product["quantity"] = new_quantity

                    print("Cập nhật sản phẩm thành công")

                break

        if found == False:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
    if choice == "4":

        delete_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == delete_id:

                product_list.remove(product)
                found = True

                print("Xóa sản phẩm thành công")
                break

        if found == False:
            print("Không tìm thấy mã sản phẩm cần xoá!")
    if choice == "5":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")