#Tinh tong tat ca so chan trong mot list
def TongSoChan(lst):
    tong =0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
input_str = input("Nhap mot list cac so nguyen, phan cach boi dau ',': ")
numbers = [int(x) for x in input_str.split(',')]
TongChan = TongSoChan(numbers)
print("Tong cac so chan trong list la: ", TongChan)