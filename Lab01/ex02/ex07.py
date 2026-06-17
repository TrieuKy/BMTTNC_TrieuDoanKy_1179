#Nhan cac chuoi dau vao la dong duoc nhap, sau do chuyen thanh chu Hoa va in ra
print("Nhap cac dong van ban( Nhap 'done' de ket thuc): ")
lines=[]
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    print("Cac dong van ban da nhap sau khi chuyen thanh chu Hoa: ")
    for line in lines:
        print(line.upper())