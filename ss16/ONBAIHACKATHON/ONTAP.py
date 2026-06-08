# Tạo menu gồm 3 chức năng (Menu phải dùng function)
# chức năng 1: Cho người dùng nhập vào số lượng sv và nhập từng sinh viên vào ds
# Mỗi sinh viên là 1 dict
# Chức năng 2: Hiển thị danh sách sinh viên
# Chức năng 3: Tìm kiếm sinh viên theo tên do người dùng nhập vào ( tìm tương đối )
# chức năng 4: sửa , xóa , sắp xếp , id tự tăng , id không trùng
# Lưu ý: Tất cả chức năng đều phải được viết trong function, sau đó mới gọi vào case


def get_validate_input(prompt : str, input_type: str = "str"):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Dữ liệu không được để trống! Nhập lại!")
            continue
        # "-123"
        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0:
                    print("Dữ liệu phải là số nguyên dương!, Nhập lại")
                    continue
                return value
             # Lỗi
            except ValueError:
                print("Dữ liệu không hợp lệ, Nhập lại!")
                continue
        return user_input

# id_input = get_validate_input("Hãy nhâp id sinh viên:", "int")


def menu():
    print("=" * 60)
    print("    ----- HỆ THỐNG QUẢN LÝ SINH VIÊN ------")
    print("=" * 60)
    print("1. Nhập sinh viên.")
    print("2. Hiển thị danh sách sinh viên.")
    print("3. Tìm kiếm sinh viên theo tên.")
    print("-" * 60)

def input_student(students):
    # global students
    num_std = get_validate_input("Nhập vào số lượng sinh viên: ", "int")
    for i in range(num_std):
        print("Nhập vào sinh viên thứ", i + 1)
        while True:
            input_id = get_validate_input("Nhập vào id sinh viên: ")
            # find_std = False
            for item in students:
                if (input_id == item.get("id")):
                    print("Id bạn nhập đã trùng, Nhập lại!")
                    # find_std = True
                    break
            else: 
            # if find_std == False:
                input_name = get_validate_input("Nhập vào tên sinh viên: ")
                new_std = { "id": input_id, "name": input_name }
                students.append(new_std)
                break


def display_student(students):
    if not students:
        print("Danh sách rỗng!")
        return
    print(f"{"STT":<3} | {"ID":<5} | {"Tên":<20}")
    for index, value in enumerate(students, start=1):
        print(f"{index:<3} | {value.get('id'):<5} | {value.get('name'):<20}")
    

def search_student(students):
    search_name = get_validate_input("Nhập vào tên cần tìm: ", "str")
    find_students = []
    for item in students:
        if (search_name.lower() in item.get("name").lower()):
            new_std = { "id": item.get("id"), "name": item.get("name") }
            find_students.append(new_std)
    print("Danh sách sinh viên tìm được!")
    display_student(find_students)

def main():
    students = [
        { "id": "S001", "name": "Tuấn"},
        { "id": "S002", "name": "Khiêm"}
    ]
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1": 
                input_student(students)
            case "2":
                display_student(students)
            case "3":
                search_student(students)
            case "5":
                print("Thoát chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

main()