from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self):
        self.__odometer = 0

    @property
    def odometer(self):
        return self.__odometer

    @abstractmethod
    def calculate_efficiency(self):
        pass

    def drive(self, distance):
        if distance <= 0:
            raise ValueError("Số km phải lớn hơn 0")
        self.__odometer += distance

    def __lt__(self, other):
        return self.odometer < other.odometer

    @staticmethod
    def validate_license_plate(plate):
        return len(plate) == 9 and plate.startswith("29")


class AutonomousFeature:
    def calculate_efficiency(self):
        return 95.0


class ElectricBus(BaseVehicle):
    def __init__(self):
        super().__init__()

    def calculate_efficiency(self):
        result = 100 - (self.odometer * 0.005)
        if result < 50:
            return 50.0
        return result


class RoboBus(ElectricBus, AutonomousFeature):
    def __init__(self):
        super().__init__()

    def calculate_efficiency(self):
        electric_eff = ElectricBus.calculate_efficiency(self)
        auto_eff = AutonomousFeature.calculate_efficiency(self)
        return (electric_eff + auto_eff) / 2


     
    def khoitao():
        while True:
            plate = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ")
            if BaseVehicle.validate_license_plate(plate):
                print("[Thành công]: Khởi tạo xe thành công!")
                print("[MRO Architecture]:")

                for cls in RoboBus.__mro__:
                    print(cls.__name__)
                return RoboBus()
            else:
                print("Biển số không hợp lệ, vui lòng nhập lại.")


def menu():
    print("""
==== SMART TRANSIT MENU ====
1. Khởi tạo & Đăng ký xe lai RoboBus mới
2. Giả lập vận hành & Kiểm tra hiệu suất
0. Thoát
""")


def main():
    current_vehicle = None
    while True:
        menu()
        choice = input("Chọn chức năng (1-2): ")
        match choice:
            case "1":
                current_vehicle= RoboBus.khoitao()
            case "2":
                pass
            case "0":
                print("Thoát chương trình.")
                break
            case _:
                print("Lựa chọn không hợp lệ!")


main()