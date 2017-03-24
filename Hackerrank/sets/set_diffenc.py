a= int(raw_input())
list1 =  raw_input().split()
b= int(raw_input())
list2 = raw_input().split()
n = set(list1).difference(list2)
count = 0
print len(n)

i/p:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

o/p:

4
