from itertools import combinations_with_replacement
s,n=raw_input().split()
print "\n".join("".join(i) for i in list(combinations_with_replacement(sorted(s),int(n))))

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
