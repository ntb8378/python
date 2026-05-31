shop_name = ""
product_name = ""
product_description = ""
category = ""
keyword_list = []
discount_code_list = []

while True:
    print("\n===== HỆ THỐNG KIỂM DUYỆT NỘI DUNG SẢN PHẨM SHOPEE =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    if choice == 1:
        shop_name = input("Nhập tên shop: ")
        product_name = input("Nhập tên sản phẩm: ")
        product_description = input("Nhập mô tả sản phẩm: ")
        category = input("Nhập danh mục sản phẩm: ")
        keywords = input("Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        if product_description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        shop_name = shop_name.strip()
        product_name = product_name.strip().title()
        product_description = product_description.strip()
        category = category.strip().lower()

        keyword_list = keywords.split(",")

        for i in range(len(keyword_list)):
            keyword_list[i] = keyword_list[i].strip()

        print("\n===== BÁO CÁO THỐNG KÊ =====")
        print("Tên shop:", shop_name)
        print("Tên sản phẩm:", product_name)
        print("Mô tả sản phẩm:", product_description)
        print("Độ dài mô tả sản phẩm:", len(product_description))
        print("Danh mục sản phẩm:", category)
        print("Danh sách từ khóa:", keyword_list)
        print("Số lượng từ khóa:", len(keyword_list))
        print("Mô tả chữ thường:", product_description.lower())
        print("Mô tả chữ hoa:", product_description.upper())

    elif choice == 2:
        if shop_name.strip() == "":
            print("Chưa có dữ liệu shop")
            continue

        normalized_shop = shop_name.strip().lower().replace(" ", "-")

        if not normalized_shop.startswith("shop-"):
            normalized_shop = "shop-" + normalized_shop

        print("Tên shop ban đầu:", shop_name)
        print("Tên shop chuẩn hóa:", normalized_shop)

    elif choice == 3:
        discount_code = input("Nhập mã giảm giá: ").strip()

        if discount_code == "":
            print("Mã giảm giá không được rỗng")
            continue

        if " " in discount_code:
            print("Mã giảm giá không được chứa khoảng trắng")
            continue

        if len(discount_code) < 6 or len(discount_code) > 12:
            print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
            continue

        if discount_code != discount_code.upper():
            print("Mã giảm giá phải được viết hoa toàn bộ")
            continue

        if not discount_code.isalnum():
            print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
            continue

        if not discount_code.startswith("SALE"):
            print("Mã giảm giá phải bắt đầu bằng SALE")
            continue

        discount_code_list.append(discount_code)

        print("Mã giảm giá hợp lệ")
        print("Danh sách mã giảm giá hiện tại:", discount_code_list)

    elif choice == 4:
        if product_description.strip() == "":
            print("Chưa có mô tả sản phẩm")
            continue

        find_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")

        if find_keyword in product_description:
            count = product_description.count(find_keyword)
            product_description = product_description.replace(find_keyword, replace_keyword)

            print("Số lần xuất hiện của từ khóa:", count)
            print("Mô tả sau khi thay thế:")
            print(product_description)
        else:
            print("Không tìm thấy từ khóa trong mô tả sản phẩm")

    elif choice == 5:
        print("Thoát chương trình")
        break