# default arguments

"""def empdetails(eid=1,ename="Anu",esal=10000):
    print("Emp id =",eid)
    print("Emp name =",ename)
    print("Empsal=",esal)
    print("*******")

empdetails()
empdetails(222)
empdetails(333,"Durga")
empdetails(111,"Gagan",10.5)  """


#keyword arguments/named arguments

"""def empdetails(name,role):
    print(name,role)
empdetails(name="Amit", role="Manager")    #function calling
empdetails(role="developer",name="anu")     #function calling  """


"""def varlengthArgs(*varargs):
    for i in varargs:
        print(i)
    print("\n I am in varlengthArgs function")

print("i am in main line")
varlengthArgs(10,20,30,40)
print("------")
varlengthArgs(10,20.4)
print("---------")"""

#none -IN PYthon means nothing

def add():
    a=10
    b=20
    c=a+b
x=add()
print(x)        #it is not returning anything 

def add(a):
    if(a%2)==0:
        return True
x=add(3)
print(x)        #output _none


