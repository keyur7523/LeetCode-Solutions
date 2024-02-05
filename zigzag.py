def zigzag(s, n):
    listt = []
    count, j = 0, 0
    while count < len(s):
        for i in range(n):
            if count >= len(s): break
            print(f"1st for loop: i {i} j {j}")
            listt.append((i, j))
            count += 1
        for i in range(n-2, 0, -1):
            if count >= len(s): break
            j += 1
            print(f"2nd for loop: i {i} j {j}")
            listt.append((i, j))
            count += 1
        j += 1
                
    print(listt)
  
    c = 0
    matrix = [[" " for _ in range(list(listt[-1])[1] + 1)] for _ in range(n)]
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if (i, j) == listt[c]:
                matrix[i][j] = s[c]
                if c < len(s)-1:
                    c += 1
            
    for i in matrix:
        print(i)
       
    ss = ''
    for i in matrix:
        ss += ''.join(i)
    ss2 = ss.replace(" ", "")
    print(ss2)
    
zigzag("HIMAJAGOGINENI", 5)