def prio(c):
    if(c.islower()):
        return ord(c) - 96
    else:
        return ord(c) - 38

def firstPart():
    with open("input/3.txt", "r") as f:
        result = 0
        for x in f.readlines():
            fullList = list(x)
            middle = len(fullList)//2
            first = fullList[:middle]
            second = fullList[middle:]
            if '\n' in second:
                second.remove('\n')
            double = list(set(first).intersection(set(second)))
            result += prio(double[0])
    return result

def secondPart():
    with open("input/3.txt", "r") as f:
        currList = []
        result = 0
        for x in f.readlines():
            x = list(x)
            if '\n' in x:
                x.remove('\n')
            currList.append(x)
            if len(currList) == 3:
                double = list(set(currList[0]).intersection(list(set(currList[1]).intersection(set(currList[2])))))
                result += prio(double[0])
                currList = []
    return result

print(firstPart())
print(secondPart())