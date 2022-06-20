# Copy: 1234567890123456
print("Hello, I am an employee of a Belarusian bank. Enter your card to encrypt it.\n"
      "--------------------------------------------------------------------------- ")


def Belarusian_bank(card):
    return '*' * len(card[:-4]) + card[-4:]


Credit_digits = input("Enter your credit card (16 digits):")
if len(Credit_digits) == 16:
    print(Belarusian_bank(Credit_digits))
    print("Thanks for the operation!")
else:
    print("Error! Incorrect value!")