def linearSearch(array, x):

    # Going through array sequencially
    for i in range(0, len(array)):

        if (array[i] == x):  # Comparing every single element
            return i
        
    return -1  # Returns -1 if the element is not found

def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet or pass each other
    while low <= high:

        mid = low + (high - low)//2 # Floor division used to avoid decimal values

        if x == array[mid]:
            return mid  # If the element is found, the function exits and returns the index

        # Set the mid based on comparisons
        elif x > array[mid]:  
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Returns -1 if the element is not found


array1 = [2, 0, 4, 1, 9]        # Unsorted array for linear search
array2 = [3, 4, 5, 6, 7, 8, 9]  # Sorted array for binary search

array1 = array1.sort()  # Sorting the array for linear search

x = 4  # Element to be searched
low = 0
high = len(array2) - 1

result = binarySearch(array2, x, low, high)
# result = linearSearch(array1, x)


if result != -1: 
    print(f"Element is present at index: {result}")
else:
    print("Nhi Mila :(")
