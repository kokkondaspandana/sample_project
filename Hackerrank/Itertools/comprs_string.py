from itertools import groupby

l = [(len(tuple(g)), k) for k,g in groupby(raw_input(), int)]
print ' '.join(map(str, l));


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
