# inner function

"""def outer():
    print("Outer function")
    def inner():
        print("inner function")
    inner()                 #CALLING INNER FUNCTION
    print("I'M still in outer function")
print("Executing inner methods")
outer()
print("I'm back in main line") """


#inner function can access outer function variables

"""def outer():
    print("Outer function")
    name1="Amit"
    def inner():
        print("Inner function")
        name2="Anu"
        print(name1)
        print(name2)
        print("I printed from inner function")
    inner()
    print(name1)
outer()
print("In main line")"""

# outer fn is able to access inner fn variables with nonlocal keyword
"""def outer():
    name1="Amit"
    def inner():
        nonlocal name1
        name1="durga"
        print("I am in inner function",name1)
    inner()
    print("Outer function",name1)
outer() """

def outer():
    name1="Amit"
    def inner():
        global name2
        name2="durga"
        print("I am in inner function",name1)
    inner()
    print("Outer function",name1)
    print("Inner function variable",name2)
outer()             # outer function calling











