def solution(number):
    with open("input/6.txt", "r") as f:
        x = f.readline()
        for i in range(number-1,len(x)):
            currSet = set()
            for j in range(i-number+1,i+1):
                currSet.add(x[j])
            if(len(currSet) == number):
                return i+1

print(solution(4))
print(solution(14))

