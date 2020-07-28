def chosen_word():
    word = input("Please enter a word")
    word = str(word)
    return word

def reverse_word(word):
    reverse = word[::-1]
    return reverse

def output_reversed_word(reverse):
    print(reverse)

def output(word, reverse):
    if word == reverse:
        print("This word is a palindrome")
    else:
        print("This word is not a palindrome")

def main():
    word = chosen_word()
    reverse = reverse_word(word)
    output_reversed_word(reverse)
    output(word, reverse)



if __name__ == '__main__':
    main()
