"""fruits={0:"apple" ,1:"kiwi" ,2:"pineapple"}
fruits[3]="chickoo"
print(fruits)"""

#create empty dictionary using {}

"""friends={'tom':'cat','jerry':'mouse'}
print(friends)

print(friends['tom'])
print(friends['jerry'])

print(friends.get("tom"))       #passing argunment key value to get method
print(friends.get("jerry"))

print(friends.get("ratan"))     # key is absent returns none
print(friends['ratan'])      #keyerror:'ratan'   """

"""d1={1:"ratan",2:"anu",4:"durga",3:"aaa"}
print(d1.keys())
print(d1.values())

print(list(d1.keys()))
print(list(d1.values()))

print(tuple(d1.keys()))
print(tuple(d1.values()))

print(set(d1.keys()))
print(set(d1.values()))

print(sorted(d1.keys()))
print(sorted(d1.values()))"""


"""d1={1:"ratan",2:"anu",3:"durga"}
for i in d1:
    print(i,d1[i])

print(d1.items())
for k,v in d1.items():
    print(k,v)

del d1[2]
print (d1)

d1.pop(3)
print (d1)"""

# popitem() removes last item of dictionary

"""#creating new dictionary by using list data
l1=[10,20,30,40]
l2=["ratan","anu","durga","aaa"]
x=zip(l1,l2)
d=dict(x)
print(d)  """

#cresting new dictionary by using dict data

"""d1={10:"ratan",20:"anu"}
d2={1:"aaa",2:"bbb"}
l1 = list(d1.keys())
l2 = list(d2.values())
x = zip(l1,l2)
d = dict(x)
print(d)

# creating dictionary with list of keys with same value
keys=["bird","plant","fish"]
d-dict.fromkeys(keys,5)
print(d)   """

#creating dictionary by using items

pairs =[("cat","meow"),("dog","bark"),("bird","chirp")]
lookup =dict(pairs)
print(lookup)
print(lookup.items())
