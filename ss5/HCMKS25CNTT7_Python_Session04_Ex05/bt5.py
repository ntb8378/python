while True:
    print("===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo")
    print("2. Hướng dẫn sử dụng")
    print("3. Thoát chương trình")
    choice=int(input("Nhập lựa chọn:"))
    if(choice==1):
        branch_count=int(input("Nhập số lượng chi nhánh:"))
        max_students=0
        max_branch=0
        for branch in range(1,branch_count+1):
            class_count=int(input(f"Nhập số lớp học của chi nhánh {branch}:"))
            total_students=0
            low_class=[]
            for classroom in range(1,class_count+1):
                while True:
                    student_count=int(input(f"Nhập số học viên lớp {classroom}:"))
                    if(student_count<0):
                        print("Số học viên không hợp lệ")
                    else:
                        break
                total_students+=student_count
                if(student_count<10):
                    low_class.append(classroom)
            print(f"Tổng số học viên chi nhánh {branch}:{total_students}")
            if(total_students>max_students):
                max_students=total_students
                max_branch=branch
            if(len(low_class)>0):
                print("Các lớp dưới 10 học viên:",end=" ")
                for classroom in low_class:
                    print(classroom,end=" ")
                print()
            else:
                print("Không có lớp nào dưới 10 học viên")
        print(f"Chi nhánh có nhiều học viên nhất là chi nhánh {max_branch}")
    elif(choice==2):
        print("\nHƯỚNG DẪN SỬ DỤNG")
        print("Nhập số lượng chi nhánh")
        print("Nhập số lớp học của từng chi nhánh")
        print("Nhập số học viên của từng lớp")
        print("Hệ thống sẽ thống kê tổng học viên")
        print("Kiểm tra lớp dưới 10 học viên")
    elif(choice==3):
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")