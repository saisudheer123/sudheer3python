import re
p=input()
b=re.sub('[\w]+','', p)
print(len(b))
