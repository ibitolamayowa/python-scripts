#! python3
# Program to detect the validity of a Nigerian Phone Number

def PhoneNumber(text):
    if len(text) == 11:
        print("Correct Number")

    elif len(text) == 14:
        if not text.startswith('+234'):
            print("Incorrect Phone Number")

        else:
            print("Correct Number")

    else:
        print("Invalid Number")


while True:
    text = str(input("Insert phone number: "))
    PhoneNumber(text)
    if len(text) != 14 and len(text) != 11:
        continue
    else:
        break
