#BFS
from collections import deque
import sys
input = sys.stdin.readline
Test_case = int(input())

def bfs(x,y,tarX,tarY) :

    dx = [2,1,-1,-2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]

    q = deque()
    q.append([x,y])

    while q : # deque 의 장점 : list 와 달리 원소가 없으면 False 반환함
        cur = q.popleft()
        curX, curY = cur[0], cur[1]
        # 목표지점 발견
        if cur == [tarX,tarY] :
            return Map[curY][curX] - 1 # 시작점의 1 제거
        else :
            # 8방향 탐색 후 방문 안한 지점들은 deque 에 append
            for i in range(8) :
                X = curX + dx[i]
                Y = curY + dy[i]
                if (0 <= X < I) and (0 <= Y < I) :
                    if Map[Y][X] == 0 : # Non-visited
                        Map[Y][X] = Map[curY][curX] + 1 # 이동할때마다 기존 거리 + 1 하여 누적
                        q.append([X,Y])

for _ in range(Test_case) :
    I = int(input())
    startX, startY = map(int,input().split())
    targetX, targetY = map(int, input().split())

    Map = [[0]*I for _ in range(I)]
    Map[startY][startX] = 1
    print(bfs(startX,startY,targetX,targetY))
