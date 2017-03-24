s=raw_input()
k=int(raw_input())
n=len(s)

for x in xrange(0, n, k):
    slicedStr = s[x : x+k]
    uni =[]
    for y in slicedStr:
        if y not in uni:
            uni.append(y)
    print ''.join(uni)

i/p:

AABCAAADA
3   

o/p:
AB
CA
AD
