from itertools import combinations
s,n=raw_input().split()
for i in range(1,int(n)+1):
    for j in combinations(sorted(s),i):
         print''.join(j)

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
