import sys
N, M = map(int, sys.stdin.readline().split())
Title = []
Power = []
for i in range(N):
    title, figure = sys.stdin.readline().split()
    figure = int(figure)
    if i == 0 :
        Title.append(title)
        Power.append(figure)
    if Power[len(Power)-1] == figure :
        continue
    Title.append(title)
    Power.append(figure)
def Binary_search(target):
    start = 0
    end = len(Power) - 1
    if target <= Power[start] :
        return Title[start]
    else :
        while end >= start :
            mean_index = (start+end)//2
            mean_power = Power[mean_index]
            if end == start + 1 :
                return Title[end]
            elif target > mean_power :
                start = mean_index
            elif target < mean_power :
                end = mean_index
            elif target == mean_power :
                return Title[mean_index]

for j in range(M) :
    print(Binary_search(int(sys.stdin.readline())))
