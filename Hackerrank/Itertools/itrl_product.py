from itertools import product
A = map(int,raw_input().split())
B = map(int,raw_input().split())
A.sort()
B.sort()

ans = [A,B]
AxB = list(product(*ans))

for i in AxB:
	print i,

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
