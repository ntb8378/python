class PTITStudent:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    def say_hi(self):
        print(f"Tôi là {self.name}, tôi chào cả lớp nha!")

# Tạo 1 method dùng để in ra xếp loại của sv dựa trên GPA
# GPA > 3.6 là sx, > 3.2 là giỏi, > 3.0 khá, cuối cùng là trung bình

    def rank_student(self):
        if self.gpa > 3.6:
            print(f"{self.name} thuộc loại suất xắc!")
        elif self.gpa > 3.2:
            print(f"{self.name} thuộc loại giỏi!")
        elif self.gpa > 3.0:
            print(f"{self.name} thuộc loại khá!")
        else:
            print(f"{self.name} thuộc loại trung bình!")

    @staticmethod
    def say_gb():
        print("tạm biệt")

student_rikkei = PTITStudent("Khiêm", 3.2)
student_tuxa = PTITStudent("Trứ", 3.7)
student_chinhquy = PTITStudent("Khoa", 4.0)

# print(student_rikkei.name , student_rikkei.gpa)

student_chinhquy.say_hi()
student_chinhquy.rank_student()
student_chinhquy.say_gb()
PTITStudent.say_gb()