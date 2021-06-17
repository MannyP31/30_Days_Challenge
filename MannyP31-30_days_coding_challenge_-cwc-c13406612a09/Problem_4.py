import math

def isRectangle(a1, a2, b1, b2, c1, c2, d1, d2):

    # A = (a1, a2), B = (b1, b2), C = (c1, c2), D = (d1, d2) -> points
    AB = int(math.pow(b1-a1, 2) + math.pow(b2-a2, 2))
    BC = int(math.pow(b1-c1, 2) + math.pow(b2-c2, 2))
    CD = int(math.pow(c1-d1, 2) + math.pow(c2-d2, 2))
    DA = int(math.pow(d1-a1, 2) + math.pow(d2-a2, 2))
    AC = int(math.pow(c1-a1, 2) + math.pow(c2-a2, 2))
    BD = int(math.pow(b1-d1, 2) + math.pow(b2-d2, 2))

    if AB^BC^CD^DA^AC^BD == 0:
        return True
    return False

print(isRectangle(2,0,0,2,2,2,0,0))