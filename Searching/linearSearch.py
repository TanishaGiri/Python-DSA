def linearSearch(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i;

    return -1;


list = input("Enter the list: ")
x = int(input("Enter te element need to be searched: "))

user_list = [int(x) for x in list.split()]

result_list = linearSearch(user_list, x)

print(result_list)
