class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = ""

    # cách getter private:(chỉ để lấy ra thôi) 
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def theory_score(self):
        return self.__theory_score
    @property
    def practice_score(self):
        return self.__practice_score
    @property
    def project_score(self):
        return self.__project_score
    @property
    def final_score(self):
        return self.__final_score
    @property
    def academic_rank(self):
        return self.__academic_rank
    
    # cách làm setter cho cập nhật có thể sửa:
    # hoặc k cần gọi setter làm cách nay cũng đc:
    def update_theory_score(self,theory_score):
        self.__theory_score = theory_score
    def update_practice_score(self,practice_score):
        self.__practice_score = practice_score
    def update_project_score(self,project_score):
        self.__project_score = project_score


    def calculate_final_score(self):
        self.__final_score = (self.__theory_score * 0.2)+(self.__practice_score*0.3)+(self.__project_score*0.5)

    def classify_academic_rank(self):
        if self.__final_score >= 8.5:
            self.__academic_rank = "Giỏi"
        elif self.__final_score >= 7:
            self.__academic_rank = "Khá"
        elif self.__final_score >= 5:
            self.__academic_rank = "Trung bình"
        else:
            self.__academic_rank = "Yếu"

class StudentManager:
    def __init__(self):
        self.students : list[Student] = []

    def find_id(self,id : str):
        for stu in self.students:
            if stu.id == id:
                return stu
            else: 
                return

    def add_student(self):
       stu_id = input("nhập MaSV: ")
       if not stu_id:
           print("không có mã SV") 
           return
       for stu in self.students:
           if stu.id == stu_id:
               print("mã SV đã tồn tại")
               return
       stu_name = input("nhập Tên SV:")
       if not stu_name:
            print("không có tên SV") 
            return
       
       stu_theory_score = float(input("nhập điểm lý thuyết: "))
       stu_practice_score = float(input("nhập điểm thực hành: "))
       stu_project_score = float(input("nhập điểm đồ án: "))

       if not stu_theory_score >= 0 and  stu_theory_score <= 10:
           print("điểm không hợp lệ")
       if not stu_practice_score >= 0 and  stu_practice_score <= 10:
            print("điểm không hợp lệ")
       if not stu_project_score >= 0 and  stu_project_score <= 10:
           print("điểm không hợp lệ")

       new_student = Student(stu_id,stu_name,stu_theory_score,stu_practice_score,stu_project_score)
       new_student.calculate_final_score()
       new_student.classify_academic_rank()
       self.students.append(new_student)
       print("thêm sinh viên thành công")


    def show_all(self):
        if not self.students:
            print("danh sách rỗng")
        else:
            print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<20} | {'Điểm Thực Hành':<20} | {'Điểm Đồ Án':<20} | {'Điểm Tổng Kết':<20} | {'Học Lực':<10}")
            for i in self.students:
                print(f"{i.id:<10} | {i.name:<20} | {i.theory_score:<20} | {i.practice_score:<20} | {i.project_score:<20} | {i.final_score:<20} | {i.academic_rank:<10}")
            

    
        # cách 1
        # stu_id = input("nhập mã SV cần cập nhật: ")
        # if self.find_id(stu_id):
        #     stu_theory_score = float(input("nhập điểm lý thuyết: "))
        #     stu_practice_score = float(input("nhập điểm thực hành: "))
        #     stu_project_score = float(input("nhập điểm đồ án: "))
        #     if not stu_theory_score >= 0 and  stu_theory_score <= 10:
        #         print("điểm không hợp lệ")
        #         return
        #     if not stu_practice_score >= 0 and  stu_practice_score <= 10:
        #             print("điểm không hợp lệ")
        #             return
        #     if not stu_project_score >= 0 and  stu_project_score <= 10:
        #         print("điểm không hợp lệ")
        #         return
        #     student = self.find_id(stu_id)
        #     student.theory_score(stu_theory_score)
        #     student.practice_score(stu_practice_score)
        #     student.project_score(stu_project_score)
# xem lại và sửa cái project_score



# cách 2
    def update_student(self):
        stu_id = input("nhập mã SV cần cập nhật: ")
        for stu in self.students:
            if stu.id == stu_id:
                stu_theory_score = float(input("nhập điểm lý thuyết: "))
                stu_practice_score = float(input("nhập điểm thực hành: "))
                stu_project_score = float(input ("nhập điểm đồ án: "))
                if not stu_theory_score >= 0 and stu_theory_score <= 10:
                    print ("điểm không hợp lệ")
                    return
                if not stu_practice_score >= 0 and stu_practice_score <= 10:
                    print("điểm không hợp lệ")
                    return
                if not stu_project_score >= 0 and stu_project_score <= 10:
                    print("điểm không hợp lệ")
                    return
                stu.update_theory_score(stu_theory_score)
                stu.update_practice_score(stu_practice_score)
                stu.update_project_score(stu_project_score)
                stu.calculate_final_score()
                stu.classify_academic_rank()
                print("cập nhật thành công")
        else:
            print("không tìm thấy SV")
            return

    def delete_student(self):
        search = input("nhập tên hoặc id muốn xóa: ")
        found = False
        for i in self.students:
            if (i.id == search) or (search.lower() in i.name.lower()):
                found = True
                confirm = input("Bạn có chắc muốn xóa sinh viên này không? (Y/N): ")
                if confirm.lower() == "y":
                    self.students.remove(i)
                    return
        if not found:
            print("không tìm thấy sinh viên")

    def search(self):
        for i in self.students:
            if i.id == id:
                print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<20} | {'Điểm Thực Hành':<20} | {'Điểm Đồ Án':<20} | {'Điểm Tổng Kết':<20} | {'Học Lực':<10}")
                print(f"{i.id:<10} | {i.name:<20} | {i.theory_score:<20} | {i.practice_score:<20} | {i.__project_score:<20} | {i.__final_score:<20} | {i.__academic_rank:<10}")

        else: 
            print("không tìm thấy SV")
            return


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách sinh viên
2. Thêm sinh viên mới
3. Cập nhật thông tin sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên theo tên
6. Thoát
=====================================

""")
    
def main():
    student_manager = StudentManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                student_manager.show_all()
            case "2":
                student_manager.add_student()
            case "3":
                student_manager.update_student()
            case "4":
                student_manager.delete_student()
            case "5":
                student_manager.search()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý học tập!")
                break
            case _:
                print("lựa chọn không hợp lệ!")
main()