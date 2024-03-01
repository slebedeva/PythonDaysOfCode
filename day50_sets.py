# Create a program that finds the intersection and union of two sets

def diff_inter(set1:set, set2:set) -> tuple[set]:
    return set1.intersection(set2), set1.union(set2)
