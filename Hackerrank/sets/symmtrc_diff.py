a,b = [set(raw_input().split()) for x in range(4)][1::2]
print '\n'.join(sorted(a^b, key=int))


i/p:
4
2 4 5 9
4
2 4 11 12

o/p:
5
9
11
12

