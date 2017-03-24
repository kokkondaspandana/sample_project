N,n = int(raw_input()),raw_input().split()
print all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])


Sample Input

5
12 9 61 5 14 
Sample Output

True
