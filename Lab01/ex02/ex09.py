#Kiem tra so nhap vao co phai so nguyen to hay ko
def KiemTraSoNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhap mot so nguyen: "))
if KiemTraSoNguyenTo(number):
    print(number, "la so nguyen to.")
else:
    print(number, "khong la so nguyen to.")
     