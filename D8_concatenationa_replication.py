"""s1="Ketan"
s2="anu"
s3=s1+s2        #concatenation
print(s3)

s="Ketan"
ss=s*3          #Replication
print(ss)"""


#python string comparison

"""print("Ketan" >"anu")
print("Ketan"<"anu")
print("Ketan">="Ketan")

print("Ketan"<="Ketan")
print("Ketan"=="Ketan")
print("Ketan"!="anu") """


"""s="Welcome all guys to Python Session"

print(s.find("l"))      #method  s.find(t) returns -1 if not found
print(s.rfind("l"))     #method s.rfind(t)
print(s.index("o"))     #method s.index(t)
print(s.rindex("o"))    #method s.rindex(t)
print(s.strip())        #method s.strip()
print(s.split("l"))     #method s.split(t)
print(s.splitlines())
print(s.lower())
print(s.upper())
print(s.title())            #all first letters of words in string to capital
print(s.capitalize())       #converts first letter of string to capital
print("*".join(s))
print(s.replace("Python","R"))

print(s.startswith("Welcome"))
print(s.startswith("come",3,10))
print(s.endswith("Session"))
print(s.endswith("to",2,16))
print(s.swapcase())

print(s.isalnum())      # True is\\ all are alphanumeric(al[phabets and numbers)
s1="Python310"
print(s1.isalnum())

print(s.isalpha())
s2="HelloPython"
print(s2.isalpha())

print(s.isdigit())
s2="98564738"
print(s2.isdigit())

print(s.islower())
s1="python"
print(s1.islower())

print(s.isupper())
s2="Hello Python"
print(s2.isupper())"""

str4 = 'Ketanit'
#enumerate()
print(tuple(enumerate(str4)))#it contains the index and value of all items in string as pairs
print(list(enumerate(str4)))


