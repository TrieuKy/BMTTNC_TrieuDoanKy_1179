#Viet ham nhan vao mot chuoi va tra ve dao nguoc cua chuoi do
def DaoNguocChuoi(chuoi):
    return chuoi[::-1]      
input_str = input("Nhap mot chuoi: ")
print("Dao nguoc cua chuoi la: ", DaoNguocChuoi(input_str))