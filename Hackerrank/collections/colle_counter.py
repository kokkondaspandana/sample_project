import collections

numShoes = int(raw_input())
shoes = collections.Counter(map(int, raw_input().split()))
numCust = int(raw_input())

income = 0

for i in range(numCust):
    size, price = map(int, raw_input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print income           


Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
