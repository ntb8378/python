# Tuple product_info ban đầu có 4 phần tử
# Phần tử "SP001" đang nằm ở index 0
# dòng 'product_code = product_info[1]' lấy sai mã sản phẩm vì: gồm có 4 phần tử , vị trí của mã sản phẩm là thứ 1 nhưng index thì lại bắt đầu từ 0 nên nó phải là index 0

# Phần tử "Áo polo nam" đang nằm ở index 1
# dòng 'product_name = product_info[2]' lấy sai tên sản phẩm vì index nó phải là 1 mới đúng sửa lại là product_name = product_info[1]

# 'product_length = product_info.length()' xảy ra lỗi vì python k hỗ trợ .length , sửa lại là len(product_info)
# 'product_info[3] = 279000' dòng sau không hợp lệ vì tuple là kiểu dữ liệu bất biến , không thể chỉnh sửa , thêm và xóa 
# Muốn cập nhật giá bán từ 299000 thành 279000, cần phải tạo tuple mới luôn


# sửa lại code:
product_info = ("SP001", "Áo polo nam", "Size L", 299000)
product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)
product_info = ("SP001", "Áo polo nam", "Size L", 279000)
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)