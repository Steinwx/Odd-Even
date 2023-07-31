def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def main():
    input_file = "numbers.txt"
    even_output_file = "even.txt"
    odd_output_file = "odd.txt"

    numbers = read_numbers_from_file(input_file)

    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    write_numbers_to_file(even_numbers, even_output_file)
    write_numbers_to_file(odd_numbers, odd_output_file)

if __name__ == "__main__":
    main()

