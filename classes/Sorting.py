def bubbleSort(array):

  # loop to access each array element
  for i in range(len(array)): ## Will run 5 times 0 -> 4

    # loop to compare array elements
    for j in range(0, len(array) - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j + 1] < array[j]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

data = [-2, 45, 0, 11, -9]


"""
In the above algorithm, all the comparisons are made even if the array is already sorted.
This goes on until the last element of the array which is not efficient for large arrays.

To solve this, we can introduce an extra boolean variable "swapped".
The value of swapped is set to "True" if there occurs swapping of elements. Otherwise, it is set to "False".

After an iteration, if there is no swapping, the value of swapped will be "False".
This means elements are already sorted and there is no need to perform further iterations.

This will reduce the execution time and helps to optimize the bubble sort.
"""


def bubbleSort_optimized(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:  # Same as: if swapped == False:, if swapped != True:
      break



bubbleSort(data)
bubbleSort_optimized(data)

print('Sorted Array in Ascending Order:')
print(data)
