def process_even_odd_numbers():
    try:
        with open("integer.txt", "r") as data, \
        open("double.txt", "w") as even_file, \
        open("triple.txt", "w") as odd_file:

            for line in data:
                unsorted_num = int(line.strip())

                if unsorted_num % 2 == 0:
                    answer = unsorted_num ** 2
                    even_file.write(str(answer) + "\n")
                else:
                    answer = unsorted_num ** 3
                    odd_file.write(str(answer) + "\n")
                
            print("successful")
    except FileNotFoundError:
            print("file not found")
        
            return
        
process_even_odd_numbers()