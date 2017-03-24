if __name__ == '__main__':
    N = int(raw_input())
    list=[]
    for x in range(N):
        s=raw_input().split()
        value=s[0]
        value1=s[1:]
        if value!="print":
            value+="("+",".join(value1)+")"
            eval("list."+value)
        else:
                print list



i/p:12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print


o/p:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

