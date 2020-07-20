list_of_divisors=[]

def chosen_number():
    number_to_choose = int(input('please enter a number'))
    return number_to_choose

def divisor(chosen):
    for divisors in range(1, chosen + 1):
        if chosen % divisors == 0:
            list_of_divisors.append(divisors)

def result():
    print(list_of_divisors)

def main():
    chosen = chosen_number()
    divisor(chosen)
    result()


if __name__ == '__main__':
    main()