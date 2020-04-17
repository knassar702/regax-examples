#!/usr/bin/env python3
import re

data = '''
knassar702@gmail.com
asfasfko@lol.com
asfokf@gmail.com
afl260.8@lo.com
<h3> your email is : lol@gmail.com </h3>
<p> email : himan.607@gmail.com </p>
'''
print(re.findall(r'[a-zA-Z0-9.-_+-]*@[a-zA-Z]+\.com',data))
