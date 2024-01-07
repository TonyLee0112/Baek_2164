# 오름차순으로 정렬된 사람들을 기억에 따라 재배열
N = int(input())
Unarranged = list(map(int,input().split()))
ans = [0]*N
# 키가 가장 작은 사람 = 재배열 시 위치가 고정됨.
# 키가 가장 작은 사람부터 배열한 후, 그 사람은 제외
for index in range(N) :
    ans[Unarranged[index]] = index + 1
    Unarranged.pop(index)

