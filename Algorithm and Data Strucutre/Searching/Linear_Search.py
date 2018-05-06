def linear_search(myItem, myList):
    found = False
    position = 0

    while ((position < len(myList)) and not found):
        if (myList[position] == myItem):
            found = True
        position = position + 1

    return found

if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = int(input("Enter your number: "))
    search_item = linear_search(item, num_list)
    if search_item:
        print('Your number is present in the list.')
    else:
        print('Your number is not there in the list.')