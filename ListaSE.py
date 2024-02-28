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
        while(ultimo.next):
          last = last.next
          last.next = nuevo_nodo
    def EliminarPrimero(self):
      temp = self.head
      if self.head is None:
        return
      else:
        self.head = temp.next
        temp = None
   def EliminarUltimo(self.head):
     if self.head is None:
       return
     if self.head.next = None:
       self.head = None
       return None
     else:
       second_last = self.had
        while(second_last.next.next):
          second_last = second_last.next 
        second_last.next = None
       return
          
       
        
        
  
