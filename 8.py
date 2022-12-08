values = []
with open("input/8.txt", "r") as f:
    index = 0
    for x in f.readlines():
        if '\n' in x:
            x = x[:-1]
        inner = []
        for c in x:
            inner.append(int(c))
        values.append(inner)
        index += index

n = len(values)
m = len(values[0])

def firstPart():
    result = [[False]*m for _ in range(n)]

    #left and right
    for i in range (0, n):
        maxLeft = values[i][0]
        maxRight = values[i][m-1]
        result[i][0] = True
        result[i][m-1] = True
        for j in range (1, m-1):
            if values[i][j] > maxLeft:
                result[i][j] = True
                maxLeft = values[i][j]
            if values[i][m-j-1] > maxRight:
                result[i][m-j-1] = True
                maxRight = values[i][m-j-1]

    #top and bottom
    for j in range (0, m):
        maxTop = values[0][j]
        maxBottom = values[n-1][j]
        result[0][j] = True
        result[n-1][j] = True
        for i in range (1,n-1):
            if values[i][j] > maxTop:
                result[i][j] = True
                maxTop = values[i][j]
            if values[n-i-1][j] > maxBottom:
                result[n-i-1][j] = True
                maxBottom = values[n-i-1][j]

    count = 0
    for i in range (0, n):
        for j in range (0, m):
            if result[i][j]:
                count += 1
    return count

def secondPart():
    result = [[1]*m for _ in range(n)]

    #left and right
    for i in range (0, n):
        for j in range (1, m):
            number = j
            for k in range(1,j):
                if(values[i][j-k]) >= values[i][j]:
                    number = k
                    break
            result[i][j] *= number
        for j in range(0, m-1):
            number = m-j-1
            for k in range(j+1, m):
                if(values[i][k] >= values[i][j]):
                    number = k-j
                    break
            result[i][j] *= number

    #top and bottom
    for j in range (0, m):
        for i in range (1, n):
            number = i
            for k in range(1,i):
                if(values[i-k][j]) >= values[i][j]:
                    number = k
                    break
            result[i][j] *= number
        for i in range(0, n-1):
            number = n-i-1
            for k in range(i+1, n):
                if(values[k][j] >= values[i][j]):
                    number = k-i
                    break
            result[i][j] *= number
            
    max = 0
    for i in range (0, n):
        for j in range (0, m):
            if result[i][j] > max:
                max = result[i][j]
    return max

print(firstPart())
print(secondPart())