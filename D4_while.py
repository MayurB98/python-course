"""a=int(input("Enter number"))
sum=0
while(a>0):
        sum+=a
        a=int(input("Enter number"))
print("Sum is ",sum)"""

"""a=int(input("Enter first number"))
b=int(input("Enter Second number"))

while(a!=b):
        if(a>b):
                a-=b
        else:
                b-=a
print("GCD =",a)"""

# pgm to print the number of digits of a given number using while loop
"""num = int(input("Enter a number"))
digits =0
while num!=0:
        num=num//10         #floor division
        print("num = ",num) # not necessary
        digits +=1
print("Number of digits",digits) """

#program to verify if a given number is  prime or not prime

n=int(input("Enter a number"))
flag = True
for div in range(2,n):
        if n%div==0:
                flag = False
print("Prime"if flag==True else "Not Prime")
