def name_and_years_information():
    name = input('Enter your name:')
    year = int(input('what year it is?'))
    years_old = int(input('how old are u?'))

def calculate_the_amount_of_years_till_100(year, years_old):
    return year-years_old+100

def the_result():
    print('you will be 100 years old at',calculate_the_amount_of_years_till_100(year, years_old))

def main():
    name_and_years_information()
    calculate_the_amount_of_years_till_100(year, years_old)
    the_result()

if __name__ == '__main__':
    main()
