list = [2,4,9,8,1,3,5,6,3]
key = 2

def binarySearch(key,list):
  found = False
  list.sort()
  firstIndex = 0
  lastIndex = len(list)-1
  while firstIndex <= lastIndex and not found :
    middleIndex = (firstIndex + lastIndex)//2
    if list[middleIndex] == key:
      found = True
    else:
      if key < list[middleIndex]:
        lastIndex = middleIndex -1
      else : 
        firstIndex = middleIndex +1
  return found

result = binarySearch(key,list)
print('Angka %s %s'%(key,result))