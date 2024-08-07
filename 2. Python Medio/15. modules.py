import sys #Sistema operativo
print(sys.path) #Directorio del archivo

import re #Expresiones regulares
text = "2 PLUS 2 IS 4, MINUS 1, THAT'S 3, QUICK MATHS!"
numbers = re.findall("[0-9]+", text)
print(numbers)

import time
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)