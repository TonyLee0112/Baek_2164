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
    if target <= Power[start] :
        return Title[start]
    elif end == start + 1 :
        return Title[end]
    else :
        meanVal = (start+end)//2
        if target > Power[meanVal] :
            return Binary_search(target,meanVal,end)
        elif target == Power[meanVal] :
            return Title[meanVal]
        else :
            return Binary_search(target,start,meanVal)


l = len(Power)
for j in range(M) :
    print(Binary_search(int(sys.stdin.readline()),0,l-1))
