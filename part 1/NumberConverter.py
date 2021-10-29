#############################################
#	COMPSCI 105 S2 C, 2018              #
#	Assignment 2 Question 2             #
#                                           #
#	@author  	Xiaolin Li (xli556) #
#	@version	04/10/2018          #
#############################################

def display_intro():
    message = "*"*2 + " "*8 + "A Number Converter Program" + " "*8+ "*"*2 +"\n"+\
              "*"*2 + " Decimal --> Binary, Octal or Hexadecimal " + "*"*2 
    print(message)

def converter(number,base):
    if number <= 0:
        return ""
    else:
        #situation when base is 16 (hex) with a = 10, b = 11, c = 12, d = 13, e = 14, and f = 15.
        if base == 16:
            x = number % 16
            digits_str = "0123456789abcdef"
            the_other_part = number//16
            if the_other_part == 0:
                return digits_str[x]
            else:
                return converter(the_other_part, 16) + digits_str[x]
        elif base == 2 or base == 8:
            return converter(number//base, base) + str(number % base)
    #YOUR IMPLEMENT

def display_separator():
    lines = "*" * 46
    print(lines)

def display_menu():
    print("1. Convert to binary value")
    print("2. Convert to octal value")
    print("3. Convert to hexadecimal value")
    print("4. Quit the program")

def get_option(start,end):
    user_option = input("Please make a selection: ")
    while not user_option.isnumeric() or int(user_option) < start or int(user_option) > end:
        user_option = input("Invalid selection. Try again: ")
    return int(user_option)

def get_num():
    user_option = input("Please enter a positive integer: ")
    while not user_option.isnumeric() or int(user_option) <= 0:
        user_option = input("Invalid entry. Try again: ")
    return int(user_option)

def main():
    display_separator()
    display_intro()
    display_separator()
    display_menu()
    option = get_option(1,4)
    while option != 4:
        dec_num = get_num()
        if option == 1:
            bin_number = converter(dec_num,2)
            print(dec_num,"is",bin_number,"in binary")
        if option == 2:
            oct_number = converter(dec_num,8)
            print(dec_num,"is",oct_number,"in octal")
        if option == 3:
            hexa_number = converter(dec_num,16)
            print(dec_num,"is",hexa_number,"in hexadecimal")
        display_menu()
        option = get_option(1,4)
        
main()
