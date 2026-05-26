print (" -- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG -- ")

# Vòng Lặp chạy 3 Lần dể nhập Lương cho 3 nhân viên
for employee_number in range(1, 4):

# Khởi tạo chiếc hộp dựng tổng tiền
    total_budget = 0

    print ("Đang xử lý nhân vien số", employee_number)
    # Nhập mức Lương
    salary = int(input(" Nhập mức Lương (VNĐ): "))

    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp
    total_budget = total_budget + salary

# Sau khi nhập xong ca 3 người, in tổng tiền ra màn hình
print (" KET QUA: TONG NGAN SACH CAN CHUAN BI LA:", total_budget, "VND")

#  lỗi là biến total được đặt ngay trong vòng lập nên là mỗi lần rết vòng lập nó sẽ trả về số 0 ,
#  nên là nó chỉ nhận giá trị cuối cùng được nhận vào thôi
# cách sửa là để ra ngoài:

print (" -- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG -- ")

# Vòng Lặp chạy 3 Lần dể nhập Lương cho 3 nhân viên
# Khởi tạo chiếc hộp dựng tổng tiền
total_budget = 0
for employee_number in range(1, 4):


    print ("Đang xử lý nhân vien số", employee_number)
    # Nhập mức Lương
    salary = int(input(" Nhập mức Lương (VNĐ): "))

    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp
    total_budget = total_budget + salary

# Sau khi nhập xong ca 3 người, in tổng tiền ra màn hình
print (" KET QUA: TONG NGAN SACH CAN CHUAN BI LA:", total_budget, "VND")
