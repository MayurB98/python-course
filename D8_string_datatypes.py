#string datatypes in python
"""name1="Ketan"
name2="anu"
name3='Ketan'
print(id(name1))
print(id(name2))
print(id(name3))
print(name1==name2)
print(name1==name3)
print(name1!=name3)
print(name1!=name3)
#to check memory address use is and is not operator
print(name1 is name2)
print(name1 is name3)
print(name1 is not name2)
print(name1 is not name3) """

#count() : to find data occurences in and not in are operators,count is function

"""s1="ketan"
print("ketan" in s1)
print("durga" in s1)
print("ketan" not in s1)
print("durga " not in s1)

s2="KetanKetan"
print(s2.count('a'))
print(s2.count('Ketan'))
print(s2.count('a',2,7))  # from 2 to 6th position
print(s2.count('Ketan',2,7))  """

#String formatting with {} operators
eid,ename,esal=111,'Ketan',10000.45
print(" Emp id=%d Emp name=%s Emp sal=%g"%(eid,ename,esal))
print("Emp eid={} Emp name={} Emp sal={}".format(eid,ename,esal))
print("Emp id ={0} Emp name ={1} Emp sal={2}".format(eid,ename,esal))
