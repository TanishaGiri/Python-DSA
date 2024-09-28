def selectionSort(list):
    for i in range(0, len(list) - 1):
        smallest = i
        for j in range(i + 1, len(list)):
            # compare smallest with j to check the element weight
            if list[smallest] > list[j]:
                smallest = j  # index change for smallest

        # swap the ith element with the smallest element received
        list[i], list[smallest] = list[smallest], list[i]

    return list


list = input("Enter non-swap element in list: ")

# split the input string into list string and then convert them into integer
user_list = [int(x) for x in list.split()]

# pass the user_list to the function and get the result_list
result_list = selectionSort(user_list)

print(selectionSort(result_list))