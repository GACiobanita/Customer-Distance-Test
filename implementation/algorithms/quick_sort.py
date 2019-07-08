# Implementation of the Divide and Conquer algorithm Quick Sort
# Borrowed from: https://www.geeksforgeeks.org/quick-sort/
# Code by Mohit Kumra
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] <= pivot:
            # increment index of smaller element 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements quick_sort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 

# Function to do Quick sort
def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high)

        # Separately sort elements before 
        # partition and after partition 
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
