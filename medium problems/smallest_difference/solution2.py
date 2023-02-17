# O(nlog(n) + mlog(m)) time | O(1) space, n is the length of the first input array
# and m is the length of the second input array


from math import inf

def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0
    smallest = inf
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        currentNum = None
        
        if firstNum < secondNum:
            currentNum = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            currentNum = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if currentNum < smallest:
            smallest = currentNum
            smallestPair = [firstNum, secondNum]
    return smallestPair
