import math, time, random
import matplotlib.pyplot as plt
import matplotlib
 
def enumeration(array):
    maxSum = None
    start, end = 0, 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            tmpSum = 0
            for k in range(i, j):
                tmpSum += array[k]
                if(tmpSum > maxSum or maxSum is None):
                    maxSum = tmpSum
                    start = i
                    end = j-1
    return maxSum, start, end
 
def better_enumeration(array):
    maxSum = None
    start, end = 0, 0
    for i in range(len(array)):
        tmpSum = 0
        for j in range(i,len(array)):
            tmpSum += array[j]
            if(tmpSum > maxSum or maxSum is None):
                maxSum = tmpSum
                start = i
                end = j
    return maxSum
 
def divide_and_conquer(array, leftIndex, rightIndex):
    maxSum = 0
    if(leftIndex == rightIndex):
        start = leftIndex
        end = rightIndex
        if(array[leftIndex] > 0):
            maxSum = array[leftIndex]
        else:
            maxSum = 0
    else:
        centerIndex = int(math.floor((leftIndex+rightIndex)/2))
        leftMaxSum, leftStart, leftEnd = divide_and_conquer(array, leftIndex, centerIndex)
        rightMaxSum, rightStart, rightEnd = divide_and_conquer(array, centerIndex+1, rightIndex)
 
        leftExtendMaxSum = 0
        leftExtendTempSum = 0
        tmpIndex1 = 0
 
        for i in range(centerIndex, leftIndex, -1):
            leftExtendTempSum += array[i]
            if(leftExtendTempSum > leftExtendMaxSum):
                tmpIndex1 = i
                leftExtendMaxSum = leftExtendTempSum
 
        rightExtendMaxSum = 0
        rightExtendTempSum = 0
        tmpIndex2 = 0
 
        for i in range(centerIndex+1, rightIndex):
            rightExtendTempSum += array[i]
            if(rightExtendTempSum > rightExtendMaxSum):
                tmpIndex2 = i
                rightExtendMaxSum = rightExtendTempSum
 
        maxSum = leftExtendMaxSum + rightExtendMaxSum
        start = tmpIndex1
        end = tmpIndex2
 
        if(maxSum < leftMaxSum):
            start = leftStart
            end = leftEnd
            maxSum = leftMaxSum
        if(maxSum < rightMaxSum):
            start = rightStart
            end = rightEnd
            maxSum = rightMaxSum
    return maxSum, start, end       
 
def dynamic_programming(array):
    maxSum = 0
    tmpSum = 0
    start = 0
    end = 0
 
    for i in range(len(array)):
        if(tmpSum > 0):
            tmpSum += array[i]
        else:
            tmpSum = array[i]
            start = i
        if(tmpSum > maxSum):
            maxSum = tmpSum
            end = i
    return maxSum
 
#print divide_and_conquer(array, 0, len(array)-1)
#print Dynamic()
 
 
if __name__ == '__main__':
    random.seed(666)
    r100 = [random.randint(-100, 100) for x in range(100)]
    r200 = [random.randint(-100, 100) for x in range(200)]
    r300 = [random.randint(-100, 100) for x in range(300)]
    r400 = [random.randint(-100, 100) for x in range(400)]
    r500 = [random.randint(-100, 100) for x in range(500)]
    r600 = [random.randint(-100, 100) for x in range(600)]
    r700 = [random.randint(-100, 100) for x in range(700)]
    r800 = [random.randint(-100, 100) for x in range(800)]
    r900 = [random.randint(-100, 100) for x in range(900)]
 
    startTime = time.time()
    print divide_and_conquer(r100, 0, len(r100)-1)
    elapsedTime = time.time() - startTime
    print '1 ',elapsedTime
    plt.scatter(100, elapsedTime, color= 'black', label= 'Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('aa')
    plt.legend()
    plt.show()
 
    startTime = time.time()
    print divide_and_conquer(r200, 0, len(r200)-1)
    elapsedTime = time.time() - startTime
    print '2 ',elapsedTime
 
    startTime = time.time()
    print divide_and_conquer(r300, 0, len(r300)-1)
    elapsedTime = time.time() - startTime
    print '3 ', elapsedTime
 
    startTime = time.time()
    print divide_and_conquer(r400, 0, len(r400)-1)
    elapsedTime = time.time() - startTime
    print '4 ',elapsedTime
 
    startTime = time.time()
    print divide_and_conquer(r500, 0, len(r500)-1)
    elapsedTime = time.time() - startTime
    print '5 ',elapsedTime
 
    startTime = time.time()
    print divide_and_conquer(r600, 0, len(r600)-1)
    elapsedTime = time.time() - startTime
    print '6 ',elapsedTime
 
    startTime = time.time()
    print divide_and_conquer(r700, 0, len(r700)-1)
    elapsedTime = time.time() - startTime
    print '7 ',elapsedTime
 
    startTime = time.time()
    print divide_and_conquer(r800, 0, len(r800)-1)
    elapsedTime = time.time() - startTime
    print '8 ',elapsedTime
 
    startTime = time.time()
    print divide_and_conquer(r900, 0, len(r900)-1)
    elapsedTime = time.time() - startTime
    print '9 ',elapsedTime