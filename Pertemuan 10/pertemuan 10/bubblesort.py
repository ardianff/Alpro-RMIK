def bubbleSort(arr):
  arr =[1,5,3,2,4]
  print("List Array : ",arr)
  n = len(arr) 
  swapped = False
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("List Array ke-",i," ", arr)

  print("Hasil Sorting :")
  for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
arr = []
bubbleSort(arr)