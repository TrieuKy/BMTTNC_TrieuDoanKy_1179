#tao mot Tuple tu mot list nhap vao tu ban phim
def taoTupleTuList(lst):
    return tuple(lst)
inputlist = input("Nhap mot list cac so nguyen, phan cach boi dau ',': ")
numbers = list(map(int, inputlist.split(',')))
mytuple = taoTupleTuList(numbers)
print("List: ",numbers)
print("Tuple: ",mytuple)