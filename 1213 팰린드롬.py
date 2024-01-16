String = input()
length = len(String)
Queue = []
front_str = []
back_str = []
for i in String :
    if i in Queue :
        Queue.remove(i)
        front_str.append(i)
        back_str.append(i)
    else :
        Queue.append(i)
front_str.sort()
back_str.sort()
if len(Queue) == 1 :
    front = ''.join(front_str)
    back = ''.join(reversed(back_str))
    result = front + Queue[0] + back
    print(result)
elif len(Queue) == 0 :
    front = ''.join(front_str)
    back = ''.join(reversed(back_str))
    result = front + back
    print(result)
else :
    print("I'm Sorry Hansoo")
