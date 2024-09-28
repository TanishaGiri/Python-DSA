def binarySeachIterative(list, x, low, high):
    mid = low + (high-low)//2;

    if x == list[mid]:
        return mid
    elif x > list[mid]:
        low = mid + 1
    else:
        high = mid - 1

    return -1

list = input("Enter a list: ")
user_list = [int(x) for x in list.split()]

x = int(input("Enter the element need to be searched: "))

# low = 0
# high = len(list)-1

result = binarySeachIterative(user_list, x, 0, len(user_list)-1)
print(result)