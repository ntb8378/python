


# Lớp cha: Nhân vật cơ bản
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

# Lớp con: Chiến binh cận chiến
class Warrior(Character,):
    # def __init__(self, name, hp, attack_power, bonus_armor):
    def __init__(self, name, hp, attack_power,bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        return self.get_total_power() > other.get_total_power()


# --- KỊCH BẢN MATCHMAKING LỖI ---
# Tạo 2 đối tượng chiến binh
w1 = Warrior("Arthur", 1000, 150, 50)  # Sức mạnh tổng: 200
w2 = Warrior("Lancelot", 900, 180, 10) # Sức mạnh tổng: 190

# In thông báo xuất trận
print(f"Chiến binh {w1.name} xuất trận!")

# So sánh sức mạnh bằng toán tử >
if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")