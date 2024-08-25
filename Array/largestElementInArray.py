def largestNumber(list):

    largest = float('-inf') # Initializing the largest variable with negative infinity

    for i in list:
        if list[i] > largest:
            largest = list[i]

    return largest


list = [1, 2, 5, 4, 6, 3, 2]
print(largestNumber(list))