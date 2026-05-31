username = ""
video_title = ""
video_description = ""
hashtag_list = []

while True:
    print("\n===== HỆ THỐNG KIỂM DUYỆT VÀ CHUẨN HÓA NỘI DUNG VIDEO TIKTOK =====")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên tài khoản TikTok")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả video")
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
        username = input("Nhập tên tài khoản: ")
        video_title = input("Nhập tiêu đề video: ")
        video_description = input("Nhập mô tả video: ")
        hashtags = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")

        if username.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        if video_description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        username = username.strip()
        video_title = video_title.strip().title()
        video_description = video_description.strip()

        hashtag_list = hashtags.split(",")

        for i in range(len(hashtag_list)):
            hashtag_list[i] = hashtag_list[i].strip()

        print("\n===== BÁO CÁO THỐNG KÊ =====")
        print("Tên tài khoản:", username)
        print("Tiêu đề video:", video_title)
        print("Mô tả video:", video_description)
        print("Độ dài mô tả:", len(video_description))
        print("Số lượng từ:", len(video_description.split()))
        print("Danh sách hashtag:", hashtag_list)
        print("Số lượng hashtag:", len(hashtag_list))
        print("Mô tả chữ thường:", video_description.lower())
        print("Mô tả chữ hoa:", video_description.upper())

    elif choice == 2:
        if username.strip() == "":
            print("Chưa có dữ liệu tài khoản")
            continue

        normalized_username = username.strip().lower()

        if not normalized_username.startswith("@"):
            normalized_username = "@" + normalized_username

        print("Tên tài khoản ban đầu:", username)
        print("Tên tài khoản chuẩn hóa:", normalized_username)

    elif choice == 3:
        hashtag = input("Nhập hashtag cần kiểm tra: ").strip()

        if hashtag == "":
            print("Hashtag không được rỗng")
            continue

        if not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")
            continue

        if " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")
            continue

        if len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")
            continue

        valid = True

        for char in hashtag[1:]:
            if not (char.isalnum() or char == "_"):
                valid = False
                break

        if not valid:
            print("Hashtag chỉ được chứa chữ cái, chữ số hoặc dấu gạch dưới")
            continue

        hashtag_list.append(hashtag)
        print("Hashtag hợp lệ")

    elif choice == 4:
        if video_description.strip() == "":
            print("Chưa có mô tả video")
            continue

        find_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")

        if find_keyword in video_description:
            count = video_description.count(find_keyword)
            new_description = video_description.replace(find_keyword, replace_keyword)
            print("Mô tả sau khi thay thế:")
            print(new_description)
            print("Số lần xuất hiện:", count)
            video_description = new_description
        else:
            print("Không tìm thấy từ khóa trong mô tả video")

    elif choice == 5:
        print("Thoát chương trình")
        break