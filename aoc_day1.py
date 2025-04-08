def quicksort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Recursive case
    pivot = len(arr) // 2
    print("pivot", pivot)
    left = [x for x in arr if x < arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]
    # quicksort(arr=left) arr or list left + plus pivot as that
    # is in the middle of the two lists.  Then arr=right which is
    # the higher numbers and quicksort is done.  Now we also could have
    # sort or sorted but we are using quicksort as it is a recursive
    # function that will sort the list.  We could also use a lambda
    # function.  The lambda function would be a one liner and we could use it
    # to sort the list.
    return quicksort(left) + [arr[pivot]] + quicksort(right)


def compare_to(list1, list2):
    i = 0
    list_diff = 0
    total = 0
    while i < len(list1):
        if len(list1) != len(list2):
            print("Lists are not the same length")
            break
        list_diff = abs(list1[i]) - abs(list2[i])
        print(list_diff)
        i += 1
        total += abs(list_diff)
    print(list_diff, total)
    return list_diff, total


list3 = []
list4 = []


with open("aoc_day1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        list3.append(int(line.split(" ")[0]))
        print(type(list3[0]))
        list4.append(int(line.split()[1]))
        print(type(list4[0]))
        # process each line subtracting the values
        # then saving the total and adding them up
        print(list3, list4)
        # now we need to compare the two lists and get the difference
    sorted_list3 = sorted(list3)
    sorted_list4 = sorted(list4)
    print(sorted_list3, sorted_list4)
    qs_list3 = quicksort(list3)
    qs_list4 = quicksort(list4)
    print(qs_list3, qs_list4)
    if qs_list3 == sorted_list3 and qs_list4 == sorted_list4:
        print("Lists are the same")
    diff_sorted = compare_to(sorted_list3, sorted_list4)
    diff_qs = compare_to(qs_list3, qs_list4)
    print(diff_sorted, diff_qs)


    total_difference = 0
    a = [int(x) for x in qs_list3]
    b = [int(x) for x in qs_list4]
    differences = [abs(a - b) for a, b in zip(a, b)]
    print(differences)
    total_difference = sum(differences)
    total_difference2 = 0
    for difference in differences:
        total_difference2 += difference
    print(total_difference)
    print(total_difference2)
    print("Total difference:", total_difference)
    print("Total difference2:", total_difference2)
