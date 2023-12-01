from bankOOP import Bankkonto, Sparekonto, BSUKonto
from Account import Account

def bankType():
    print("1. Bankkonto")
    print("2. Sparekonto")
    print("3. BSUKonto")
    print("4. Exit")

def display_menu1():
    print("1. Add money")
    print("2. Take out money")
    print("3. Exit")

def main():
    print("-------------------Welcome to the Bank Of America---------------------------")

    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")

    account = Account(firstName, lastName)

    user_choice = 0

    while user_choice != 4:
        print("------------------User-----------------------")
        print(account.bankBruker())
        bankType()

        try:
            user_choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")

        if user_choice == 1:
            bankkonto = Bankkonto(0, firstName, lastName)  # Initialize saldo to 0

            while user_choice != 3:
                print("------------------Bankkonto Menu-----------------------")
                display_menu1()

                try:
                    user_choice = int(input("Enter your choice (1-3): "))
                except ValueError:
                    print("Invalid input. Please enter a number.")

                if user_choice == 1:
                    amount = int(input("Enter the amount to add: "))
                    bankkonto.settPenger(amount)
                elif user_choice == 2:
                    amount = int(input("Enter the amount to take out: "))
                    bankkonto.taUtPenger(amount)
                elif user_choice == 3:
                    print("Exiting Bankkonto Menu.")
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif user_choice == 2:
            print("Sparekonto menu not implemented yet.")
        elif user_choice == 3:
            print("BSUKonto menu not implemented yet.")
        elif user_choice == 4:
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
