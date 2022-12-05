def solution(partNr):    
    numberOfStacks = 0
    maxSize = 0
    with open("input/5.txt", "r") as f:
        count = 0
        for x in f.readlines():
            if x[1] == '1': 
                numberOfStacks = int(x[-3])
                maxSize = count
                break
            else: count += 1

    stacks = []
    for i in range(0,numberOfStacks):
        stacks.append([])

    with open("input/5.txt", "r") as f:
        count = 0
        for x in f.readlines():
            if(count < maxSize):
                if x[1] == '1': break
                for i in range (0, numberOfStacks):
                    if x[1+4*i] != ' ':
                        stacks[i].append(x[1+4*i])
                count += 1
            elif(x[0] == 'm'):
                parts = x.split(' ')
                amount = int(parts[1])
                fromStack = int(parts[3]) - 1
                toStack = int(parts[5]) - 1
                moving = stacks[fromStack][:amount]
                if partNr == 1:
                    moving.reverse()
                stacks[toStack] = moving + stacks[toStack]
                del stacks[fromStack][:amount] 
    result = ''
    for i in stacks:
        result = result + i[0]
    return result
    
print(solution(1))
print(solution(2))

        

