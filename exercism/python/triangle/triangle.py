def equilateral(sides):
    if valid_triangle(sorted(sides)):
        return min(sides) == max(sides)
    else:
        return False


def isosceles(sides):
    if valid_triangle(sorted(sides)):
        return len(set(sides)) < 3
    else:
        return False

def scalene(sides):
    if valid_triangle(sorted(sides)):
        return len(set(sides)) == 3
    else:
        return False

def valid_triangle(sides):
    if len(sides) != 3 or sides[-1] > (sides[0] + sides[1]) or sides[0] <= 0:
        return False
    return True
