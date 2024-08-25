def reverseArray(list):
    first = 0
    last = len(list) - 1

    while first < last:
        # swapping python
        list[first], list[last] = list[last], list[first]
        first += 1
        last -= 1

    return list


# Testing the code
list = [1, 2, 3, 4, 5, 6]

reverseArray(list)

for i in list:
    print(i)
