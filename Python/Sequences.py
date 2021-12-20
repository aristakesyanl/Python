from collections import deque

# There are three basic sequence types: lists, tuples and ranges objects
# Common operations on sequences listed in ascending priority
# x in s true is x in s, false otherwise
# x not in s true if sis not in s, false otherwise
# s + t concatenation of s and t
# s * n or n * s add s to itself n times
# s[i] ith element of the sequence
# s[i:j] slicing s from i to j
# s[i:j:k] slicing s from i to j with step k
# len(s) length of s
# min(s) smallest of s
# max(s) largest of s
# s.index(x[, i[, j]]) index of first occurrence of x in s(or starting from i and before index j)
# s.count(x) total number of occurrences x in s
colors = ['red', 'green', 'black', 'yellow', 'brown']
more_colors = ['pink', 'blue', 'white']
print('white' in colors)
print('white' not in colors)
print(colors + more_colors)
# indexing starts from 0
print(colors[0])
print(colors[0:3])
# starts from 0 index
print(colors[:4])
# goes till the last element
print(colors[2:])
print(colors[0:5:2])
print(len(colors))
# prints lexicographically largest
print(max(colors))
# prints lexicographically smallest
print(min(colors))
print(colors.index('green'))
print(colors.count('yellow'))

# Lists
# List are mutable object typically used to store homogeneous items
# Lists may be constructed several ways
# Empty list []
s = []
print(s)
# Using square brackets
s = [1, 2, 3]
print(s)
# Using a list comprehension
s = [x for x in '1234']
print(s)
# using type constructor
s = list()
print(s)
s = list('abcd')
print(s)

# Lists implement all common and mutable operations
# List methods

# list.append() add an item to the end of the list
colors.append('grey')
print(colors)
# colors.append(more_colors)
# print(colors)

# list.extend() extends list from iterable
colors.extend(more_colors)
print(colors)

# list.insert(i,x) inserts x in given position
colors.insert(2, 'white')
print(colors)

# list.remove(x) removes first item from the list whose value is equal to x
colors.remove('white')
print(colors)

# list.pop(i) removes item in ith position and returns it
color = colors.pop(2);
print(color)
print(colors)

# list.sort() sorts list in place
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
# if you want sorted list without altering the original use sorted()
new_sort = sorted(more_colors)
print(new_sort)
print(more_colors)

# list.reverse() reverse the list
more_colors.reverse()
print(more_colors)

# list.copy() returns a copy of the list
new_colors = colors.copy()
print(new_colors)

# Using lists as stack
# Use append() and pop methods
stack = [1, 3, 5, 12]
stack.append(23)
print(stack)
stack.pop()
print(stack)

# Using lists as queues
# Queues can be implemented using list insert() and pop() methods
# But this is not efficient
# Instead use collections.deque to implement lists
queue = deque([1, 3, 5, 6])
queue.append(13)
queue.append(56)
print(queue)
queue.popleft()
print(queue)

# Tuples
# Tuples are immutable sequences, typically used to store collections of heterogeneous data
# Tuples may be constructed in a number of ways
# Using () to denote an empty tuple
t = ()
print(t)
# Using a trailing comma for a singleton tuple
t = 123,
print(t)
# Using items with commas
t = (1, 2, 45, 63)
print(t)
# Using tuple()
t = tuple()
print(tuple)
t = tuple('abnbdh')
print(t)
# Note that it is comma that make tuple, not parenthesis
# Tuple implement all common sequence operations


# Ranges
# The range type represents an immutable sequence of numbers
# and is commonly used for looping a specific number of times in for loops.
# class range(stop)
# class range(start, stop[, step])
# The arguments to the range constructor must be integers
# (either built-in int or any object that implements the __index__() special method).
# If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0.
num = list(range(10))
print(num)
num = list(range(1, 10, 2))
print(num)


