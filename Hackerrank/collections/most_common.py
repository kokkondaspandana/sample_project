from collections import Counter
string = sorted(Counter(raw_input()).items(), key= lambda x: (-x[1],x[0]))[:3]
print("\n".join(x[0]+" "+str(x[1]) for x in string))

Sample Input

aabbbccde
Sample Output

b 3
a 2
c 2
