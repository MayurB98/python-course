"""x,y=10,20 #global variables

def add(a,b):   #local variables
    print(a+b)
    print(x+y)
def mul(a,b):       #local variables
    print(a*b)
    print(x*y)

add(4,4)            #function calling
mul(5,5)         """   #function calling

a,b=10,20       #GLOBAL VARIABLE
def add(a,b):       #local variables
    print(a+b)
    print(globals()['a']+globals()['b'])
add(4,4)            #function calling
