# Python implementation of Binary Indexed Tree
# Binary Indexed Tree or Fenwick Tree is used to
# to prefix operations with updates efficiently.

# Update - O(log n)
# Prefix Sum - O(log n)


# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITTree[].
def getsum(BITTree, i):
    s = 0
    i = i+1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s

# Updates a node in Binary Index Tree (BITree) at given index
# in BITree. The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.


def updatebit(BITTree, n, i, v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)


# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
    BITTree = [0]*(n+1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree


# Driver code to test above methods
arr = [3, 6, 0, 5, 2, 9, -1]
BITTree = construct(arr, len(arr))
print("Sum of elements in arr[0..6] is " + str(getsum(BITTree, 6)))
arr[2] += 4
updatebit(BITTree, len(arr), 2, 4)
print("Sum of elements in arr[0..6]" +
      " after update is " + str(getsum(BITTree, 6)))
