def solution(x, queries):
    v, k = [], []
    while (x > 0):
        v.append(int(x % 2))
        x = int(x / 2)
    for i in range(0, len(v)):
        if (v[i] == 1):
            k.append(2**i)
    
    solution = []
    for query in queries:
        if query[0] == query[1]:
            solution.append(k[query[0]-1]%query[2])
        else:
            print(query)
            solution.append((k[query[0]-1]*k[query[1]-1])%query[2])
           
    return solution
    
solution(26, [[1, 2, 1009], [3, 3, 5]])