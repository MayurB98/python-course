'''import re
result=re.findall(r'.','AV is largest Analytics community of india')
print(result)
'''
'''import re
result=re.findall(r'\w','AV is largest Analytics community of india')
print(result)
'''
'''import re
result=re.findall(r'\w*','AV is largest Analytics community of india')
print(result)  # words and spaces
'''
'''import re
result=re.findall(r'\w+','AV is largest Analytics community of india')
print(result) # words and not spaces
'''
'''import re
result=re.findall(r'^\w+','AV is largest Analytics community of india')
print(result) # returns only first word in a string
'''
'''import re
result=re.findall(r'\w+$','AV is largest Analytics community of india')
print(result)  #returns last word from string
'''
'''import re
result=re.findall(r'\w\w','AV is largest Analytics community of india')
print(result) #without spaces extract letters in pairs of two
'''
'''import re
result=re.findall(r'\b\w.','AV is largest Analytics community of india')
print(result) #extract two characters avaiable at start of word boundary
'''
'''import re
result=re.findall(r'\b.','AV is largest Analytics community of india')
print(result) # extracts first character with spaces.
'''
'''import re
result=re.findall(r'@\w+.\w+','abc.test@gmail.com,xyz@test.in,test.first@analyticsvidhya.com')
print(result)  #extract all characters after @
#@\w+.+ -> can give domain with 2 dots eg.@yahoo.co.in
'''
'''import re
result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com,xyz@test.in,test.first@analyticsvidhya.com')
print(result) #extract only domain name using()
'''

'''import re
result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007,XYZ 56-4532 11-11-2011,ABC 67-8945 12-01-2009')
print(result) #return date from given string
'''
'''import re
result=re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007,XYZ 56-4532 11-11-2011,ABC 67-8945 12-01-2009')
print(result)  #to extract only year use parenthesis "( )"
'''
'''import re
result=re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of india')
print(result) #returns string that start with alphabets
'''
'''import re
result=re.findall(r'\b[^aeiouAEIOU]\w+','AV is largest Analytics community of india')
print(result)
'''
import re
line ='asdf fjdk;afed,asdf,foo'
#string has multiple delimiters{";"","" "}
result=re.split(r'[;,\s]',line)
print(result)





