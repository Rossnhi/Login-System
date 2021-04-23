def maxxxx(s):
    o = 0
    O = 0
    res = 0
    for i in range(len(s)):
        l = s[-i-1]
        if l == "O":
            O += 1
        elif l == "o":
            o += 1
        elif l == "i":
            if o > 0:
                o -= 1
            else:
                O -= 1
        else:
            if O > 0:
                O -= 1
                res += 1
            else:
                o -= 1
    return(res)

t = int(input())
for test_case in range(t):
    s = input()
    print(f"case #{test_case + 1}: {maxxxx(s)}")

