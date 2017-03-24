english = int(raw_input())
eng_id = set([int(x) for x in raw_input().split()])
french = int(raw_input())
fre_id = set([int(x) for x in raw_input().split()])

print(len(eng_id.intersection(fre_id)))


i/p:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

o/p:
5
