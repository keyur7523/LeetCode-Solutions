def efficient_servers(memory):
    idx_max = len(memory) // 2
    efficiency_max = 0
    mem = list(memory)
    for idx in range(1, idx_max+1):
        print(f"idx = {idx}")
        for i in range(idx_max):
            print(f"i = {i} len(mem) - i - 1 = {len(mem) - i - 1}")
            if len(mem) - 2 * (i) - 2 <= idx:
                temp = mem[i]
                mem[i] = mem[len(mem) - i - 1]
                mem[len(mem) - i - 1] = temp
            print(f"memory = {memory} mem = {mem}")
            
            eff = 0    
            for x, m in enumerate(mem):
                eff += (x+1) * m
            
            print(f"efficiency = {eff}")        
            efficiency_max = max(efficiency_max, eff)
                
    print(f"The max efficiency is {efficiency_max}")            

efficient_servers([5,4,1,5,3,2])