import itertools

n = int(input())
k = raw_input().split()
l = int(input())
count = 0

itcomb = list(itertools.combinations(k, l))
lilen = float(len(itcomb))

for i in itcomb:
    if 'a' in i:
        count += 1
        
print (float(count)/lilen)

Sample Input

4 
a a c d
2
Sample Output

0.8333

