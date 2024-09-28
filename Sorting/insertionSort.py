def insertionSort(list): # O(n^2)
    #steps to be followed
    #1. sorted and unsorted divided
    #2. take element from the unsorted and place oint he sorted list on there current position
    #3. until and unless they did not find there current position use a while loop to iterate
    for i in range(0, len(list)):
        current = list[i]
        j = i-1
        while j >= 0 and current < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = current

    return list

list = input("Enter elements in non-sored form: ")

# split the string into various string and convert them into integer
user_list = [int(x) for x in list.split()]

# pass the user_list into insertion sort function
result_list = insertionSort(user_list)

print(result_list)