def solution(bridge_length, weight, truck_weights):
    answer = 0
    length = len(truck_weights)
    bridge = []
    finish = []
    while len(finish) < length:
        answer += 1
        cur_weight = 0
        if bridge:
            for i in range(len(bridge)):
                if bridge[i][0] == 0:
                    continue
                bridge[i][1] = bridge[i][1] + 1
                if bridge[i][1] > bridge_length:
                    finish.append(bridge[i][0])
                    bridge[i] = [0, 0]
                else:
                    cur_weight = cur_weight + bridge[i][0]
            if truck_weights and (cur_weight + truck_weights[0] <= weight):
                bridge.append([truck_weights.pop(0),1])
        else:
            if truck_weights:
                bridge.append([truck_weights.pop(0),1])
        
    
    return answer