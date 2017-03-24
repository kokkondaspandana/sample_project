from calendar import weekday,day_name
MM,DD,YYYY=[int(i) for i in raw_input().split()]
print day_name[weekday(YYYY,MM,DD)].upper()


Sample Input

08 05 2015
Sample Output

WEDNESDAY
