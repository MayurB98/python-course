"""#creating empty list
list1=[]
print(list1)

list2=list()        #constructor for allocating memory
print(list2)

list3 = list("Ketan")
print(list3)     """

"""l1=[10,20,30,40,50]

print(l1[2])
print(l1[2:4])
print(l1[1:4:2])
print(l1[2:])
print(l1[:2])
print(l1[:])
print(l1[::2])
#print(l1[8])   IndexError: list index out of range

print(l1[-3])
print(l1[-3])
print(l1[-3:-1])
print(l1[-3:])
print(l1[:-3])
print(l1[:])
print(l1[::-2])
#print(l1[-9])  IndexError: list index out of range """

"""l=["ketan","anu","durga","sunny"]
for x in l:
    print(x)
print("------")


for x in l[1:3]:
    print(x)
print("--------")

for x in l[1:]:
    print(x)
print("------")

for x,y in enumerate(l):   # 2 iterators for index and value
    print(x,y)  """

"""#new
l1=[10,20,30]
l2=[40,50,60]
l3=l1
l4=[10,20,30]

print(l1==l2)       # checks values 
print(l1==l4)
print(l1!=l2)
print(l1!=l4)
print("-----")

print(l1 is l2)         #checks memory address in python if same values then point to same address
print(l1 is l3)
print(l1 is not l2)
print(l1 is not l3)
print("------")

#in and not in is used to check data is available
print(10 in l1)
print (100 in l2)
print(10 not in l1)
print(100 not in l2)  """

# unpacking the list data

l1=[10,"ketan",10.5]
a,b,c=l1
print(a,b,c)
print(type(a),type(b),type(c))

l2=[10,"ketan",10.5,30]
a,b,c=l2 

