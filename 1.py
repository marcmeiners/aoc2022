def elf():
    result = []
    count = 0
    with open("input/1.txt", "r") as f:
        for x in f.readlines():
            if x == "\n":
                result.append(count)
                count = 0
            else:
                count += int(x)
        result.append(count)
    result.sort(reverse = 1)
    return result

def firstPart():
    result = elf()
    return(result[0])

def secondPart():
    result = elf()
    return(result[0] + result[1] + result[2])

print(firstPart())
print(secondPart())