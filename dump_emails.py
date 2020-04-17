#!/usr/bin/env python3
import re

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
Mrs. LOl
knassar702@gmail.com
asfasfko@lol.com
asfokf@gmail.com
afl260.8@lo.com
<h3> your email is : lol@gmail.com
https://google.com
lol@ff.net
http://nokia.com
'''
d = re.compile(r'[a-zA-Z0-9.-_+-]*@[a-zA-Z]+\.(com|net|edu|eg)')
m = d.finditer(data)
for i in m:
        print(i.group())
