import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {
        "name": "Phin Sữa Đá",
        "price": 35000
    },
    "F1": {
        "name": "Freeze Trà Xanh",
        "price": 55000
    },
    "T1": {
        "name": "Trà Sen Vàng",
        "price": 45000
    }
}


def view_menu():
    """Hiển thị thực đơn."""

    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, drink in DRINK_MENU.items():
        print(
            f"[{code}] - "
            f"{drink['name']} - "
            f"{drink['price']:,} VNĐ"
        )


def add_to_order(current_order):
    """Thêm món vào giỏ hàng."""

    print("\n--- THÊM MÓN VÀO GIỎ ---")

    drink_code = input(
        "Nhập mã đồ uống: "
    ).strip().upper()

    if drink_code not in DRINK_MENU:

        logging.warning(
            f"ItemNotFoundError - Code: {drink_code}"
        )

        print(
            "Mã đồ uống không hợp lệ, "
            "vui lòng kiểm tra lại thực đơn!"
        )

        return

    try:
        quantity = int(
            input("Nhập số lượng: ")
        )

        if quantity <= 0:

            logging.warning(
                f"InvalidQuantityError - Quantity: {quantity}"
            )

            raise ValueError(
                "Số lượng phải lớn hơn 0!"
            )

        current_order.append(
            {
                "code": drink_code,
                "quantity": quantity
            }
        )

        logging.info(
            f"Added {quantity} of "
            f"{drink_code} to order"
        )

        print(
            f"Đã thêm {quantity} x "
            f"{DRINK_MENU[drink_code]['name']} "
            f"vào giỏ hàng."
        )

    except ValueError as e:

        if "invalid literal" in str(e):

            logging.error(
                "ValueError - Invalid quantity input"
            )

            print(
                "Vui lòng nhập số lượng "
                "là một số nguyên!"
            )

        else:
            print(e)


def calculate_total(current_order):
    """Tính tổng tiền."""

    total = 0

    for item in current_order:

        code = item["code"]

        quantity = item["quantity"]

        total += (
            DRINK_MENU[code]["price"]
            * quantity
        )

    return total


def view_order(current_order):
    """Hiển thị giỏ hàng."""

    if not current_order:

        print(
            "Giỏ hàng trống, "
            "vui lòng chọn món (Chức năng 2)."
        )

        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")

    print(
        "Mã SP | Tên đồ uống | "
        "Đơn giá | Số lượng | Thành tiền"
    )

    total = 0

    for item in current_order:

        code = item["code"]

        quantity = item["quantity"]

        drink = DRINK_MENU[code]

        amount = (
            drink["price"]
            * quantity
        )

        total += amount

        print(
            f"{code} | "
            f"{drink['name']} | "
            f"{drink['price']:,} | "
            f"{quantity} | "
            f"{amount:,} VNĐ"
        )

    print("-" * 60)

    print(
        f"Tổng tiền cần thanh toán: "
        f"{total:,} VNĐ"
    )


def checkout(current_order):
    """Thanh toán đơn hàng."""

    if not current_order:

        print(
            "Giỏ hàng trống, "
            "vui lòng chọn món (Chức năng 2)."
        )

        return

    total = calculate_total(current_order)

    print("\n--- THANH TOÁN ---")

    print(
        f"Tổng tiền cần thanh toán: "
        f"{total:,} VNĐ"
    )

    confirm = input(
        f"Xác nhận thanh toán "
        f"{total:,} VNĐ? (y/n): "
    ).lower()

    if confirm == "y":

        logging.info(
            "Checkout successful"
        )

        current_order.clear()

        print("Thanh toán thành công.")
        print("Giỏ hàng đã được làm trống.")

    elif confirm == "n":

        print(
            "Đã hủy thao tác thanh toán."
        )

    else:

        print(
            "Lựa chọn không hợp lệ. "
            "Thanh toán đã bị hủy."
        )