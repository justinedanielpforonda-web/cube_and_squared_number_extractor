with open("integer.txt", "r") as data:
    for line in data:
        unsorted_num = int(line.strip())
        if unsorted_num % 2 == 0:
            print("even")
        else:
            print("odd")
