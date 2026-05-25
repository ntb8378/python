print("====================================")
print(" KIOSK TIẾP NHẬN VÀ KHAI BÁO Y TẾ")
print(" BỆNH VIỆN ĐA KHOA SỨC KHỎE VÀNG")
print("====================================")

patient_name = input(
"Nhập họ tên bệnh nhân:"
)
patient_code = input(
"Nhập mã bệnh nhân: "
)
patient_age = input(
"Nhập tuổi bệnh nhân bằng số: "
)
body_temperature = input(
"Nhập nhiệt độ cơ thể dạng số thực: "
)
heart_rate = input(
"Nhập nhịp tim dạng số nguyên: "
)
body_weight = input(
"Nhập cân nặng dạng số thực kg: "
)
symptom_description = input(
"Nhập triệu chứng ban đầu: "
)
patient_age = int(patient_age)
body_temperature = float(body_temperature)
heart_rate = int(heart_rate)
body_weight = float(body_weight)

print("\n")
print("==========================")
print("  PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("==========================")

print("Mã bệnh nhân:", patient_code)
print("Họ tên bệnh nhân:", patient_name)
print("Tuổi:", patient_age)
print("Nhiệt độ cơ thể:", body_temperature, "độ C")
print("Nhịp tim:", heart_rate, "nhịp/phút")
print("Cân nặng:", body_weight, "kg")
print("Triệu chứng:", symptom_description)

print("  TIẾP NHẬN DỮ LIỆU THÀNH CÔNG")

print("=============== SYSTEM LOG =================")

print("patient_name =", type(patient_name))
print("patient_code =", type(patient_code))
print("patient_age =", type(patient_age))
print("body_temperature =", type(body_temperature))
print("heart_rate =", type(heart_rate))
print("body_weight =", type(body_weight))
print("symptom_description=", type(symptom_description))
