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
Add initial insertion sort program
