class c2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __iadd__(self, ob):
        self.x +=ob.x
        self.y +=ob.y
        return c2(self.x, self.y)
    def __isub__(self, ob):
        self.x -=ob.x
        self.y -=ob.y
        return c2(self.x,self.y)
    def __str__(self):
        return "(%d,%d)"%(self.x,self.y)
ob1=c2(20,10)
ob2=c2(10,10)
ob1 += ob2
print(ob1)
ob1=c2(20,10)
ob2=c2(10,10)
ob2 -= ob1
print(ob2)