#시간복잡도 O(logN)
N = int(input())
N_binary = bin(N)
digit = len(N_binary)-2
sum_digits = 0
if N == 0 or N == 1 :
    print(N)
else :
    second_exp = digit-2 # 2^second_exp
    for i in N_binary[3:] :
        if i == '1' :
            sum_digits += 2*pow(2,second_exp)
        second_exp -= 1

    if sum_digits == 0 :
        print(N)
    else :
        print(sum_digits)
