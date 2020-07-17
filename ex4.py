my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

def print_all_numbers_less_then_chosen_number():
    number_chosen = int(input('enter a number'))
    for number in my_list:
        if number < number_chosen:
            new_list.append(number)
    print(new_list)

def main():
    print_all_numbers_less_then_chosen_number()

if __name__ == '__main__':
    main()
