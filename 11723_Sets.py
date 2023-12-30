import sys
s = set()
M = int(sys.stdin.readline())  //readline 쓰니까 시간초과 문제 해결됨
for i in range(M):
    I = sys.stdin.readline().strip().split()
    if len(I) == 2 :
        I[1] = int(I[1])

    if I[0] == 'add':
        s.add(I[1])

    elif I[0] == 'check':
        if I[1] in s :
            print(1)
        else :
            print(0)

    elif I[0] == 'remove' :
        if I[1] in s :
            s.remove(I[1])

    elif I[0] == 'toggle' :
        if I[1] in s:
            s.remove(I[1])
        else:
            s.add(I[1])

    elif I[0] == 'all' :
        s = set(range(1,21))

    elif I[0] == 'empty' :
        s = set()
