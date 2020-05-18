# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # Initialize swapped so the loop runs
    swapped = True
    while swapped:
        swapped = False
        # Loop through the elements
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                # Swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Set the swapped flag to True
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    # If arr is empty, do nothing
    if len(arr) == 0:
        return arr
    # Find the maximum if not supplied
    if maximum == -1:
        maximum = max(arr)
    m = maximum + 1
    # Initialize the count array with zeroes
    count = [0] * m
    for num in arr:
        # Return error if encountering a negative number
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        # Count the occurrences of num
        count[num] += 1
    i = 0
    for num in range(m):
        # Add `count[num]` copies of `num` to the output array
        for _ in range(count[num]):
            arr[i] = num
            i += 1
    return arr
