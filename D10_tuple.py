"""t1=(10,20,30,40,50)         #tuple
print(t1[0])
print(t1[2:4])
print(t1[1:4:2])
print(t1[:4])
print(t1[2:])
print(t1[:])
print(t1[::2])
print(t1[2:10])
#print(t1[10])      IndexError: tuple index out of range
print(t1[-3])
print(t1[-4:-2])
print(t1[:-3])
print(t1[-3:])      #output (30, 40, 50)
#print(t1[-9])      IndexError: tuple index out of range """

#if you want to extract all the elements without specifying indexes,make sure
#LHS side of all vraiables match size of tuple

#if less number of variables are there in LHS side ,then specify indexing to
#the tuple to RHS side

"""t1=(10,20,30)
a,b=t1[1],t1[2]
print(a,b) """

#NESTED TUPLE

"""t=((10,20),(30,40,50))

print(t[0])
print(t[1])
print(t[1][1])
print(t[0][1])
print(t[1][2])

#unpacking nested tuple

a,b=t
print(type(a))
print(type(b)) """

"""#adding multiple elements in tuple

t1 = tuple(x for x in range(10))
print(t1)

t2 = tuple(x+267 for x in range(10,26))
print(t2)

t3=tuple(x*89 for x in range(10,99,4))
print(t3)  """

# concatenation and replication

"""t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
print(t1)
print(id(t1))

t4=t1*3
print(t4)"""

t1=(10,20,30)
print(id(t1))
t2=(40,50,60)
t1=t1+t2
print(t1)
print(id(t1))

# here old object without reference so object is destroyed


