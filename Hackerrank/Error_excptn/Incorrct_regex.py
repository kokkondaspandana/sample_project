import re
for i in range(int(raw_input())):
    try:
        reg=re.compile(raw_input())
    except re.error:
        print False
    else:
        print True


Sample Input

2
.*\+
.*+
Sample Output

True
False
