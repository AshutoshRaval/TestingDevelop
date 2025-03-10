#Shardul Chavan

############################################################
# Write code in file solution.py 
# Post� solution.py in Canvas along with 4 screen shots that shows Leetcode has passed. We will not use screen shot to give 100
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run solution.py file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def __len__(self) -> 'int':
        return self._len

    def _get_first_element(self)->'T':
        if(self._first):
            return self._first.val
        else: return -1

    def _find(self, x:'int') -> 'list of [current_node, previous_node]':
        nodes = [self._first, None] 
        while(nodes[0] != None):
            if (nodes[0].val == x):
                return nodes
            nodes[1] = nodes[0]
            nodes[0] = nodes[0].next
        return nodes
    
    def delete_specific_value(self,x:'int')->'bool':
        nodes = self._find(x)
        a = self._delete(nodes)
        return a
        
    def _delete_from_front(self,x:'int')->'bool':
        if (self._first):
            return self.delete_specific_value(self._first.val)
        else: 
            return False

    
    def append(self, new_num:'int'):
        self._len = self._len+1 
        self._add_element(new_num,True)

    def _add_element(self,new_num:'int',append:'bool'=True):
        n = ListNode(new_num)
        if self._first == None and self._last == None:
            self._first = n
            self._last = n
        else:
            if append:
                self._last.next = n
                self._last = n
            else:
                n.next = self._first
                self._first = n

    def _delete(self,nodes:'list of size 2') -> 'bool':
        if (nodes[0]):
            current_node = nodes[0]
            previous_node = nodes[1]
            if ((current_node == self._first) and (current_node == self._last) and (previous_node == None)):
                
                #if list has only one element
                assert(self._first == self._last)
                self._first = None
                self._last = None
                                
            elif (current_node == self._first): #removing first element 
                assert(self._first.next != None)
                self._first = current_node.next
                              
            elif (current_node == self._last): #removing last element 
                assert(self._first)
                previous_node.next = None
                self._last = previous_node
                
            else:
                assert(self._first)
                assert(self._last)
                previous_node.next = current_node.next
            
            self._len = self._len - 1
            return True
        else:
            return False

    def _get_last_element(self)->'T':
        if self._first:
            assert (self._last)
            return self._last.val
        else: return -1
            
    def _delete_last_element(self) -> 'bool':
        if (self._first):
            nodes = [self._first, None]
            
            while(nodes[0].next):
                nodes[1] = nodes[0]
                nodes[0] = nodes[0].next
                
            assert(nodes[0])
            assert(nodes[0].next == None)
            
            if (nodes[1]):
                assert(nodes[1].next == nodes[0])
                
            a = self._delete(nodes)
            return a
        else:
            return False

    def prepend(self, new_num:'int'):
        self._len = self._len + 1   
        self._add_element(new_num, False) 

  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()
        
    def push(self,x:'int'):
        self._s.append(x)
        
    def pop(self)->'int':
        top_element = self._s._get_last_element()
        if top_element != -1:
            self._s._delete_last_element()
        return top_element

    def top(self)->int:
        return self._s._get_last_element()
        
    def empty(self) -> bool:
        return len(self._s) == 0    
        

############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self,x:int)->None:
        self._s.append(x)

    def pop(self) -> int:
        x = self._s._get_first_element()
        self._s._delete_from_front(x)
        return x
        
    def peek(self)->int:
        return self._s._get_first_element()

    def empty(self) -> bool:
        return len(self._s) == 0    



############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    def enQueue(self, value: int) -> bool:
        if len(self._s) < self._K:
            self._s.append(value)
            return True
        return False
    
    def deQueue(self) -> bool:
        if not len(self._s) == 0:
            x = self.Front()
            self._s._delete_from_front(x)
            return True
        else: return False
        

    def Front(self) -> int:
        return self._s._get_first_element()        

    def Rear(self) -> int:
        return self._s._get_last_element()
        

    def isEmpty(self) -> bool:
        return len(self._s) == 0
        
    def isFull(self) -> bool: 
        return len(self._s) == self._K
 

############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    def insertFront(self, value: int) -> bool:
        if len(self._s) < self._K:
            self._s.prepend(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self._s) < self._K:
            self._s.append(value)
            return True
        return False
              

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            x = self.getFront()
            self._s._delete_from_front(x)
            return True
        return False

    def deleteLast(self) -> bool:     
        if not self.isEmpty():
            self._s._delete_last_element()
            return True
        return False
        

    def getFront(self) -> int:
        return self._s._get_first_element()

    def getRear(self) -> int:
         return self._s._get_last_element()
        

    def isEmpty(self) -> bool:
        return len(self._s)==0
        

    def isFull(self) -> bool:
        return len(self._s) == self._K
 
