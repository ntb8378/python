print(' --- HỆ THỐNG TIEP NHẬN BỆNH NHÂN --- ');
name_patient = input( 'Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input ('Mời bạn nhập triệu chứng bênh: ');

print(' - PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:', symptom);
print('Tuổi:', name_patient);
print ('Triệu chứng:', age);

# code này không lỗi cú pháp , nhưng sai về logic , các câu lệnh được gọi không đúng chỗ
# tên bệnh nhân nhưng lại gọi biến triệu chứng , tuổi thì gọi tên , triệu chứng thì gọi tuổi
# nó bị ngược 

# cách sửa đúng
print(' --- HỆ THỐNG TIEP NHẬN BỆNH NHÂN --- ');
name_patient = input( 'Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input ('Mời bạn nhập triệu chứng bênh: ');

print(' - PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:', name_patient);
print('Tuổi:',age );
print ('Triệu chứng:',symptom );
