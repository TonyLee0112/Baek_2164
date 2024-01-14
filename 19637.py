import sys

N, M = map(int, sys.stdin.readline().split())
Title = []
Power = []
for i in range(N):
    title, figure = sys.stdin.readline().split()
    figure = int(figure)
    if i == 0:
        Title.append(title)
        Power.append(figure)
    elif not figure in Power:
        Title.append(title)
        Power.append(figure)


def Binary_search(target, start, end):
    if (Power[start] < target <= Power[end]) :
        if (end == start + 1) :
            return Title[end]
        else :
            meanVal = (start+end)//2
            if target > Power[meanVal] :
                Binary_search(target,meanVal,end)
            elif target == Power[meanVal] :
                return Title[meanVal]
            else :
                Binary_search(target,start,meanVal)
    elif target <= Power[start] :
        return Title[start]

l = len(Power)
for j in range(M) :
    pow = int(sys.stdin.readline())
    print(Binary_search(pow,0,l-1))
