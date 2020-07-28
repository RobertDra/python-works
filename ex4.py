my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

def chosen_number():
    number_chosen = int(input('enter a number'))
    return number_chosen

def check_in_list(less_than_the_number):
    for number in my_list:
        if number < less_than_the_number:
            new_list.append(number)

def output_message():
    print(new_list)

def main():
    less_than_the_number = chosen_number()
    check_in_list(less_than_the_number)
    output_message()

if __name__ == '__main__':
    main()
