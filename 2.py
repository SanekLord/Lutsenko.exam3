def PolText(word):
    word_back = word[::-1]
    if word.isdigit():
        print("Error! You entered digits!")
    elif len(word.split()) == 1 and word.isalpha():
        if word == word_back:
            print("* Is the word a palindrome. *")
        else:
            print("* This word is not a palindrome. *")
    elif len(word.split()) > 1:
        print(f"Error! You entered {len(inp_word.split())} words!")
    elif not word.isalpha():
        print("Error! You entered an invalid value!")


print("Hello write the word and I will tell you if it is a palindrome.\n"
      "---------------------------------------------------------------")
while True:
    inp_word = input("Enter the word:")
    PolText(inp_word)
    if inp_word == "n":
        print("Program off!")
        break