m = int(raw_input())
A = set(map(int, raw_input().split(" ")))
n = int(raw_input())

for i in range(n):
    cmd, args = raw_input().split(" ")
    B = set(map(int, raw_input().split(" ")))
    eval('A.'+cmd+'(B)')

print sum(A)


i/p:
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

Sample Output

38
