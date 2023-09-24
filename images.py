import requests
import re

content = requests.get('https://manuelsanciens.blogspot.com/2019/11/brachet-dumarque-elements-de-geometrie.html').content
regex = r'src="(https://.*\d{4}\.jpg)'
matches = re.findall(regex, content.decode('utf-8'))

i = 0
for match in matches:
    print (match)
    with open(format(i, '#04d') + '.jpg', 'wb') as f:
        f.write(requests.get(match).content)
    i = i+ 1
    