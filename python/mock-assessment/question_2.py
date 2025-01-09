import math

def union(objectA, objectB):
    """
    a function that return union of two sets of spheres without redundant spheres

    args:
        objectA (set of tuples): set of spheres (x, y, z, radius)
        objectB (set of tuples): set of spheres (x, y, z, radius)

    returns:
        set of tuples: union of the two sets of spheres without redundant spheres
    """
    # combine all spheres from both objects
    combined = list(objectA) + list(objectB)
    result = []
    # iterate over each sphere
    for i, s1 in enumerate(combined):
        x1, y1, z1, r1 = s1
        # check if s1 is contained within any other sphere
        contained = any(
            math.dist((x1, y1, z1), (x2, y2, z2)) + r1 <= r2
            for j, (x2, y2, z2, r2) in enumerate(combined) if i != j
        )
        # if not contained, add to result
        if not contained:
            result.append(s1)
    # return result as a set
    return set(result)