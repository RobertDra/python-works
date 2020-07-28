def get_number_from_user():
   number_to_choose = int(input('enter a number'))
   return number_to_choose

def even_or_odd(given_number):

   if (given_number % 2) == 0:
     return ('number is even')
   else:
     return ('number is odd')

def output_message(state):
  print(state)

def main():
   given_number = get_number_from_user()
   state = even_or_odd(given_number)
   output_message(state)

if __name__ == '__main__':
   main()
