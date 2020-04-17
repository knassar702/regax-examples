import re,sys

data = '''
https://google.com
https://nokia.com
Your Website: https://www.php.net
http://facebook.com/asfasf/as.php
http://lol.net
'''
d = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
m = d.finditer(data)
for i in m:
	print(i.group())
