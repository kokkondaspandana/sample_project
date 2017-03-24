a = set(map(str, raw_input().split(' ')))
is_strict_superset = []
for i in range(int(raw_input())):
     is_strict_superset.append(a.issuperset(set(map(str, raw_input().split(' ')))))
print(all(is_strict_superset))


Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output

False
