#Xoa mot phan tu tu dictonary theo key da cho
def xoaPhanTu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict={'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = input("Nhap key can xoa: ")
if xoaPhanTu(my_dict, key_to_delete):
    print("Phan tu co key '{}' da duoc xoa.".format(key_to_delete))
else:
    print("Key '{}' khong ton tai trong dictionary.".format(key_to_delete))