def name_and_years_information():
    name = input('Enter your name:')
    year = int(input('what year it is?'))
    years_old = int(input('how old are u?'))
    return year, years_old


def calculate_the_amount_of_years_till_100(year, years_old):
    return year-years_old+100

def the_result(output):
    print('you will be 100 years old at', output)

def main():
    year, years_old  = name_and_years_information()
    output = calculate_the_amount_of_years_till_100(year, years_old)
    the_result(output)

if __name__ == '__main__':
    main()
