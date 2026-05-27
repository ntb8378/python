max=0 ; min=0
sum_invoice= int(input('nhập số lượng hóa đơn trong ca:'))
for i in range(1,sum_invoice + 1):
    invoice_value=int(input(f'nhập giá trị hóa đơn thứ {i}:'))
    if(i==0):
        min=invoice_value
    if(invoice_value>max):
        max=invoice_value
    if(invoice_value<min):
        min=invoice_value

print(f"hóa đơn có giá trị cao nhất: {max}")
print(f"hóa đơn có giá trị thấp nhất: {min}")


