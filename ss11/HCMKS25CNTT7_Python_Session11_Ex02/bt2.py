# Dictionary employee gồm những key: "employee_id": "NV001","full_name","department","status"
# employee_id = employee[0] gây lỗi vì: không thể truy cập dữ liệu theo vị trí
# Muốn lấy mã nhân viên "NV001", cần viết: employee["employee_id"]
# full_name = employee["name"] dòng này lỗi vì sai tên key phải là employee["full_name"]
# employee["employee_status"] = "official" không cập nhật đúng giá trị của nhân viên vì: sai tên key phải là :employee["status"] = "official" 
# employee.append("base_salary", 15000000) gây lỗi bởi vì: dict không sử dụng được append
# Muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh employee["base_salary"]= 15000000 thì nó sẽ tự thêm vào 
# xóa phòng ban thì del employee["department"]  , cái kia sai bởi vì sai tên key


employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}
employee_id= employee["employee_id"]

full_name = employee["full_name"]

employee["status"] = "official"

employee["base_salary"]= 15000000

del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)