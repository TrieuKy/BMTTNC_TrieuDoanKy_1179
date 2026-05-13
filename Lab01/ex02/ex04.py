#Tim tat ca so tu 2000 den 3200 chia het cho 7 va khong phai la boi cua 5
j=[]
for i in range(200,3201,1):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))