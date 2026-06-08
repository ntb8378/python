# Hàm không có tham số => không có giá trị trả về
# def sum_number():
#     a = 10
#     b = 20
#     print(a + b)

#  Hàm có tham số
# def sum_number(a, b):
#     print(a + b)

# def sum_number(a, b):
#    return a + b

# result = sum_number(10, 20)
# print(result)

# counter = 0

# def increment():
#     # global counter; 
#     counter = 0
#     counter += 1; 

# increment()

# print(counter)
# counter = 0
# for i in range(5): 
#     counter += 1

# print(counter)

# counter = 10

# def increment(count):
#     global counter;
#     counter = count - 3
#     return counter

# counter = increment(counter)
# print(counter)

# Tạo menu gồm 3 chức năng (Menu phải dùng function)
# chức năng 1: Cho người dùng nhập vào số lượng sv và nhập từng sinh viên vào ds
# Mỗi sinh viên là 1 dict
# Chức năng 2: Hiển thị danh sách sinh viên
# Chức năng 3: Tìm kiếm sinh viên theo tên do người dùng nhập vào ( tìm tương đối )
# Lưu ý: Tất cả chức năng đều phải được viết trong function, sau đó mới gọi vào case

def get_validate_input(prompt: str, input_type: str = "text"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Dữ iệu không được để trống! Nhập lại!")  
            continue
        # "123abc"
        if input_type == "int":
            if not user_input.isdigit():
                print ("Dữ liệu không phải là số, Nhập lại!")
                continue
            value = int(user_input) # Lỗi
            return value
        return user_input

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
    num_std = int(input("Nhập số lượng sinh viên: "))
    for i in range(num_std):
        print(f"Nhập sinh viên thứ {i + 1}")
        stu_id = input("Nhập vào mã sinh viên: ")
        stu_name = input("Nhập vào tên sinh viên: ")
        new_std = { "id": stu_id, "name": stu_name}
        students.append(new_std)
def display_student(students):
    # global students
    for index, value in enumerate(students):
        print(f"Sinh viên thứ {index + 1} có id: {value["id"]} - có tên: {value["name"]}")

def search_student(students):
    name_search = input("Nhập vào tên cần tìm: ")
    for item in students:
        if (name_search in item["name"]):
            print(f"Sinh viên có id: {item["id"]} - có tên: {item["name"]} đã tìm thấy")

def main():
    students = []
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
                