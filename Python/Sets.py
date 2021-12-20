# Sets
# Python also includes a data type for sets.
# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

# Sets may be constructed several ways
# Empty set
s = set()
s = set('gvhvh')
print(s)

# Set comprehension
s = {x for x in [1, 2, 1, 2, 3]}
print(s)

# Literal syntax
s = {'F', 2, 3}
print(s)

a = set('gfhfjhfjba')
b = set('gcDLADM.N')

# Union
print(a | b)

# Intersection
print(a & b)

# Difference
print(a - b)

# Symmetric difference(letter in a or b but not in both)
print(a ^ b)
