def bubbleSort(arr):
    list= int(input("Masukkan Jumlah Element Array : "))
    for k in range(0,list):
        input_list = int(input("Masukkan list angka Ke-%s : "%k))
        arr.append(input_list)
    # arr =[4,2,12,1,3,5,]
    print("\nList Array : ",arr)
    n = len(arr) 
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("List Array ke-",i," ", arr)
        if not swapped:
            return 
    print("Hasil Sorting :")
    for i in range(len(arr)):
        print("% d" % arr[i], end=" ")
arr = []
bubbleSort(arr)
