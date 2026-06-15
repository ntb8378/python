import logging

def menu():
    print("""
     ========== VÍ MOMO GIẢ LẬP ==========

            1. Nạp tiền vào ví

            2. Chuyển tiền

            3.  Xem số dư hiện tại

            4. Thoát chương trình 

===============================================
""")
def deposit(user_money):
    try:
        input_money = float(input("Nhập vào số tiền cần nạp: "))
        if user_money <= 0:
            print("Lỗi số tiền Âm!")
            logging. error(f"InvalidAmountError: Attempted to process {input_money}")
        else:
            user_money += input_money
            print(f"Nạp tiền thành công, số dư mới là: {user_money}.")
            logging. info(f"IDeposit successful: {input_money} VND. Current Balance: {user_money}")
    except Exception as e:
        print("Lỗi: vui lòng nhập số tiền hợp lệ!")

def transfer(user_money):
    phone_number = input("nhập vào số điện thoại người nhận: ")
    if not phone_number.isdigit() and len(phone_number) != 10:
        print("số điện thoại không hợp lệ!")
        return
    try:
        payment = float("số tiền cần chuyển: ")
        if payment > user_money:
            print("giao dịch thất bại, số dư của bạn không đủ!")
            raise ValueError("lỗi số dư không đủ")
    except ValueError:
        print("Lỗi định dạng dữ liệu!")
    except Exception as InsufficientBalanceError:
        print(f"Loi: {InsufficientBalanceError}")

def main():
    user_money = 0
    while True:
        menu()
        choice = input("nhập lựa chọn: ")
        match choice:
            case "1":
                deposit(user_money)
            case "2":
                transfer(user_money)
            case "3":
                pass
            case "4":
                print("đã thoát!")
                break
            case _:
                print("lựa chọn không hợp lệ!")
main()
