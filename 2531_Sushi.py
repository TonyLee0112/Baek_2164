import sys
N,d,k,c = map(int,sys.stdin.readline().strip().split())
# N : 접시 수
# d : 초밥 번호의 최댓값
# k : 연속하여 먹는 접시의 수
# c : 쿠폰 초밥 번호
sushi = []
max_kind = 0
max_set = []
Index = [-1,-1]
for i in range(N) :
    sushi.append(int(sys.stdin.readline()))

a_sushi = [sushi[len(sushi)-1]] + sushi + sushi[0:k]
# a_sushi = [마지막 항,스시~~,k-1개의 스시항 추가]
for probe in range(1,N+1) :
    temp = a_sushi[probe:probe+k]
    sushi_set = set(temp)
    kind_of_sushi = len(sushi_set)
    if kind_of_sushi >= max_kind :
        max_kind = kind_of_sushi
        max_set = temp
        Index = [probe,probe+k-1]
        if c == a_sushi[Index[0]-1] :
            if not c in sushi_set :
                max_kind += 1
                Index = [probe-1, probe + k - 1]
        elif c == a_sushi[Index[1]+1] :
            if not c in sushi_set :
                max_kind += 1
                Index = [probe, probe + k]
print(max_kind)
