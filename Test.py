

class myClass:
    def __init__(self, myVar):
        self.myVar = myVar

class mySubclass(myClass):
    def __init__(self, myVar2, myVar):
        self.myVar2 = myVar2

c = myClass(5)

s = mySubclass(myVar2=2)


print(isinstance(s, mySubclass))
print(s.myVar)
print(s.myVar2)