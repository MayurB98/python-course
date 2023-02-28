"""def happyBirthday(person):
    print("Happy Birthday dear",person)

def main():
    happyBirthday('amit')
    happyBirthday('Anu')
print("Welcome to Birthady messages")
main()
print("End of code") """

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def product(a,b):
    return a*b

def divide (a,b):
    if(b==0 or a==0):
        print("\nDivision not possible")
        return 0
    else :
        return a/b

n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))

add=sum(n1,n2)
print("\n The Addition is",add)

diff=sub(n1,n2)
print("\n the difference is",diff)

mul=product(n1,n2)
print("\n The Multiplication is",mul)

div=divide(n1,n2)
if div==0:
    print("Invalid values for division")
else:
    print("\n The division is",div)
print("\n End of code")















