S = input()
T = input()
def Reversed_OP1(string) : # 문자열 끝 부분 A 제거
    return string[:len(string)-1]
def Reversed_OP2(string) : # 문자열 처음 부분 B 제거 후 Reverse
    s = string[1:]
    return ''.join(reversed(list(s)))
def Reversed_Search(string,target_str) : # cnt <= OP_times
    if len(string) < len(target_str) :
        return 0
    else :
        if string == target_str :
            return 1
        elif (string[0] == 'B') and (string[-1] == 'A') :
            Rev_OP1 = Reversed_OP1(string)
            Rev_OP2 = Reversed_OP2(string)
            Result_1 = Reversed_Search(Rev_OP1,target_str)
            Result_2 = Reversed_Search(Rev_OP2,target_str)
            if Result_1 + Result_2 > 0 :
                return 1
            else :
                return 0
        elif string[0] == 'B' :
            Rev_OP2 = Reversed_OP2(string)
            return Reversed_Search(Rev_OP2, target_str)
        elif string[-1] == 'A' :
            Rev_OP1 = Reversed_OP1(string)
            return Reversed_Search(Rev_OP1, target_str)
        else :
            return 0

print(Reversed_Search(T,S))
