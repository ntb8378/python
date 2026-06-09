raw_logs = []
processed_logs = []
def menu():
    menu = ("""
============= SECURITY LOG ANALYZER =============
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
=================================================
""")
    print(menu)
menu()


def input_fresh():
    global raw_logs
    
    print("--- NẠP DỮ LIỆU LOG ---")
    input_value = input("Nhập chuỗi log thô (cách nhau bởi dấu ;):")
    remove_key = input_value.maketrans("","","!@#$")
    clean_input = input_value.translate(remove_key)

    raw_logs = clean_input.split(";")
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống")

def caution_log():
    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
    else:
        print("--- LỌC CẢNH BÁO ---")
        processed_logs = [
            log for log in raw_logs
            if "ERROR".lower() in log.lower() or "CRITICAL".lower() in log.lower()
        ]
        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")

        for log in processed_logs:
            print(log)

def encoding_value():
    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
    else:
        print("--- MÃ HÓA IP ---")
        safe_logs = []
        for log in raw_logs:
            words = log.split()
            for i in range(len(words)):
                if "." in words[i]:
                    ip_parts = words[i].split(".")
                    if len(ip_parts) == 4:
                        ip_parts[2] = "*"
                        ip_parts[3] = "*"
                        words[i] = ".".join(ip_parts)
            safe_logs.append(" ".join(words))
        print("Báo cáo log an toàn:")
        for i in range(len(safe_logs)):
            print(f"{i + 1}. {safe_logs[i]}")
        return safe_logs

def main():
    while True:
        choice = input("Chọn chức năng (1-4):")
        match choice:
            case "1":
                input_fresh()
                print(raw_logs) 
            case "2":
                caution_log()
            case "3":
                encoding_value()
            case "4":
                print("Đã đóng hệ thống!")
                break
main()
