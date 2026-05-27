total=0
count =0
day=0
for i in range(1,8):
    doanhthu=int(input(f'nhập doanh thu ngày {i}:'))
    day+= 1
    total=total+doanhthu
    if(doanhthu >= 5000000):
        count += 1
print(f"tổng doanh thu cả tuần: {total}")
print(f"doanh thu trung bình mỗi ngày trong tuần: {total/day}")
print(f'số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND): {count} ngày')
