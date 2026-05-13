#Tinh luong nhan vien, co ban 44h, sau 44h dc them 150%
soGioLam = float(input("Nhap so gio lam moi tuan: "))
luongGio = float(input("Nhap luong theo gio tieu chuan: "))
gioTieuChuan = 44
gioVuotChuan = max(0, soGioLam - gioTieuChuan)
thucLinh = (gioTieuChuan * luongGio) + (gioVuotChuan * luongGio * 1.5)
print("Luong thuc linh cua nhan vien la: ", thucLinh)   