with open("integer.txt", "r") as data, \
     open("double.txt", "w") as even_file, \
     open("triple.txt", "w") as odd_file:

    for line in data:
        unsorted_num = int(line.strip())
        if unsorted_num % 2 == 0:
            answer = unsorted_num ** 2
            str(answer + "\n")
            even_file.write(answer)
        else:
            answer = unsorted_num ** 3
            str(answer + "\n")
            odd_file.write(answer)
            
        print(answer)

