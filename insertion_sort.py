"""
MSCS 532 - Assignment 1
Student: Fahad Jafar
Insertion Sort in Monotonically Decreasing Order
"""


def insertion_sort_decreasing(array):
    """
    Sorts an array in monotonically decreasing order
    using the Insertion Sort algorithm.
    """

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


numbers = [34, 8, 64, 51, 32, 21, 90, 17]

print("Original Array:")
print(numbers)

sorted_numbers = insertion_sort_decreasing(numbers.copy())

print("\nSorted Array in Monotonically Decreasing Order:")
print(sorted_numbers)
# Additional test cases to verify the algorithm
test_cases = [
    [5, 2, 9, 1, 5, 6],
    [1, 2, 3, 4, 5],
    [10, 8, 6, 4, 2],
    [4, 4, 2, 9, 9]
]

print("\nAdditional Test Cases:")

for test in test_cases:
    result = insertion_sort_decreasing(test.copy())
    print("Original:", test)
    print("Sorted:", result)
