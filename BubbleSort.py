# Bubble Sort using Python
#   O(N^2) Time | O(1) Space

def bubbleSort(array):
    isSorted = False
    counter = 1
    while not isSorted:
        isSorted = True
        for i in range(len(array) - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        counter += 1
    return array
    
N = list(map(int, input().split()))
print(bubbleSort(N))
