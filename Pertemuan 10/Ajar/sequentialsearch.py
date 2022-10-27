list = [11,23,58,31,56,77,43,12,65,19]

def sequential (data,value):
  start = 0
  temp = False
  while start < len(data) and not temp:
    # membandingkan value dengan nilai dalam array
    if data[start] == value :
      temp = True
      print("Nilai ",value," ada di indeks ke- ",start)
    else:
      start +=1
  return temp

sequential(list,11)