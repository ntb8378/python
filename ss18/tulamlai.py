def menu():
    print("="*60)
    print("1. Hiển thị danh sách cầu thủ\n" +
          "2. Tiếp nhận cầu thủ mới\n" +
          "3. Cập nhật thông tin và chỉ số\n" +
          "4. Xóa cầu thủ\n" +
          "5. Tìm kiếm cầu thủ\n" +
          "6. Thống kê loại phong độ\n" +
          "7. Đánh giá phong độ tự động\n" +
          "8. Thoát!")
    print("="*60)

def render_list(player_list):
    if not player_list:
        print("danh sách rỗng!")
    else:
        print(f"{"Mã CT":<5} | {"Họ tên":<20} | {"Số trận":<10} | {"Bàn thắng":<10} | {"Kiến tạo":<10} | {"Điểm hiệu suất":<20} | {"Phân loại phong độ":<20}")
        for item in player_list:
            print("-"*120)
            print(f"{item.get('id'):<5} | {item.get('name'):<20} | {item.get('match'):<10} | {item.get('win'):<10} | {item.get('assist'):<10} | {item.get('per'):<20} | {item.get('rank'):<20}")
        print("-"*120)


def check_str(prompt):
    while True:
        value= input(prompt).strip()
        try:
            if value == "":
                print("không được để trống!")
                continue
        except ValueError:
            print("sai định dạng")
        return value
    
def check_int(prompt):
    while True:
        try:
            value= int(input(prompt))
            if value <=0:
                print("phải lớn hơn 0!")
                continue
        except ValueError:
            print("sai định dạng")
        return value

def rank_for_per(per_math):
        if per_math < 15:
            return "Cần thanh lý"
        elif per_math < 30:
            return "Dự bị chiến lược"
        elif per_math < 50:
            return "Trụ cột đội bóng"
        else:
            return "Ngôi sao đẳng cấp"

def input_new_player(player_list):
    while True:
        input_id = check_str("nhập mã cầu thủ:").upper()
        for item in player_list:
            if (input_id.lower() == item.get("id").lower()):
                print("id đã tồn tại!")
                break
        else:
            input_name = check_str("nhập tên cầu thủ:")
            input_match = check_int("nhập số trận đấu:")
            input_win = check_int("nhập số bàn thắng:")
            input_assist = check_int("nhập bàn kiến tạo:")
            per_math = (input_match * 1) +(input_win * 3)+(input_assist *2)
            
            list_new={"id": input_id,
                    "name": input_name,
                        "match": input_match,
                        "win": input_win ,
                            "assist": input_assist,
                            "per": per_math,
                                "rank": rank_for_per(per_math)}
            player_list.append(list_new)
            print("đã thêm thành công!")
            break

def update_player(player_list):
    search_id = check_str("nhập mã CT cần cập nhật:")
    for item in player_list:
        if (search_id.lower() == item.get("id").lower()):
            update_match = check_int("nhập lại số trận:")
            update_win = check_int("nhập lại số bàn thắng:")
            update_assist = check_int("nhập lại số bàn kiến tạo")
            per_math = (update_match * 1) +(update_win * 3)+(update_assist *2)
                        
            item["match"] = update_match
            item["win"] = update_win
            item["assist"] = update_assist
            item["per"] = per_math
            item["rank"] = rank_for_per(per_math)

            print("đã cập nhật thành công!")
            break
    else:
        print(f"Không tìm thấy mã {search_id}")

def remove_player(player_list):
    search_id = check_str("nhập mã CT cần xóa:")
    for item in player_list:
        if (search_id.lower() == item.get("id").lower()):
            confirm = input(f"bạn có muốn xóa {search_id} không? (Y/N)")
            print(confirm)
            if confirm.lower() == "y":
                player_list.remove(item)
                print("đã xóa!")
            break
    else:
        print(f"Không tìm thấy mã {search_id}")
            
def search_player(player_list):
    finding = False
    search = check_str("nhập tên hoặc id cầu thủ cần tìm:")
    for item in player_list:
        if (search.lower() in item.get("name").lower() or search.lower() == item.get("id").lower()):
            finding = True
            print(f"phong độ của cầu thủ {item.get("name")} : {item.get("rank")}")
    if finding == False:
        print("không tìm thấy cầu thủ")

def render_rank(player_list):
    player_star = 0
    player_core = 0
    player_mechalin = 0
    player_buy = 0
    if not player_list:
        print("danh sách rỗng!")
    else:
        print(f"{"Ngôi sao":<10} | {"Trụ cột":<10} | {"Dự bị":<10} | {"Cần thanh lý":<10}")
        for item in player_list:
            if item.get("rank") == "Ngôi sao đẳng cấp":
                player_star += 1
            elif item.get("rank") == "Trụ cột đội bóng":
                player_core += 1
            elif item.get("rank") == "Dự bị chiến lược":
                player_mechalin += 1
            else:
                player_buy += 1
            


        print("-"*120)
        print(f"{player_star:<10} | {player_core:<10} | {player_mechalin:<10} | {player_buy:<10}")
        print("-"*120)

def auto_fill_rank(player_list):
    for item in player_list:
        per_math = (item.get("match") * 1) +(item.get("win")*3)+(item.get("assist")*2)
        item["per"]= per_math
        item["rank"]=rank_for_per(per_math)
    print("đã cập nhật rank thành công!")

def main():
    player_list=[
        {"id": "CT001", "name": "Bảo", "match": 10, "win": 9, "assist": 8, "per": 100, "rank": "Ngôi sao đẳng cấp"}
    ]
    while True:
        menu()
        choice = input("nhập lựa chọn:")
        print(choice)
        match choice:
            case "1":
                render_list(player_list)
            case "2":
                input_new_player(player_list)
            case "3":
                update_player(player_list)
            case "4":
                remove_player(player_list)
            case "5":
                search_player(player_list)
            case "6":
                render_rank(player_list)
            case "7":
                auto_fill_rank(player_list)
            case "8":
                print("đã thoát chương trình")
                break
            case _:
                print("lựa chọn không hợp lệ")
main()