# bởi vì thứ tự vòng lạp đang bị sai nên không hiển thị đúng như mong muốn
# phải lạp chi nhánh trước rồi mưới tới tháng

# cách sửa

branch_count = int(input("Nhập số lượng chi nhánh: "))

# duyệt từng chi nhánh
for branch in range(1, branch_count + 1):

    # duyệt từng tháng
    for month in range(1, 4):

        revenue = int(input(
            f"Nhập doanh thu chi nhánh {branch}, tháng {month}: "
        ))

        print(
            f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng"
        )