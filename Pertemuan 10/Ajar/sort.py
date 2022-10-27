def sort():
  # l= [2,12,5,10,-1,-5,6,34,55,20,-10] 
  l=[5,6,3,2,4,1]
  print("List array : ",l)
  # angka_element= int(input("Masukkan Jumlah Element "))
  # for k in range(0,angka_element):
  #   ele = int(input("Masukkan list angka "))
  #   l.append(ele)
  
  for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
      if(l[i]>l[j]):
        l[i],l[j] = l[j],l[i]
    print("List ke-",i," ", l)
  print("Hasil Sort ",l)
  
sort()