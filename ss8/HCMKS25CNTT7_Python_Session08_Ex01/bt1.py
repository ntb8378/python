while True:
    print("+======================================+")
    print("|   HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK   |")
    print("| 1.Nhập và phân tích thông tin video")
    print("| 2.Chuẩn hóa tên tài khoản")
    print("| 3.Kiểm tran hashtag hợp lệ")
    print("| 4.Tìm kiếm và thay thế từ khóa")
    print("| 5.Thoát chương trình")
    print("+======================================+")
    choice = input(">Mời bạn chọn chức năng (1-5):")

    match (choice):
        case "1":
            print("Nhập và phân tích thông tin video")
            user_name = input("Nhập tên tài khoản:")
            title = input("Nhập tiêu đề video:")
            description = input("Nhập mô tả video:")
            list_hashtag = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
            print("====Đã qua xử lý, hiển thị!=====")
            print(f"Tên tài khoản: {user_name.strip()}")
            print(f"Tên tiêu đề: {title.title().strip()}")
            print(f"Mô tả: {description.strip()}")
            print(f"Độ dài mô tả: {len(description)}")
            count_space = description.count(" ") + 1
            print(f"Số lượng từ trong mô tả: {count_space}")
            # "#hashtag1, #hashtag2"
            list_temp = list_hashtag.split(",")
            new_list_hashtag = "".join(list_temp)
            print(f"Danh sách hashtag: {new_list_hashtag}")
            # Dùng kiến thức mới ( len(list) )
            count_hashtag = len(list_temp);
            print(f"Số lượng hashtag là: {count_hashtag}")
            print(f"Mô tả video đã chuyển thành thường: {description.lower()}")
            print(f"Mô tả video đã chuyển thành hoa: {description.upper()}")
        case "2":
            print(f"Tên tài khoản trước khi chuẩn hóa: {user_name}")
            print("Tên tài khoản sau khi chuẩn hóa: ", "@" + user_name.lower())
        case "3":
            hashtag = input("Nhập hashtag: ")
            if (hashtag == ""):
                print("Không được rỗng!")
            elif (not hashtag.startswith("#")):
                print("phải bắt đầu bằng #")
            elif (" " in hashtag):
                print("Không được chưa khoảng trắng")
            elif (len(hashtag) < 2):
                print("Phải chứa tối thiểu 2 kí tự") 
            else:
                print("Hashtag hợp lệ!")
                list_hashtag = list_hashtag + hashtag
                print(f"Danh sách hashtag mới: {list_hashtag}")
        case "4":
            find_word = input("Nhập từ khóa cần tìm: ")
            count_word = description.count(find_word)
            if (count_word > 0):
                description = description.replace(find_word, "Từ khóa mới")
                print(f"Mô tả sau khi thay thế:  {description}")
                print(f"Số lần xuất hiện từ khóa: {count_word}")
            else:
                print("Từ khóa không tìm thấy!")
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ!")
