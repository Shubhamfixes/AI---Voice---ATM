import pyttsx3
import time
from colorama import Fore, Style, init

init(autoreset=True)

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def loading_system():

    print(Fore.GREEN + "\n[ INITIALIZING SECURE BANKING SYSTEM ]")
    time.sleep(1)

    print(Fore.YELLOW + "[ CONNECTING TO BANK SERVER... ]")
    time.sleep(1)

    print(Fore.CYAN + "[ VERIFYING USER IDENTITY... ]")
    time.sleep(1)

    print(Fore.GREEN + "[ ACCESS GRANTED ]\n")
    time.sleep(1)


PIN = 1980
attempts = 3
BALANCE = 12000
history = []
name = "Shubham"


loading_system()

speak(f"Welcome Boss {name}")
speak("Secure ATM system activated")


while attempts > 0:

    try:

        user = int(input(Fore.CYAN + "Enter Your Secure PIN: "))

    except ValueError:

        speak("Invalid PIN format")
        continue


    if user == PIN:

        speak("Identity verified successfully")

        while True:

            print(Fore.MAGENTA + """

**********************************************************************

                    SECURE ATM SYSTEM

                1. CHECK BALANCE

                2. CASH DEPOSIT

                3. CASH WITHDRAW

                4. TRANSACTION HISTORY

                5. CHANGE PIN

                q. QUIT SYSTEM

**********************************************************************

""")

            speak("Select an operation")

            Action = input(Fore.YELLOW + "Select Option: ")


            if Action == "1":

                print(Fore.GREEN + f"\nCurrent Balance: {BALANCE} USD\n")
                speak(f"Your current balance is {BALANCE} dollars")


            elif Action == "2":

                try:

                    amount = int(input("Enter amount to deposit: "))

                    if amount <= 0:
                        speak("Invalid amount")
                        continue

                    BALANCE += amount

                    history.append(f"Deposited {amount} USD")

                    print(Fore.GREEN + "\nTransaction Successful\n")

                    speak(f"{amount} dollars deposited successfully")
                    speak(f"Updated balance is {BALANCE} dollars")

                except ValueError:

                    speak("Please enter numbers only")


            elif Action == "3":

                try:

                    amount = int(input("Enter amount to withdraw: "))

                    if amount <= 0:
                        speak("Invalid amount")
                        continue

                    if BALANCE - amount < 0:

                        print(Fore.RED + "\nInsufficient Balance\n")
                        speak("Insufficient balance")
                        continue

                    BALANCE -= amount

                    history.append(f"Withdrawn {amount} USD")

                    print(Fore.GREEN + "\nTransaction Successful\n")

                    speak(f"{amount} dollars withdrawn successfully")
                    speak(f"Remaining balance is {BALANCE} dollars")

                except ValueError:

                    speak("Please enter valid numbers")


            elif Action == "4":

                print(Fore.CYAN + "\n===== TRANSACTION HISTORY =====\n")

                if len(history) == 0:

                    print("No transactions available")

                else:

                    for i in history:
                        print(i)

                print()


            elif Action == "5":

                try:

                    old_pin = int(input("Enter current PIN: "))

                    if old_pin == PIN:

                        new_pin = int(input("Enter new PIN: "))

                        PIN = new_pin

                        print(Fore.GREEN + "\nPIN Changed Successfully\n")

                        speak("PIN updated successfully")

                    else:

                        print(Fore.RED + "\nWrong Current PIN\n")

                        speak("Wrong current PIN")

                except ValueError:

                    speak("PIN must contain numbers only")


            elif Action == "q":

                print(Fore.GREEN + "\nThank You For Using Secure ATM System\n")

                speak("Thank you for using secure ATM system")
                break


            else:

                print(Fore.RED + "\nInvalid Operation\n")

                speak("Invalid operation selected")

        break


    else:

        attempts -= 1

        print(Fore.RED + "\nWrong PIN Detected\n")

        speak("Security alert. Wrong PIN detected")

        print(Fore.YELLOW + f"Attempts Left: {attempts}\n")

        if attempts == 0:

            print(Fore.RED + "\nATM LOCKED DUE TO MULTIPLE FAILED ATTEMPTS\n")

            speak("ATM locked due to multiple failed attempts")