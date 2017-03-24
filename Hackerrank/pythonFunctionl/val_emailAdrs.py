import re
def fun(s):
    # return True if s is a valid email, else return False       
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)


Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
