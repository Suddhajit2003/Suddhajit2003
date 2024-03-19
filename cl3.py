#Dynamic Array
import ctypes
class Mylist:
    def __init__(self):
        self.n=0
        self.size=1
        self.A=self._make_array(self.size)
    def _make_array(self,capacity):
        return(capacity * ctypes.py_object)()
    def append(self,item):
        if self.n==self.size:
            self._resize(2*self.size)
            self.n+=1
        else:
            self.A[self.n]=item
            self.n +=1
    def _resize(self,new_capacity):
        #1.Create new array
        B=self._make_array(new_capacity)
        self.size=new_capacity
        
        #2.Copy the content
        for i in range(self.n):
            B[i]=self.A[i]
        #3.Reassign
            self.A=B
    def __len__(self):
        #len(obj)
        return self.n
        
    
