def linear_Search(list, key):  
    # Searching list1 sequentially  
    n = len(DataList)  
    for i in range(0, n):  
        if (list[i] == key):  
            print(list[i])
            return i  
    return -1  
  
  
DataList = [2,12,5,10,-1,-5,6,34,55,20,-10] 
print("List Array : ",DataList,"\n")
cari = int(input("Masukkan Angka Yang Anda Cari : "))
# cari = 2
res = linear_Search(DataList, cari)  

if(res == -1):  
    print("Angka Tidak ditemukan")  
else:  
    print('Angka ditemukan. Angka %s ada di index %s'% (cari,res))
    