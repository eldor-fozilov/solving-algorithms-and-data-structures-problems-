# Time Complexity: O(n(log(n))), n is the number of number of tandem bicycles
# Auxiliary Space Complexity: O(1)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

    redShirtSpeeds.sort(reverse = True)
    if fastest:
        blueShirtSpeeds.sort()
    else:
        blueShirtSpeeds.sort(reverse = True)

    output = 0
    for i in range(len(redShirtSpeeds)):
        output += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    
    return output
