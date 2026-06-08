# Danh sach thuoc ngay hom qua (Lich sử benh an can giu nguyen)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Ham tạo va cap nhat đon thuoc cho ngay mới
def update_prescription(old_prescription):
    # Lập trình viên co gang sao chep đơn thuốc sang ngày mới
    new_prescription = old_prescription.copy()
    # Co gang đoi ten thuoc o vi tri dau tien (index 0) tu Panadol thanh Paracetamol
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    # Thêm thuốc mới cho ngày hôm nay
    new_prescription.append("Oresol")
    return new_prescription

# Hệ thong chay cap thuoc cho ngay hom nay
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuoc hom qua:", yesterday_prescription)
print("Đon thuoc hom nay:", today_prescription)