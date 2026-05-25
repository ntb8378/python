namePatient=input('nhập tên bệnh nhân:')
gender=input('nhập giới tính:')
dob=int(input('nhập năm sinh:'))
phone= input('nhập số điện thoại:')
email=input('nhập email:')
symptom= input('nhập triệu chứng ban đầu:')
price= float(input('nhập chi phí khám:'))

import random
ma_bn =  str(dob) + str(random.randint(100,999))

print("--- THẺ BỆNH NHÂN ---")
print("Mã BN      :", ma_bn)

print("Tên        :", namePatient, "(str)")
print("Giới tính  :", gender, "(str)")
print("Năm sinh   :", dob, "(int)")
print("Điện thoại :", phone, "(str)")
print("Email      :", email, "(str)")
print("Triệu chứng:", symptom, "(str)")
print("Chi phí    :", price, "VND (float)")