import re
for i in range(input()):
	print bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', raw_input()))


Sample Input

4  
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output

False
True
True
False
