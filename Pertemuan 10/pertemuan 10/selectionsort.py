def selectionSort(array,size):
  for i in range(size):
    min_index = i
    for j in range(i+1,size):
      if array[j] < array[min_index]:
        min_index = j
        print(array[min_index])
    (array[i], array[min_index]) = (array[min_index], array[i])
    
arr = [-1,1,5,-2,3,4]
print("Array : ", arr)
size = len(arr)
selectionSort(arr,size)
print("Selection sort Ascending is : ")
print(arr)