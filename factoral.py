# Created by Dylan Melo
# Created on January 2022
# This program gets the user to enter a integer
# and will display the factorized number.


def main():
    # initializations
    loop_counter = 0
    factorial_answer = 1

    # get the user number
    user_number = int(input("Enter a positive number: "))
    print("")

    # replicates a do. .while loop
    # calculate the factorial of the user number using a loop
    while True:
        loop_counter = loop_counter + 1
        factorial_answer = factorial_answer * loop_counter
        print("Tracking {} time(s) through loop.". format
        (loop_counter))
        if loop_counter >= user_number:
            break
    print("")
    print("{}! = {}".format(user_number, factorial_answer))


if __name__ == "__main__":
    main()
