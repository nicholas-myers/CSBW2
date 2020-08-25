class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.storage.append(x) 
    
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.storage.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.storage[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.storage) > 0:
            return False
        else:
            return True