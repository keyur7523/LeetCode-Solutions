from collections import defaultdict

def message_delivery(timestamp, messages, k):
    message_dict, delivery_status, count_dict = {}, [], defaultdict(list)
    
    # for x, msg in enumerate(messages):
    #     count_dict[msg] += [timestamp[x]]
        
    # print(f"count = {count_dict}")
    
    
    # for i in range(len(timestamp)):
    #     message_dict[timestamp[i]] = messages[i]
    
    for x, ts in enumerate(sorted(timestamp)):
        if messages[x] not in count_dict.keys():
            #print(f"message: {messages[x]} loop 1")
            delivery_status.append(True)
            count_dict[messages[x]] += [ts]
            
        else:
            #print(f"message: {messages[x]} loop 1")
            if ts - count_dict[messages[x]][-1] < k:
                delivery_status.append(False)
                count_dict[messages[x]] += [ts]
            else:
                delivery_status.append(True)
                count_dict[messages[x]] += [ts]
                
    #print(f"message_dict = {message_dict}\ndelivery_status = {delivery_status}\ncount_dict = {count_dict}")
    #print(f"count = {count_dict}")
    #print(f"delivery = {delivery_status}")
        
    return delivery_status

timestamp = [17]
messages = ["h"] 
k = 5

message_delivery(timestamp, messages, k)