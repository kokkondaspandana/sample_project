from itertools import permutations
inputs = raw_input().split()
print "\n".join( "".join(i) for i in permutations(sorted(inputs[0]),int(inputs[1])) )

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
