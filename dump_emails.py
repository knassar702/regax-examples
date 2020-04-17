import re,sys

data = '''
I Love You lol
Khaled : 109-140-351
Mohamed : 150-999-123
lol : 150.999.123
ff : 150*999-123
sdg nokia.com
gat
bat
dat
Mr. Khaled
Mr. Zigoo0
Ms. Nada Mohamed
Mrs. LOl
knassar702@gmail.com
asfasfko@lol.com
asfokf@gmail.com
afl260.8@lo.com
<h3> your email is : lol@gmail.com
'''
print(re.findall(r'[a-zA-Z0-9.-_+-]*@[a-zA-Z]+\.com',data))
