# bởi vì tạo biến tổng ở trên nên là sau mỗi lần lập nó sẽ cộng dồn vô
# giải pháp là tạo biến tổng trong vòng lập để khi mỗi vòng lập thì nó sẽ reset lại

# cách sửa

branch_count = int(input("Nhập sô lượng chi nhánh: "))
class_count = int(input("Nhập sô lớp học của môi chi nhánh: "))


for branch in range(1, branch_count + 1):
    total_students = 0
    print(f"\nChi nhánh {branch}")
    for classroom in range(1, class_count + 1):
        student_count = int( input(f"Nhập so học viên lớp {classroom}: "))
        total_students += student_count

    print(f"Chi nhánh {branch}: {total_students} học viên")