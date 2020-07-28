def input_the_sentence():
    sentence = input("Please enter a sentence")
    sentence = str(sentence)
    return sentence

def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

def output(rev):
    print(rev)

def main():
        sentence = input_the_sentence()
        rev = rev_sentence(sentence)
        output(rev)

if __name__ == "__main__":
    main()
