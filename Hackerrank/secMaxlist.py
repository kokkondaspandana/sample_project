if __name__ == '__main__':
    n = int(raw_input())
    
lis = list(map(int,raw_input().strip().split()))[:n]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)


i/p:
5
2 3 6 6 5

o/p:
5
