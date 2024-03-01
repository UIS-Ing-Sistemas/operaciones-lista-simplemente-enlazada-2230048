class Nodo:
  def __init__(self,data):
      self.data = data
      self.next = None


class ListaSE:
  def __init__(self):
    self.head = None
  def AgregarInicio(self,new_data):
      nuevo_nodo = Nodo(new_data)
      if self.head is None:
         self.head = nuevo_nodo
         return
      else:
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo
  def InsertarFinal(self,valor):
      nuevo_nodo = Nodo(valor)
      if self.head is None:
         self.head = nuevo_nodo
         return
      else:
        last = self.head
        while(last.next):
          last = last.next
      last.next = nuevo_nodo
  def EliminarPrimero(self):
      temp = self.head
      if self.head is None:
        return
      else:
        self.head = temp.next
        temp = None
  def EliminarUltimo(self):
     if self.head is None:
       return
     if self.head.next == None:
       self.head = None
       return 
     else:
       second_last = self.head
       while(second_last.next.next):
          second_last = second_last.next 
       second_last.next = None
       return
  def BuscarElemento(self, value):
      temp = self.head
      while(temp != None):
          if temp.data == value:
            return True
          temp = temp.next
      return False
  def ContarElementos(self):
      cuenta=0
      temp = self.head
      while(temp != None):
          cuenta += 1
          temp = temp.next
      return cuenta
  def ListaVacia(self):
      if self.head is None:
        return True
      else:
          return False
  def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

  
ListaSE1 = ListaSE()
ListaSE1.AgregarInicio(1)
ListaSE1.AgregarInicio(5)
ListaSE1.AgregarInicio(9)
ListaSE1.AgregarInicio(20)
ListaSE1.printList()
print("\n")
ListaSE1.InsertarFinal(15)
ListaSE1.InsertarFinal(45)
ListaSE1.printList()
print("\n")
ListaSE1.EliminarPrimero()
ListaSE1.printList()
print("\n")
ListaSE1.EliminarUltimo()
ListaSE1.printList()
print("\n")
if ListaSE1.BuscarElemento(70):
    print("Verdadero")
else:
    print("Falso")
print("\n")
print(ListaSE1.ContarElementos())
if ListaSE1.ListaVacia():
    print("Yes")
else: 
    print("No")
