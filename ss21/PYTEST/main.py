# Tạo 1 hàm để giảm giá sản phẩm trước khi thanh toán
def calculate_payment(amount : float, rate: float) -> float:
    if amount < 0:
    # print("Số tiền không được phép âm!")
        raise ValueError("Số tiền Âm")
        # 100.000 Giảm 10% -> 90.000
        # return amount * 1 + amount * rate
    return amount * (1 - rate)