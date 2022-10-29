"""
Reverse the given list. If the elements of the list contain a list, reverse the inner list too.

Example:
input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def reverse(a):
    new=a[::-1]
    return new

def inner_reverse(bb):
    new=[]
    for sublist in bb:
        for b in bb:
            new.append(b[::-1])
        return new

print(inner_reverse(reverse(input)))
