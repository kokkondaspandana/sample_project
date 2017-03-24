if __name__ == '__main__':
    n = int(raw_input())
input_line = raw_input()
input_list = input_line.split()
input_list = map(int, input_list)
t = tuple(input_list)
print hash(t)



i/p:
2
1 2

o/p:
3713081631934410656
