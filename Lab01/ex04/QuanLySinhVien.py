class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocluc = ""


class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxID = 1
        if self.soLuongSinhVien() > 0:
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxID < sv._id:
                    maxID = sv._id
            maxID += 1
        return maxID

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, id):
        sv = self.findByID(id)
        if sv != None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print("Cap nhat thong tin sinh vien thanh cong!")
        else:
            print("Sinh vien co ID = {} khong ton tai".format(id))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, id):
        searchResult = None
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv._id == id:
                    searchResult = sv
        return searchResult

    def findByName(self, name):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                # Sửa lỗi biến keyword thành name
                if name.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteByID(self, id):
        isDeleted = False
        sv = self.findByID(id)
        if sv != None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocluc = "Gioi"
        elif sv._diemTB >= 7:
            sv._hocluc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<12} {:<15} {:<10} {:<10}".format("ID", "Ten", "Gioi tinh", "Chuyen nganh", "Diem TB", "Hoc luc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<12} {:<15} {:<10} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
            print("\n")

    def getListSinhVien(self):
        return self.listSinhVien


# --- CHƯƠNG TRÌNH CHÍNH ---
qlsv = QuanLySinhVien()

while True:
    print("\n----- QUAN LY SINH VIEN -----")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien boi ID")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")

    key = int(input("Nhap lua chon: "))
    
    if key == 1:
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
        
    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Cap nhat thong tin sinh vien. ")
            ID = int(input("\nNhap ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")
            
    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xoa sinh vien.")
            ID = int(input("\nNhap ID: "))
            if qlsv.deleteByID(ID):
                print("\nSinh vien co id = ", ID, " da bi xoa.")
            else:
                print("\nSinh vien co id = ", ID, " khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")
            
    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("\nNhap ten de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
            
    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA). ")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
            
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
            
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
            
    elif key == 0:
        print("\nBan da chon thoat chuong trinh!")
        break
        
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")