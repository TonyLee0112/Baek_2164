import sys
input = sys.stdin.readline
num = int(input())
Switches = [False] + list(map(int,input().split()))
students = int(input())
# len(Switches) = num + 1
# 0 < index < len(Switches)
def turn(index) :
    Switches[index] = 1 - Switches[index]

def side_compare(index,step) :
    if Switches[index-step] == Switches[index+step] :
        return 1
    else :
        return 0

for i in range(students) :
    gender, given_num = map(int,input().split())
    if gender == 1 : # 남학생
        cnt = given_num
        while cnt <= num :
            turn(cnt)
            cnt += given_num
    else : #여학생
        turn(given_num)
        cnt = 1
        while (given_num > cnt) and (given_num+cnt < len(Switches)) :
            if side_compare(given_num,cnt) == 1 :
                turn(given_num + cnt)
                turn(given_num - cnt)
                cnt += 1

for i in range(1,num+1) :
    print(Switches[i],end=" ")
    if i % 20 == 0 :
        print()
