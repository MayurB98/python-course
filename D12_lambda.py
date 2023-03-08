"""def m1(x,y):
    print(x*y)
m1(10,20)

a = lambda x,y:x*y
print(a(10,20))

b=lambda x,y:x if x>y else y
print(b(3,4))"""   #lambda function

"""print(list(filter(lambda x:x%2==0,range(10))))
n='Yogesh'
print(list(filter(lambda x:x=='e',n)))

print(list(map(lambda x:x*2,range(10))))"""

"""import math
print("The value of pi is ",math.pi) """

"""import math as m
print("The value of pi is ",m.pi)"""

"""import calculator
calculator.addition(10,20)
calculator.subtraction(10,20) """

"""import datetime
print(datetime.datetime.now())

print(datetime.date.today())  #for current date  """
#decorators
"""def makeDecorator(func):
    def inner():
        print("I am Decorator!!")
        func()
    return inner

#the function which is to be decorated(wrapped) use @wrapper/decorator
#function name ABOVE its DEFINATION
@makeDecorator
def generalFunc():      #function to be decorated
    print("I am General Function..!!")
generalFunc()"""

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
@uppercase
def greet():
    return 'Hello Guys'
print(greet())



 
