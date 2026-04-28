with open("integer.txt", "r") as data:
    for line in data:
        unsorted_num = int(line.strip())
        if unsorted_num % 2 == 0:
            answer = unsorted_num ** 2
        else:
            answer = unsorted_num ** 3
        print(answer)

