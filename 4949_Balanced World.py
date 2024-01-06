import sys
while True :
    strings = sys.stdin.readline()
    Bracket = []
    Error_code = 0
    if strings[0] == "." :
        break
    else :
        for element in strings :
            if Error_code == 0 :
                if element == "[" or element == "(":
                    Bracket.append(element)
                elif element == "]":
                    if len(Bracket) > 0 and Bracket[len(Bracket)-1] == "[":
                        Bracket.pop()
                    else :
                        Error_code = 1 # Error
                elif element == ")":
                    if len(Bracket) > 0 and Bracket[len(Bracket)-1] == "(":
                        Bracket.pop()
                    else:
                        Error_code = 1  # Error
        if Error_code == 1 or len(Bracket) != 0 :
            print("no")
        else :
            print("yes")
