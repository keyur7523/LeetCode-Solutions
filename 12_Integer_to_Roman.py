def intToRoman(num):
    ro = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    div = [1000, 500, 100, 50, 10, 5, 1]
    c = 0
    s = []
    while num:
        d = num//div[c]
        m = num%div[c]
        print(f"d:{d} m:{m}")
        if d:
            flag = 1
            if d == 5:
                s.append(ro[c-1])
                #d -= 5
                print(f"d: {d} s: {s}")
                flag = 0
            if d > 5 and d < 9:
                s.append(ro[c-1])
                d -= 5
                
            if d in [4,9]:
                s.append(ro[c])
                if d == 4: s.append(ro[c-1])
                if d == 9: s.append(ro[c-2])
                flag = 0
                print(f"d: {d} s: {s}")
            if flag:
                for _ in range(d):
                    s.append(ro[c])
                print(f"d: {d} s: {s}")
            num = m
        else:
            c += 2
        print(''.join(s))
              
intToRoman(58)
intToRoman(1994)


    