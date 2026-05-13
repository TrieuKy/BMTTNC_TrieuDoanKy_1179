#truy cap cac phan tu dau tien ca cuoi cung tron Tuple
def truyCapPhanTu(tupledata):
    first_element = tupledata[0]
    last_element = tupledata[-1]
    return first_element, last_element
input_tuple = input("Nhap mot tuple cac so nguyen, phan cach boi dau ',': ")
first, last = truyCapPhanTu(input_tuple)
print("Phan tu dau tien: ", first)
print("Phan tu cuoi cung: ", last)