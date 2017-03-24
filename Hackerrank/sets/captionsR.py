d=input();  
a=raw_input().split();  
s1=set();  #all unique room number
s2=set();  #all unique room number occur more than once
for i in a:
    if  i in s1:
        s2.add(i);
    else:
        s1.add(i);
s3=s1.difference(s2);
print list(s3)[0];

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output

8
