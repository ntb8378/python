class NetflixAccount:
    platform_name = "Netflix"
    max_profiles = 5 
    
    def __init__(self,email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        return "********"
    
    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("mật khẩu phải lớn hơn 5 ký tự!")
        self.__password = new_password

    @property
    def plan(self):
        return self.__plan
    
    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        return False
    
    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return
        self.profiles.append(profile_name)

    def upgrade_plan(self, new_plan):
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
        else:
            print("Gói cước không hợp lệ")

    def display_info(self):
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Plan: {self.plan}")
        print(f"Profiles: {self.profiles}")

def main():
    current_account = None
    while True:
        choice = input("""
===== NETFLIX ACCOUNT MANAGER =====
1. Đăng ký tài khoản mới
2. Xem thông tin tài khoản
3. Thêm người xem
4. Nâng cấp gói cước
5. Cập nhật chính sách Netflix
6. Thoát chương trình
===================================
Chọn chức năng:
""")
        match choice:
            case "1":

                email = input("Nhập email: ")

                if not NetflixAccount.validate_email(email):
                    print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                    continue

                password = input("Nhập mật khẩu: ")

                try:
                    current_account = NetflixAccount(email)
                    current_account.password = password

                    print("Đăng ký tài khoản thành công!")

                except ValueError as e:
                    print(e)

            # Xem thông tin
            case "2":

                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                else:
                    current_account.display_info()

            # Thêm profile
            case "3":

                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                else:
                    profile_name = input("Nhập tên Profile: ")

                    current_account.add_profile(profile_name)

            # Nâng cấp gói
            case "4":

                if current_account is None:
                    print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
                else:

                    print("""
1. Basic
2. Standard
3. Premium
""")

                    plan_choice = input("Chọn gói cước: ")

                    if plan_choice == "1":
                        current_account.upgrade_plan("Basic")

                    elif plan_choice == "2":
                        current_account.upgrade_plan("Standard")

                    elif plan_choice == "3":
                        current_account.upgrade_plan("Premium")

                    else:
                        print("Lựa chọn không hợp lệ")

            # Đổi chính sách Netflix
            case "5":

                try:
                    new_limit = int(input("Nhập giới hạn Profile mới: "))

                    NetflixAccount.update_max_profiles(new_limit)

                    print(
                        f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}"
                    )

                except ValueError:
                    print("Vui lòng nhập số nguyên")

            # Thoát
            case "6":
                print("Cảm ơn bạn đã sử dụng chương trình")
                break

            case _:
                print("Lựa chọn không hợp lệ")