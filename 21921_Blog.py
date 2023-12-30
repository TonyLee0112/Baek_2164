N, X = map(int,input().split())
Daily = list(map(int,input().split()))
s = [Daily[0]]
if Daily == [0] * N:
    print("SAD")
else :
    for i in range(1,N) :
        s.append(Daily[i]+s[i-1])
    maxValue = s[X-1]
    num = 1
    for current_index in range(N-X) :
        if maxValue < s[current_index+X]-s[current_index] :
            maxValue = s[current_index+X]-s[current_index]
        elif maxValue == s[current_index+X]-s[current_index] :
            num += 1
    print(maxValue)
    print(num)
