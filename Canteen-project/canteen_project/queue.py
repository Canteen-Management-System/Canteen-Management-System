class Node :
    def __init__(self,value):
        self.value = value 
        self.next = None


class Queue:
    '''
    a Queue class that has a front property. It creates an empty Queue when instantiated.
    This object should be aware of a default empty value assigned to front when the queue is created.
    '''

    def __init__(self):
        self.front  = None
        self.rear = None

    def enqueue(self, value):
        '''
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        '''
        node = Node(value)

        if not self.front:
            self.rear = node
            self.front = node

        else:
            self.rear.next = node 
            self.rear = node 
    
    def dequeue(self):
        '''
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        '''
        if (self.front == None):
            raise Exception("Queue is empty")
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value


    def isImpty(self):
        '''
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        '''
        return self.front == None


    def peek(self):
        '''
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        '''
        if (self.front == None):
            raise Exception("Queue is empty")
        else:
            return self.front.value