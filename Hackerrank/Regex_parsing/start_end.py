import re
s, k = raw_input(), raw_input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')


Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)

