class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.id = id
        self.name = name
        self.theory_score = theory_score
        self.practice_score = practice_score
        self.project_score = project_score
        self.final_score = 0
        self.academic_rank = ""

    def calculate_final_score(self):
        self.final_score = (self.theory_score * 0.2) + (self.practice_score * 0.3) + (self.project_score * 0.5)

    def classify_academic_rank(self):
        if self.final_score >= 8.5:
            self.academic_rank = "Giỏi"
        elif self.final_score >= 7:
            self.academic_rank = "Khá"
        elif self.final_score >= 5:
            self.academic_rank = "Trung bình"
        else:
            self.academic_rank = "Yếu"

class StudentManager:
    def __init__(self):
        self.students : list = []

    def show_all(self):
        if not self.students:
            print("danh sách rỗng!")
        else:
            print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<20} | {'Điểm Thực Hành':<20} | {'Điểm Đồ Án':<20} | {'Điểm Tổng Kết':<20} | {'Học Lực':<10}")
            for i in self.students:
                print(f"{i.id:<10} | {i.name:<20} | {i.theory_score:<20} | {i.practice_score:<20} | {i.project_score:<20} | {i.final_score:<20.2f} | {i.academic_rank:<10}")
            
    def add_student(self):
        input_id = input("nhập Mã SV: ")
        if not input_id:
            print("Mã SV không được để trống!")
            return
        for i in self.students:
            if input_id == i.id:
                print("Mã sinh viên này đã tồn tại trong dnah sách!")
                return
        input_name = input("nhập tên SV: ")
        if not input_name:
            print("Tên SV không được để trống!")
            return
        input_theory_score = float(input("nhập điểm lý thuyết: "))
        if (input_theory_score <0 or input_theory_score >10):
            print("điểm chỉ nằm trong khoảng 0 đến 10")
            return
        input_practice_score = float(input("nhập điểm thực hành: "))
        if (input_practice_score <0 or input_practice_score >10):
            print("điểm chỉ nằm trong khoảng 0 đến 10")
            return
        input_project_score = float(input("nhập điểm đồ án: "))
        if (input_project_score <0 or input_project_score >10):
            print("điểm chỉ nằm trong khoảng 0 đến 10")
            return

        new_students= Student(input_id, input_name, input_theory_score, input_practice_score, input_project_score)
        new_students.calculate_final_score()
        new_students.classify_academic_rank()
        self.students.append(new_students)
        print("đã thêm thành công!")

    def update_student(self):
        search_id = input("Nhập Mã SV cần sửa: ")
        found = False
        for i in self.students:
            if (search_id == i.id):
                found = True
                new_theory_score = float(input("nhập vào điểm lý thuyết mới: "))
                if new_theory_score < 0 or new_theory_score > 10:
                    print("Điểm chỉ nằm trong khoảng 0 đến 10")
                    return

                new_practice_score = float(input("nhập vào điểm thực hành mới: "))
                if new_practice_score < 0 or new_practice_score > 10:
                    print("Điểm chỉ nằm trong khoảng 0 đến 10")
                    return

                new_project_score = float(input("nhập vào điểm đồ án mới: "))
                if new_project_score < 0 or new_project_score > 10:
                    print("Điểm chỉ nằm trong khoảng 0 đến 10")
                    return

                i.theory_score = new_theory_score
                i.practice_score = new_practice_score
                i.project_score = new_project_score
                i.calculate_final_score()
                i.classify_academic_rank()

                print("cập nhật thành công!")
                break

        if not found:
            print("không tìm thấy Mã SV này!")