import sys
input = sys.stdin.readline

N = int(input())
data = []
for i in range(N) :
    data.append(list(map(int,input().split())))
data.sort() # data[i][0] 기준 정렬

curX = data[0][0] # 2
curMax_Y = data[0][1] # 4
curSum = 0
max_X = data[N-1][0]+1 # 16
for i in range(1,N) :
    if data[i][1] >= curMax_Y :
        curSum += curMax_Y * (data[i][0] - curX) + data[i][1] * 1
        curMax_Y = data[i][1]
        curX = data[i][0] + 1

if curMax_Y > data[N-1][1] :
    curSum += (max_X - curX) * data[N-1][1]
print(curSum)
