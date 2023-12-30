N, X = map(int, input().split())
Daily = list(map(int, input().split()))

s = [Daily[0]]
for i in range(1, N):
    s.append(Daily[i] + s[i - 1])

maxValue = s[X - 1]
num = 1

for current_index in range(1, N - X + 1):
    current_sum = s[current_index + X - 1] - s[current_index - 1]

    if maxValue < current_sum:
        maxValue = current_sum
        num = 1
    elif maxValue == current_sum:
        num += 1

if maxValue == 0:
    print("SAD")
else:
    print(maxValue)
    print(num)
