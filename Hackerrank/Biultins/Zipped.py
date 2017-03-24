from __future__ import division 
m, n = map(int, raw_input().split())
res = []
for x in xrange(n):
    res.append(map(float, raw_input().split()))
for i in map(lambda x: x/n, map(sum, zip(*res))):
    print i


Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
Sample Output

90.0 
91.0 
82.0 
90.0 
85.5  
