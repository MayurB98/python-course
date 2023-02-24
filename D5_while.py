#while loop e\with else block
"""a=1
while(a<=10):
    print("Hello Sir",a)
    a=a+1
else:
    print("Else block after while")
print("Process done")"""


#case 1 if error no else

"""while True:
    print(10/0)
else:
    print("While loop terminated normally...")
print("Done")"""

#Case2 when break used else not executred

"""a=0
while(a<10):
    a=a+1
    if(a==3):
        break
    print("KIMIT:",a)
else:
    print("Else block")
print("Done")"""

#case 3 when os._exit(0) is used ,else not executed

import os
a=1
while a<10:
    print("KetanIT:")
    os._exit(0)
    a+=1
else:
    print("Else block")












