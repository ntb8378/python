patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


def menu():
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")
    return input("Chọn chức năng (1-5): ")


def find_patient_index(records, patient_id):
    for i in range(len(records)):
        if records[i].startswith(patient_id + "-"):
            return i
    return -1


def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("\n--- DANH SÁCH BỆNH NHÂN ---")

    for i in range(len(records)):
        data = records[i].split("-")

        print(
            f"{i+1}. [{data[0]}] {data[1]} | "
            f"Năm sinh: {data[2]} | "
            f"Chẩn đoán: {data[3]}"
        )


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = name.replace("-", " ")
    name = name.title()

    while True:
        birth_year = input("Nhập năm sinh: ")

        if birth_year.isdigit() == False:
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        if int(birth_year) < 1900 or int(birth_year) > 2026:
            print("Năm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        break

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.replace("-", " ")
    diagnosis = diagnosis.capitalize()

    new_record = (
        patient_id
        + "-"
        + name
        + "-"
        + birth_year
        + "-"
        + diagnosis
    )

    records.append(new_record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print(new_record)


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[index].split("-")

    print(f"Tìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ")

    new_diagnosis = new_diagnosis.replace("-", " ")
    new_diagnosis = new_diagnosis.capitalize()

    data[3] = new_diagnosis

    records[index] = "-".join(data)

    print("Cập nhật chẩn đoán thành công!")
    print(records[index])


def generate_age_report(records):
    children = 0
    adults = 0
    elderly = 0

    current_year = 2026

    for record in records:
        data = record.split("-")

        age = current_year - int(data[2])

        if age < 16:
            children += 1
        elif age <= 60:
            adults += 1
        else:
            elderly += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")


def main():
    records = patient_records.copy()

    while True:
        choice = menu()

        if choice == "1":
            display_records(records)

        elif choice == "2":
            add_patient(records)

        elif choice == "3":
            update_diagnosis(records)

        elif choice == "4":
            generate_age_report(records)

        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()