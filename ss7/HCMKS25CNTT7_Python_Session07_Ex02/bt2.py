
transaction ="nguyEN vAn a | PYTHON-01 | 15000000 | paid"
# không thể nào chấm luôn được , python sẽ không hiểu
# phải gán vào biến đó.
transaction.strip()
# split là tách chuỗi và - ở trong đang và ký tự dùng để tách chuỗi
#  nhưng trong đề là | nên phải thay thế - thành |
parts = transaction.split("-")
#  sau khi đổi ký tự tách chuỗi thì bây h các câu này  mới chạy đúng
student_name = parts[0].title()
course_code = parts [1]
# amout là số nhưng khi nhập thì nó là chuỗi
# nên phải ép chuỗi thành số nguyên bằng int
amount = parts [2]
status = parts [3].upper()

print( "Học viên:", student_name)
print( "Khóa học:", course_code)
print("So tiên:", amount, "VND")
print("Trạng thái:", status)



# cách sửa
transaction ="nguyEN vAn a | PYTHON-01 | 15000000 | paid "

transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].title()
course_code = parts [1]
amount = int(parts [2])
status = parts [3].upper()

print( "Học viên:", student_name)
print( "Khóa học:", course_code)
print("So tiên:", amount, "VND")
print("Trạng thái:", status)