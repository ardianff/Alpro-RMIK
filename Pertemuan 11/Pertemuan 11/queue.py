from collections import deque
class Queue :
  def __init__(self):
    self.items = deque()
  def enqueue(self,item):
    self.items.append(item)
  def dequeue(self):
    return self.items.popleft()
  def peek(self):
    return self.items[0]
  def __str__(self):
    return str(self.items)
  
list = Queue()
print("Kondisi List awal ",list)
list.enqueue("Ayam Goreng")
list.enqueue("Bebek Goreng")
print("\nKondisi List sekarang ",list)
list.enqueue("Lele Goreng")
print("\nKondisi List sekarang ",list)
print("Item terdepan adalah ",list.peek()) 

list.dequeue()
print("\n",list)
print("\nItem terdepan adalah ",list.peek()) 
list.enqueue("Burung Dara")
print("\n",list)



# ['Ayam Goreng','Bebek Goreng']

# Ayam Goreng
# Bebek Goreng