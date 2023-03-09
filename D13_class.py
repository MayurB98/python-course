"""class MyClass():
    a,b=10,20
    def add(self):
        print(self.a+self.b)
    def largerval(self):
        print(self.a if self.a>self.b else self.b)


c=MyClass()
c.add()
print(c.a+c.b)
c.largerval()  """


#conversion of local variables to class level variables

"""class MyClass():
    def values(self,val1,val2):
        print(val1)
        print(val2)
        #conversion of local to class values
        self.val1=val1
        self.val2=val2
    def add(self):
        print(self.val1+self.val2)
c=MyClass()
c.values(3,3)
c.add()  """

#local variables vs. class variables vs,global variables

"""a,b=100,200
class MyClass():
    a,b=10,20
    def add(self,a,b):
        print(a+b)  #will add 10 and 20
        print(globals()['a'] + globals()['b'])  #will add 100 and 200
        print(self.a + self.b)
    def disp(self):
        print("Good Morning")
        
c = MyClass()
c.disp()
c.add(3,3) #local
#name less object approach
MyClass().disp()
#second object creation
c2=MyClass()
c2.disp()"""

"""class MyClass():
    name = "ketan"
#first object creation
c1 = MyClass()
c1.name="durga"
print(c1.name)      #durga

#second object creation
c2 =MyClass()
print(c2.name)       """   #ketan

# to check memory location of objects

class MyClass():
    pass
c1 = MyClass()
c2 = MyClass()
c3 = c1

print(id(c1))
print(id(c2))
print(id(c3))

# is and is not checks memory address
print(c1 is c2)
print(c1 is c3)
print(c1 is not c2)
print(c1 is not c3)

