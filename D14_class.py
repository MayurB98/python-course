#conversiom process:conversion of local to class level values
'''class MyClass:
    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        #make local to class level values
        self.val1=val1
        self.val2=val2

    def add(self):
        print(self.val1 + self.val2)
 
c=MyClass(10,20)
c.add()  '''

'''class MyClass:
    pass

c=MyClass()
print(c)
#<__main__.MyClass object at 0x0000015609CDD110>
'''

'''class Test:
    def __str__(self):
        return "Welcome to __str__()Constructor"

t=Test()
print(t)
'''
'''class Test:
    def __str__(self):
        return 10

t=Test()
print(t)
'''
#TypeError: __str__ returned non-string (type int)

 #inheritance
'''
class Person:
    name='ABC'
    mobile =9876543210
class address(Person):
    address = 'Pune'

p=address()
print(p.name)
print(p.mobile)
print(p.address)
'''

class Parent:
    def m1(self):
        print("Parent class m1")

class Child(Parent):
    def m2(self):
        print("Child class m2")
p=Parent()
p.m1()

c=Child()
c.m1()
c.m2()
#p.m2() AttributeError: 'Parent' object has no attribute 'm2'











