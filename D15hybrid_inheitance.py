'''class School:
    schname="abc" #public member
    __schoolcode="0A23D"  #private member done by by 2 underscore
    def func1(self):
        print("This function is in school")
class Student1(School): # single level inheritsnce
    def func2(self):
        print("This function is in student 1")
class Student2(School): #multi level inheritance
    def func3(self):
        print("This function is in student 2")
class Student3(Student1,School): #hybrid iinheritance
    def func4(self):
        print("This function is in student 3")

#drivers code
object=Student3()
object.func1()
object.func2()
print(object.schname)  #will print as it is public
print(object.schoolcode) #error as trying to access private variable
'''
'''
from math import pi
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self,length):
        super().__init__("Square")
        self.length=length
    def area(self):
        return self.length**2

class Circle(Shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius=radius
    def area(self):
        return pi*self.radius**2

a=Square(4)
b=Circle(7)
print(a)
print(b)
print(a.area())
print(b.area())
'''

#abstaraction

from abc import ABC,abstractmethod  #abstarctmethod is decorator

class AbstractDemo(ABC):
    @abstractmethod
    def display(self):
        none
    @abstractmethod
    def show(self):
        none

class Demo(AbstractDemo):
    def display(self):
        print("Abstract Method")
    def show(self):
        print("Abstract Method Show")
#Obj =AbstractDemo()
Ob = Demo()
Ob.display()
Ob.show()
    

        
    
    
