print("--- HỆ THỐNG CHUẨN HÓA DỮ LIỆU ---")

# Nhập dữ liệu
patient_code = input("Nhập mã bệnh nhân: ")

# Ép kiểu ngay lúc nhập
body_temperature = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))

# Hiển thị kết quả
print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")

print("Mã bệnh nhân:", patient_code)

print("Nhiệt độ cơ thể:", body_temperature, "độ C")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(body_temperature))

print("Nhịp tim:", heart_rate, "nhịp/phút")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))

print("\nThông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")