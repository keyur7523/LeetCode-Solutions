
def insert(intervals, newInterval):
    x, flag= 0, 1
    inte = []
    for i in range(len(intervals)):
        print(f"interval: {intervals[i]} inte: {inte}") 
  
        if newInterval[0] > intervals[i][0] and newInterval[0] < intervals[i][1]:
            x = intervals[i][0]
            flag = 0
            print(f"condition 1 x: {x}")
            
        elif newInterval[0] > intervals[i][1] and newInterval[0] < intervals[i+1][0]:
            x = newInterval[0]
            flag = 0
            inte.append(intervals[i]) 
        
        elif newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:
            inte.append([x, intervals[i][1]])
            print(f"condition 2 list: [{x}, {intervals[i][1]}]")
            flag = 1
            
        elif newInterval[1] < intervals[i][0] and newInterval[1] > intervals[i-1][1]:
            inte.append([x, newInterval[1]])
            print(f"condition 3 list: [{x}, {newInterval[1]}]")
            inte.append(intervals[i])
            flag = 1
            
        else:
            if flag: inte.append(intervals[i])
            print(f"condition 4 list: {intervals[i]}")
            
    print(inte)

insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])  # o/p [[1,2],[3,10],[12,16]]
        