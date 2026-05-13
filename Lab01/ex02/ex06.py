#Nhap X Y, tao mang 2 chieu, hang i cot j la i*j, i chay tu 0 toi X-1 va j chay tu 0 toi Y-1
input_str= input("Nhap X Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)