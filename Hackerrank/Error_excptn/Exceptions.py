for i in range(int(raw_input())):
    try:
        a,b=map(int,raw_input().split())
        print a/b
    except Exception as e:
        print "Error Code:",e

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
