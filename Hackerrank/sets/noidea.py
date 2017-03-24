n,m=(raw_input().split())
s_arr=(raw_input().split())
A=set(raw_input().split())
B=set(raw_input().split())
print sum((i in A)-(i in B) for i in s_arr)

i/p:
3 2
1 5 3
3 1
5 7

o/p
1
