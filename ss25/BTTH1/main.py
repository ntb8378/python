class BankAccount:
    bank_name= "Vietcombank"
    transaction_fee= 2000

    def __init__(self,account_number,account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    @property
    def get_account_name(self):
        return self.account_name
    @get_account_name.setter
    def set_account_name(self, new_name: str):
        self.account_name = new_name.strip().upper()
    @staticmethod
    def validate_account_number(account_number: str):
        if account_number.isdigit() and len(account_number) == 10:
            return True
        else: 
            return False
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self,amount):
        total = amount + self.transaction_fee
        if self.__balance < total :
            print("số dư không đủ")
        else:
            self.__balance -= total
    def display_info(self):
        print(f"Tên ngân hàng:{self.bank_name}")
        print(f"Số TK:{self.account_number}")
        print(f"Tên chủ TK:{self.get_account_name}")
        print(f"Số dư hiện tại{self.balance}")



def main():
    current_account = None
    while True:
        choice = int(input("""===== VIETCOMBANK DIGIBANK SIMULATOR =====
                        1. Mở tài khoản mới
                        2. Xem thông tin tài khoản
                        3. Giao dịch Nạp / Rút tiền
                        4. Cập nhật Tên chủ tài khoản
                        5. Đổi phí giao dịch hệ thống
                        6. Thoát chương trình
                        ==========================================
                        Chọn chức năng (1-6):"""))
        match choice:
            case 1:
               new_account = None
               while True: 
                   number_bank_account = input("nhập vào số TK: ")
                   account_new_name = input("nhập vào Tên TK: ")
                   if BankAccount.validate_account_number(number_bank_account):
                        new_account = BankAccount(number_bank_account, account_new_name)
                        current_account = new_account
                        print("Đã thêm tài khoản mới thành công")
                        break
                   else: 
                       print("STK không hợp lệ")
            case 2:
                if current_account is None:
                    print("Vui lòng mở tài khoản (Chức năng 1) trước")
                else: 
                    current_account.display_info()
            case 3:
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản")
                else:
                    print("1. Nạp tiền")
                    print("2. Rút tiền")

                    transaction_choice = input("Chọn loại giao dịch: ")

                    amount = int(input("Nhập số tiền: "))

                    if transaction_choice == "1":
                        current_account.deposit(amount)
                        print("Nạp tiền thành công")

                    elif transaction_choice == "2":
                        current_account.withdraw(amount)
            case 4:
                if current_account is None:
                    print("Hệ thống chưa có thông tin tài khoản")
                else:
                    new_name = input("Nhập tên mới: ")

                    current_account.set_account_name = new_name

                    print("Cập nhật thành công")
            case 5:
                new_fee = int(input("Nhập phí giao dịch mới: "))

                BankAccount.update_transaction_fee(new_fee)

                print("Đã cập nhật phí giao dịch")
            case 6:
                print("Cảm ơn bạn đã sử dụng chương trình")
                break
                        
main()