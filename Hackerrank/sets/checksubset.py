for i in range(int(raw_input())):  
    a = int(raw_input())
    A = set(raw_input().split())
    b = int(raw_input())
    B = set(raw_input().split())
    print "True" if len(A) == len(B.intersection(A)) else "False"


Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False
