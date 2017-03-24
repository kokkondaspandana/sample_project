import re
print '\n'.join([n for n in re.split(r'[,.]',raw_input()) if n])


Sample Input

100,000,000.000
Sample Output

100
000
000
000

