"""my_list = ["mouse",[1,2,3],['a','b'],"anu"]
print(my_list)          #output ['mouse', [1, 2, 3], ['a', 'b'], 'anu']

matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])            #output [4, 5, 6]
print(matrix[1][1])         #output 5
print(matrix[2][0])         #output 7    """

""" # iterating through range using list comprehension

x=[i for i in range(10,20)]
print(x)            #output [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

y=[i*i for i in range(10)]
print(y)            #output [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

z=-[i+1 for i in range(10,20,2)]
print(z)    """


"""# list.append() will add item at the end
l1=[10,20,30]
l2=[40,50,60]
l1.append(40)
print(l1)

animal =['cat','tiger']
animal.append('rat')
print(animal)

#using insert function
animal.insert(2,'lion')
animal.insert(0,'cow')
animal.insert(6,'jaguar')
print(animal)       #outout ['cow', 'cat', 'tiger', 'lion', 'rat', 'jaguar']  

# adding list using + operator creating 3rd list
l3=l1+l2
print(l3)

#replicating values of list in new list
l4=l1*2
print(l4)    """

animal =['rat','tiger']
print(animal)       #output ['rat', 'tiger']

animal[1]='lion'
print(animal)       #output ['rat', 'lion']

animal[1:3]=['cat','rat','dog']
print(animal)

animal[2:4]=['ant']# list  # here  single ant is given and dog is eliminated
print(animal)       #output ['rat', 'cat', 'ant']

animal[1:3]='puppy'  #string
print(animal)       #output ['rat', 'p', 'u', 'p', 'p', 'y']

animal[2]=10        #number
print(animal)
