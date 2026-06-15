import logging

from pos_logic import (
    view_menu,
    add_to_order,
    view_order,
    checkout
)


def menu():
    """Hiển thị menu chính."""

    print("""
========== HIGHLANDS MINI POS ==========
1. Xem thực đơn
2. Thêm món vào giỏ
3. Xem giỏ hàng & Tính tổng tiền
4. Thanh toán & Xóa giỏ hàng
5. Thoát ca làm việc
========================================
""")


def main():
    """Điều khiển chương trình."""

    current_order = []

    while True:

        menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        match choice:

            case "1":
                view_menu()

            case "2":
                add_to_order(
                    current_order
                )

            case "3":
                view_order(
                    current_order
                )

            case "4":
                checkout(
                    current_order
                )

            case "5":

                logging.info(
                    "Cashier logged out. "
                    "System shutdown."
                )

                print(
                    "Đã thoát ca làm việc. "
                    "Hẹn gặp lại!"
                )

                break

            case _:

                print(
                    "Lựa chọn không hợp lệ."
                )


if __name__ == "__main__":
    main()