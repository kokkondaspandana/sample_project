N,M=map(int,raw_input().split())
rows = [raw_input() for i in range(N)]
K = int(raw_input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

