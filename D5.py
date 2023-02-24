#break examples
"""for i in range(1,10):
    if(i==4):
        break
    print(i)"""

"""for letter in "Ketan":
    if letter =='t'or letter =='a':
        break
    print('Current letter :',letter)"""

#continue examples

"""for i in range(1,10):
    if(i==4):
        continue
    print(i)

for letter in "ketan":
    if letter =='t' or letter =='a':
        continue
    print('Current letter :',letter)"""

# else block for for loop

"""for i in range(1,5):
    print(i)
else:
    print("The for loop is over and else block print")
print("Done")"""

#CASE 1
"""for x in range(10):
    print("Hello World ",x)
    print(10/0)
else:
    print("Else block")
print("Done")"""

#Case 2

"""for x in range(10):
    print("Pratap sir",x)
    if(x==4):
        break
else:
    print("Else block")
print("Done")"""

#Case 3

import os
for x in range(6):
    print("Gagan :",x)
    os._exit(0)
else:
    print("Else block")













