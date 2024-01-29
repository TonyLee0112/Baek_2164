# dijkstra's Algorithm
import sys
ii = sys.stdin.readline
n,d = map(int,ii().split())

# 도로를 d 등분하여 모든 지점들을 node 로 만듦
inf = int(110001)
Map = [[] for _ in range(d+1)]
dist = [inf] * (d+1) # 출발 지점 ~ 각 지점에 대한 최소 비용. 새 지점을 탐색할 때마다 update
cloud = [False] * (d+1) # 방문한 점들을 하나씩 cloud에 넣기.
def dijkstra(start) :
    dist[start] = 0 # 시작 지점의 거리를 0으로 초기화
    while True :
        cnt = -1
        # 방문 X 인 점들 중에 기준 node 로부터 가장 가까운 지점의 index 를 cnt에 저장
        for i in range(d+1) :
            if cloud[i] == False :
                if cnt == -1 :
                    cnt = i
                elif dist[i] < dist[cnt]:
                    cnt = i
        # 방문하지 않은 점들이 없다면 break
        if cnt == -1 :
            break

        # 새 지점 encloud
        cloud[cnt] = True

        for i in Map[cnt] : # cnt : 시작점, Map[cnt]: (도착점,비용)
            cost = dist[cnt] + i[1] # cnt 를 거쳐 도착점까지 갈 때의 비용들을 갱신
            if cost < dist[i[0]] : #i[0] : 끝점의 위치, dist[i[0]] : 이 위치에 대한 최소비용
                dist[i[0]] = cost

# 지름길이 아닌 일반 도로들은 거리가 1인 edge 로 연결
for i in range(d):
    Map[i].append((i + 1, 1))

for _ in range(n):
    start, end, cost = map(int, ii().split())
    if end > d: # 도착점을 넘어가는 지름길은 저장 X
        continue
    Map[start].append((end, cost)) # 지름길들은 일반 도로 뒤에 append


dijkstra(0)
print(dist[d])
