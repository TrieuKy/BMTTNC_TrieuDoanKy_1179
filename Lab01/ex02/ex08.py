#Nhap chuoi so nhi phan 4 chu so phan cach bang dau ','. Kiem tra xem co chia het cho 5, in ra so dung phan cach boi dau ','
def ChiaHetCho5(SoNhiPhan):
    SoThapPhan = int(SoNhiPhan, 2)
    if SoThapPhan % 5 == 0:
        return True
    else:
        return False
ChuoiSoNhiPhan = input("Nhap chuoi so nhi phan 4 chu so phan cach bang dau ',': ")
SoNhiPhanList = ChuoiSoNhiPhan.split(',')
SoChiaHetCho5 = [so for so in SoNhiPhanList if ChiaHetCho5(so)]
if len(SoChiaHetCho5) > 0:
    print("Cac so nhi phan chia het cho 5: " + ','.join(SoChiaHetCho5))
else:
    print("Khong co so nhi phan nao chia het cho 5.")   