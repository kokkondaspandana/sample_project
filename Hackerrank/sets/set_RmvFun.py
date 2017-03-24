n = input()
s = set(map(int, raw_input().split())) 
for i in range(int(input())):
    x = list(raw_input().split())
    eval('s.{0}({1})'.format(*x+['']))
print sum(s)


i/p:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

o/p:
4

