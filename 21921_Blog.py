N, X = map(int, input().split())
Daily = list(map(int, input().split()))

s = [Daily[0]]
for i in range(1, N):
    s.append(Daily[i] + s[i - 1])

maxValue = s[X - 1]
num = 1

for current_index in range(N - X):
    current_sum = s[current_index + X] - s[current_index]

    if maxValue < current_sum:
        maxValue = current_sum
        num = 1 # 초기화하는 작업을 빼먹었네
    elif maxValue == current_sum:
        num += 1

if maxValue == 0:
    print("SAD")
else:
    print(maxValue)
    print(num)
