from data_structures_and_algorithms.stack_and_queue import Stack,Node,Queue,PseudoQueue
import pytest
import unittest




def test_push(stack):


  actual = stack.top.value
  expected = 2
  assert actual == expected
  
def test_pop(stack):
 

  actual= stack.pop()
  expected =2
  assert actual == expected


def test_peek_of_stack(stack):
  

  actual = stack.peek()
  expected = 2
  assert actual == expected


def test_is_empty_stack():
  stack=Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected

def test_next_item(stack):
  actual=stack.top.next.value
  expected = 3
  assert actual == expected
  
def test_enqueue(test_queue):
  actual=test_queue.front.value
  expected=13
  assert actual == expected

def test_dequeue(test_queue2):
  
  actual = test_queue2.dequeue()
  expected=13
  assert actual == expected

def test_peek(test_queue2):
  
  actual = test_queue2.peek()
  expected=13
  assert actual == expected

def test_pseudo_queue():
  pq=PseudoQueue()
  pq.enqueue(13)
  pq.enqueue(27)
  pq.enqueue(23)
  actual=pq.dequeue()
  expected=13
  assert actual == expected

 
@pytest.fixture
def stack():
 
  stack = Stack()
  stack.push(5)
  stack.push(3)
  stack.push(2)

  return stack

@pytest.fixture
def test_queue():
  queue=Queue()
  queue.enqueue(13)
  return queue

@pytest.fixture
def test_queue2():
  queue=Queue()
  queue.enqueue(13)
  queue.enqueue(15)
  queue.enqueue(17)
  queue.enqueue(7)
  return queue



