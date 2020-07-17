def even_or_odd():
   number_to_choose = int(input('enter a number'))
   if (number_to_choose % 2) == 0:
      print((number_to_choose), 'is Even')
   else:
      print((number_to_choose), 'is Odd')

def main():
   even_or_odd()

if __name__ == '__main__':
   main()
