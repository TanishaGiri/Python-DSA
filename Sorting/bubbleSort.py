def bubbleSort(list):   # Time complexity is O(n^2)
    for i in range(0, len(list)-1):
        for j in range(0, len(list)-1-i):
            if list[j] > list[j+1]:
                # swapping the i and j index element
                list[j], list[j+1] = list[j+1], list[j];

    for i in range(len(list)):
        print(list[i])


list = [1, 2, 6, 4, 3, 5]
bubbleSort(list)