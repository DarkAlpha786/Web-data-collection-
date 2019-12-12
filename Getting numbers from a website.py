import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum1 = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
	x= tag.contents[0]
	#find the numbers in contents
	num = re.findall('[0-9]+' , x )
	#breaking the list
	for lst1 in num:
		#converting the string to a integer
		lst1 = int(lst1)
		sum1 = sum1 + lst1
print sum1
