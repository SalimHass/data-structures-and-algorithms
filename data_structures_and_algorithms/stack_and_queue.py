class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 

class Stack :
  def __init__(self,node=None):
    self.top = node 

  def push(self,value):
    node = Node(value)
    node.next = self.top
    self.top = node 

  def pop(self) :
    if self.top is None:
        raise ValueError
    temp = self.top
    self.top = self.top.next
    temp.next= None
    return temp.value

  def peek(self):
    if self.top is None:
        raise ValueError
    return self.top.value
   
  def is_empty(self):
    """method to check if stack is impty
     return boolean
    """
    return self.top == None 

class Queue :
  def __init__(self):
    self.front=None
    self.rear=None

  def enqueue(self,value):
    node = Node(value)

    if not self.front :
      self.rear = node 
      self.front = node 
      
    else:  
      self.rear.next = node 
      self.rear = node 
      
  def dequeue(self) :
    if self.rear is None:
        raise ValueError
    temp_node = self.front
    self.front=self.front.next
    temp_node.next=None
    return temp_node.value

  def peek(self):
    if self.front is None:
        raise ValueError
    return self.front.value

  def is_empty(self):
    if self.front in None:
        return True
    else: 
        return False


class PseudoQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, value):
        self.stack_in.push(value)
        return self.stack_in

    def dequeue(self):
        if self.stack_out.is_empty() is False:
            return self.stack_out.pop()
        if self.stack_in.is_empty():
            raise ValueError
        else:
            while self.stack_in.is_empty() is False:
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    




if __name__=="__main__":
  queue=Queue()
  queue.enqueue(13)
  queue.enqueue(15)
  queue.enqueue(17)
  queue.enqueue(7)
  queue.dequeue()
  queue.peek()

  sq=PseudoQueue()
  sq.enqueue(11)
  sq.enqueue(13)
  sq.enqueue(17)
  print(sq.dequeue())
  print(sq.dequeue())

  print(sq.dequeue())

