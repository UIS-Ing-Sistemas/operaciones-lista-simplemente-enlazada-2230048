class Nodo:
  def __init__(self,valor)
  self.data = valor
  self.next = None


class ListaSE:
  def __init__(self):
    self.head = None
    def AgregarInicio(self,valor):
      nuevo_nodo = Nodo(valor)
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
     if self.head.next = None:
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
      i=0
      temp = self.head
        while(temp != None):
          i == i++
          return i
    def ListaVacia(self):
      if self.head is None:
        return True
      else return False

  
ListaSE = ListaSE()
ListaSE.AgregarInicio(1)
ListaSE.AgregarInicio(5)
ListaSE.AgregarInicio(9)
ListaSE.AgregarInicio(20)
