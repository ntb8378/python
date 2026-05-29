raw_data = (
    "emp-001,nguyen van a,it,0912-345-678;"
    "emp-002,tran thi b,hr,0987654321;"
    "emp-003,le van c,finance,09ab123456"
)

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()
    if choice == "1":

        print("\n===== DỮ LIỆU GỐC =====")
        print(raw_data)
    elif choice == "2":

        print("\n========== BÁO CÁO NHÂN VIÊN ==========")

        print(f"{'ID':<12}{'HỌ TÊN':<25}{'PHÒNG BAN':<15}{'SĐT'}")

        employees = raw_data.split(";")

        for employee in employees:
            fields = employee.split(",")

            employee_id = fields[0].strip().upper()

            full_name = fields[1].strip().title()

            department = fields[2].strip().upper()

            phone = fields[3].strip()

            phone = phone.replace("-", "")

            if phone.isdigit():

                phone = "******" + phone[-4:]

            else:

                phone = "Invalid Format"

            print(
                f"{employee_id:<12}"
                f"{full_name:<25}"
                f"{department:<15}"
                f"{phone}"
            )
    elif choice == "3":

        search_id = input("Nhập mã nhân viên cần tìm: ")

        search_id = search_id.strip().upper()

        employees = raw_data.split(";")

        found = False

        for employee in employees:

            fields = employee.split(",")

            employee_id = fields[0].strip().upper()

            if employee_id == search_id:

                full_name = fields[1].strip().title()

                department = fields[2].strip().upper()

                phone = fields[3].strip()

                phone = phone.replace("-", "")

                if phone.isdigit():

                    phone = "******" + phone[-4:]

                else:

                    phone = "Invalid Format"

                print("\n===== THÔNG TIN NHÂN VIÊN =====")

                print("ID:", employee_id)
                print("Họ tên:", full_name)
                print("Phòng ban:", department)
                print("SĐT:", phone)

                found = True

                break

        if found == False:

            print("Không tìm thấy nhân viên")

    elif choice == "4":

        print("Thoát chương trình")

        break
    else:

        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

