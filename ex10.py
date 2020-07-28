import random
import string

def get_random_pass(length):
    letters_and_digits = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters_and_digits) for i in range(length))
    print("The password is", password)

def main():
    get_random_pass(8)

if __name__ == '__main__':
    main()
