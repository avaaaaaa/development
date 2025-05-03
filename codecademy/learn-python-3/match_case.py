# match-case statement is introduced in python 3.10
# match-case is actually if-elif-else but only used for checking equality
# so we cannot implement > or < logic with match-case, only ==
# it is possible to say using match-case might make your program easier
#   to understand since it is specialized version of if statements and
#   when we see it, we know we will be checking only for equality.

exit_loop = False
get_number = ""

while not exit_loop:
    get_number = input("enter a number: ")
    if get_number.isdigit():
        exit_loop = True
        get_number = int(get_number)

if get_number == 1:
    print("1")
elif get_number == 2:
    print("2")
elif get_number == 3:
    print("3")
else:
    print("4")

match get_number:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case default:
        print("4")