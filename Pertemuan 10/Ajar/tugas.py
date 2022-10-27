# def sort():
#   l= []
#   angka_element= int(input("Masukkan Jumlah Element : "))
  
#   for k in range(0,angka_element):
#     ele = int(input("Masukkan list angka : "))
#     l.append(ele)
    
#   print("\nList Array : ",l)
#   for i in range(0,len(l)-1):
#     for j in range(i+1,len(l)):
#       if(l[i]>l[j]):
#         l[i],l[j] = l[j],l[i]
#     print("Sorting ke-%s : %s"%(i,l))
#   print("Sorted List ")
#   print(l)
  
# sort()

# angka = [5,2,3,1,4]
# jumlah  = len(angka)



angka = []
jml_angka = int(input("Masukkan Jumlah Element : "))
for i in range(0, jml_angka):
  list = int(input("Masukkan list angka : "))
  angka.append(list)
print("\n")

def bubblesort(arr):
    print("List Array : ",arr)
    n = len(arr)
    for i in range(n-1):
      for j in range(0,n-i-1):
        if arr[j]> arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
      print("Sorting ke-",i,": ",arr)
    print("Sorted List :",arr)
    
    # for i in range(len(arr)):
    #   print("%d" %arr[i],end=" ")
bubblesort(angka)



