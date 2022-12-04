def firstPart():
    result = 0
    with open("input/4.txt", "r") as f:
        for x in f.readlines():
            pairs = x.split(',')
            firstPair = pairs[0].split('-')
            secondPair = pairs[1].split('-')
            secondPair[1] = secondPair[1][:-1] #remove \n
            if int(firstPair[0]) <= int(secondPair[0]) and int(secondPair[1]) <= int(firstPair[1]):
                result += 1
            elif int(secondPair[0]) <= int(firstPair[0]) and int(firstPair[1]) <= int(secondPair[1]):
                result += 1
    return(result)

def secondPart():
    result = 0
    with open("input/4.txt", "r") as f:
        for x in f.readlines():
            pairs = x.split(',')
            firstPair = pairs[0].split('-')
            secondPair = pairs[1].split('-')
            secondPair[1] = secondPair[1][:-1] #remove \n
            if int(firstPair[0]) <= int(secondPair[0]) and int(secondPair[1]) <= int(firstPair[1]):
                result += 1
            elif int(secondPair[0]) <= int(firstPair[0]) and int(firstPair[1]) <= int(secondPair[1]):
                result += 1      
            elif int(secondPair[1]) >= int(firstPair[1]) and int(secondPair[0]) >= int(firstPair[0]) and int(secondPair[0]) <= int(firstPair[1]):
                result += 1
            elif int(firstPair[1]) >= int(secondPair[1]) and int(firstPair[0]) >= int(secondPair[0]) and int(firstPair[0]) <= int(secondPair[1]):
                result += 1
    return(result)

print(firstPart())
print(secondPart())