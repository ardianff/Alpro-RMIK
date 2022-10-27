from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
      if(len(self.items) == 0):
        return "Kosong", self.items
      else :
        return "Ada isinya", self.items
        
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return str(self.items)
      
q = Queue()
print("List Awal ",q)
print("Kondisi List ",q.is_empty())
# q.enqueue("Buku")
# q.enqueue("Majalah")
# q.enqueue("Koran")

jml_angka = int(input("\nMasukkan Jumlah Element : "))
for i in range(0, jml_angka):
  list = input("Menambahkan Item : ")
  q.enqueue(list)
  
print("\nList Sekarang ", q)
print("Kondisi List ",q.is_empty())
# q.enqueue("4")
# q.enqueue("5")
# q.enqueue("6")
# q.dequeue()
# print(q)
print("\nJumlah item dari List : ", q.size())
print("Item terdepan di List:", q.peek())
print("\nMengambil ",q.dequeue())
print("Mengambil ",q.dequeue())
print("\nList Sekarang ", q)
# print(q)