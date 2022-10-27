def linear_search(list,key):
  n = len(DataList)
  for i in range(0,n):
    if(list[i] == key):
      print(list[i])
      return i
  return -1
  # i -=1
  # i --1
  
DataList = [1,3,2,5,4]
cari = 6
print("Array : ", DataList) 

result = linear_search(DataList,cari)
print("Angka ditemukan. Angka %s ada di index %s "%(cari, result))