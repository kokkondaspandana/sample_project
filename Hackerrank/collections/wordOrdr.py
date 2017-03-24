from collections import Counter

n = int(raw_input())
words = [raw_input().strip() for x in range(n)]
counts = Counter(words)

print len(counts)

for word in words:
    d = counts.pop(word, None)
    if d == None:
        continue
    else:
        print d, 


Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
