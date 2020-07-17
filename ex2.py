def calculate_the_amount_of_years_till_100(y, z):
    return y-z+100

def enter_information():
    name = input('Enter your name:')
    year = int(input('what year it is?'))
    years_old = int(input('how old are u?'))

def print():
    print('you will be 100 years old at', calculate_the_amount_of_years_till_100())

def main():
    enter_information()
    calculate_the_amount_of_years_till_100(year, years_old)
    print()

if __name__ == '__main__':
    main()
