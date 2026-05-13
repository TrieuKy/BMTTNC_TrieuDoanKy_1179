#dao nguoc phan tu vi tri trong danh sach
def DaoNguocDanhSach(lst):
    return lst[::-1]
input_str = input("Nhap mot list cac so nguyen, phan cach boi dau ',': ")
numbers = list(map(int, input_str.split(',')))
listDaoNguoc = DaoNguocDanhSach(numbers)
print("Dao nguoc cua list la: ", DaoNguocDanhSach(numbers))