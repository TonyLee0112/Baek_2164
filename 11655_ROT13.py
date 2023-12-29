# 대문자 A~Z = 65 ~ 90
# 소문자 a~z = 97 ~ 122

a = input()
ans = ''
for i in range(len(a)) :
    if not a[i].isspace() :
        oo = ord(a[i]) + 13
        if 77 < oo < 91 or 109 < oo < 123 :
            ans = ans + chr(oo)
        elif 90 < oo < 104 or 122 < oo < 136 :
            oo = oo - 26
            ans = ans + chr(oo)
        else :
            ans = ans + a[i]
    else :
        ans = ans + a[i]

print(ans)
