class Stack():
  def __init__(self):
    self.stack = list()
  def push (self,item):
    self.stack.append(item)
  def pop (self):
    if len(self.stack)> 0 :
      return  self.stack.pop()
    else :
      return None
  def peek(self):
    if len(self.stack)>0 :
      return self.stack[len(self.stack)-1]
    else :
      return None
  def __str__(self):
    return str(self.stack)
  
my_stack = Stack()
# my_stack.push("Buku 1")
# my_stack.push("Buku 2")
# print(my_stack)
# print(my_stack.peek())
# print("List Item ", my_stack)
# print("\nItem Terakhir adalah", my_stack.peek())
# print("\nMengeluarkan ",my_stack.pop())
# print("\nList Item Sekarang" ,my_stack)
jml_angka = int(input("Masukkan Jumlah Element : "))
for i in range(0, jml_angka):
  list = input("Menambahkan Item : ")
  my_stack.push(list)






