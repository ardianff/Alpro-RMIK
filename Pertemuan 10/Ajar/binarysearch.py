###
yourList = [2,4,9,8,1,3,5,6,3] # Example List
yourNumber = int(input('Insert Number to search ? ')) # angka yang ingin dicari

#Fungsi
def searchNumber(Number,List):
    found = False     #Untuk memberikan kondisi adanya angka
    List.sort() # binary search harus diurutkan
    firstIndex = 0  #index pertama
    lastIndex = len(List)-1 #index terakhir
    while firstIndex <= lastIndex and not found:
        middleIndex = (firstIndex + lastIndex) // 2     #mancari index tengah
        if List[middleIndex] == Number:
            found = True
        else:
            if Number < List[middleIndex]:
                lastIndex = middleIndex - 1
            else:
                firstIndex = middleIndex + 1
    return found
    
#Pemanggilam Fungsi ditandai dengan pemanggilan nama fungsi
result = searchNumber(yourNumber,yourList)
if result:
    print('Number %s is Found in List '% yourNumber)
else:
    print('Number %s not Found in List' % yourNumber)