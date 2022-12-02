def mapping(letter):
    if(letter == "A" or letter == "X"):
        return 0
    elif(letter == "B" or letter == "Y"):
        return 1
    else:
        return 2

def solutions():
    with open("input/2.txt", "r") as f:
        result = [0,0]
        for x in f.readlines():
            them = mapping(x[0])
            me = mapping(x[2])
            result[0] += ((me - them + 1) % 3) * 3  + (me + 1)
            result[1] += (me + them + 2) % 3 + 1 + (me * 3)
    return result

def firstPart():
    x = solutions()
    return x[0]

def secondPart():
    x = solutions()
    return x[1]
           
print(firstPart())
print(secondPart())