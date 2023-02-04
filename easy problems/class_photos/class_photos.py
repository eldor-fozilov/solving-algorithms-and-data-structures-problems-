# Time Complexity: O(nlog(n)) - n is the number of student in the class
# Space Complexity: O(n) - the input size

def classPhotos(redShirtHeights, blueShirtHeights):

    redShirtHeights.sort()
    blueShirtHeights.sort()

    reds_high_count = blues_high_count = 0
    
    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] > blueShirtHeights[i]:
            reds_high_count += 1
        elif redShirtHeights[i] == blueShirtHeights[i]:
            return False
        else:
            blues_high_count += 1

    if reds_high_count == len(redShirtHeights) or blues_high_count == len(blueShirtHeights):
        return True
    
    return False
