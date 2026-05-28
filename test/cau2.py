# câu 2
password = '123'
count = 0
for i in range(3):
    password_input=input('nhập mk:')
    if( password_input ==password):
        print('đăng nhập thành công')
        count += 1
        break
    else:
        print("mật khẩu sai , vui lòng nhập lại")
print('tài khoản đã bị khóa')
    
