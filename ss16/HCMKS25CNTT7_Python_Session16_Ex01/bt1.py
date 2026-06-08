# Danh sach chan doan hien tai cua benh nhan Nguyen Văn A
patient_diagnoses = ["Sot Xuat Huyet"]
# Ham chuan hoa ten benh va them vao ho sơ
def add_diagnosis(raw_diagnosis, current_list):
    # Co gang chuẩn hoa tên bệnh
    raw_diagnosis = raw_diagnosis.strip()
    raw_diagnosis = raw_diagnosis.title()
    # Them chan đoan vao danh sach benh an
    current_list.append(raw_diagnosis)
    return current_list

# Bac sĩ nhap them mot chan đoan moi bi loi đinh dang
new_diagnosis = " viEm phE QUan "

# Gọi ham để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ so benh an (Cac chan đoan):", updated_diagnoses)


# Tại sao hai dòng lệnh raw_diagnosis.strip() và raw_diagnosis.title() trong hàm không hề làm thay đổi giá trị của biến raw_diagnosis? bởi vì hàm chưa được gọi đúng, gán đúng.
# Để các hàm xử lý chuỗi ở trên thực sự phát huy tác dụng và chuỗi mới được lưu lại, ta cần sửa lại cú pháp gán biến lại
# Phương thức extend() của List hoạt động như thế nào khi tham số truyền vào là một chuỗi văn bản (String) nó sẽ thêm nhiều phần thử vào một list 
# Để khắc phục lỗi "vỡ vụn" chữ cái và đưa nguyên vẹn một chuỗi (ví dụ: "Viem Phe Quan") vào danh sách, ta cần thay thế extend() bằng phương thức append để chỉ thêm 1 phần tử thôi thì nó sẽ không bị rời rạc