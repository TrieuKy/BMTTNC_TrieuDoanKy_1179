#Dem so lan xuat hien cua tung phan tu trong mot list va luu ket qua vao mot dictionary
def DemSoLanXuatHien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_str = input("Nhap mot list cac tu, phan cach boi dau ',': ")
word_list =input_str.split(',')
so_lan_xuat_hien = DemSoLanXuatHien(word_list)
print("So lan xuat hien cua tung tu trong list la: ", so_lan_xuat_hien)