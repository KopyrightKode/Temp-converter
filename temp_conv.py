#Temperature converter written by KopyrightKid
# C = (F - 32) * 5/9
# F = (C * 1.8) + 32
#
#
def temp_converted():

    f_or_c = input("Is the number you want to convert in Farenheit (f) or Celsius (c)? ")
    if f_or_c == "f":
        num = input("Enter your number in Farenheit: ")
        int_num = int(num)
        c_num = (int_num - 32) * (5/9)
        print("Your Temperature in celsius is: " + str(c_num))
    elif f_or_c == "c":
        num = input("Enter your number in Celsius: ")
        int_num = int(num)
        f_num = (int_num * 1.8) + 32
        print("Your Temperature in Farenheit is: " + str(f_num))
    else:
        print("You fucked up gooby")
temp_converted()
