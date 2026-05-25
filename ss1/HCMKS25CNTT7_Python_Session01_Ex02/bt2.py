print (" --- HỆ THỐNG NHẬP CHỈ SỐ SINH TÔN-")
name_patient = input ("Nhập tên bệnh nhân : ")
weight - input ("Nhập cân nặng bệnh nhân : ")

print (" --- KIỂM TRA DỮ LIỆU LƯU TRỮ -- ")
print ("Bệnh nhân : " , name_patient)
print ("Cân nặng dã nhập : " , weight)

# Trưởng nhóm IT viết thêm dòng này dể kiểm tra dữ liệu của cân nặng
print ("CẢNH BAO - Kieu du lieu dang lưu la : ", type(weight))

# bài này vẫn chạy bthg nhưng kiểu dữ liệu của cân nặng không đúng bởi vì chưa ép kiểu , dữ liệu nhập từ input mặc định nó sẽ là dạng chuỗi
# nếu k ép kiểu thì type của weight sẽ là dạng chuỗi
# cách làm đúng

print (" --- HỆ THỐNG NHẬP CHỈ SỐ SINH TÔN-")
name_patient = input ("Nhập tên bệnh nhân : ")
weight - float(input ("Nhập cân nặng bệnh nhân : "))

print (" --- KIỂM TRA DỮ LIỆU LƯU TRỮ -- ")
print ("Bệnh nhân : " , name_patient)
print ("Cân nặng dã nhập : " , weight)

# Trưởng nhóm IT viết thêm dòng này dể kiểm tra dữ liệu của cân nặng
print ("CẢNH BAO - Kieu du lieu dang lưu la : ", type(weight))