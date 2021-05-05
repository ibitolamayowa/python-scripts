#! python3
# Program to detect the validity of a Nigerian Phone Number

def phonenumber(text):
    if len(text) == 11:
        print("This is a correct Number")

    elif len(text) == 14:
        if not text.startswith('+234'):
            print("This is an incorrect Phone Number")

        else:
            print("Correct Number")

    else:
        print("Invalid Number")


while True:
    text = str(input("Insert the phone number: "))
    phonenumber(text)
    if len(text) != 14 and len(text) != 11:
        continue
    else:
        break
