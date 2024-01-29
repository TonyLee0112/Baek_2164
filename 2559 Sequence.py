import sys
input = sys.stdin.readline
total, piece = map(int,input().split())
temp = list(map(int,input().split()))

curSum = sum(temp[:piece])
maxVal = curSum
for cur in range(total-piece) :
    curSum += temp[cur+piece] - temp[cur]
    if curSum > maxVal :
        maxVal = curSum
print(maxVal)
