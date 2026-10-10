# Class and Object

class Atm:  # class name (pascal case: MyWorld)
    # constructor (special function)
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()     # function calling

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            # create pin
            self.create_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw()
        else:
            exit()

    def create_pin(self):       # function for pin generation
        user_pin = input('enter your pin:')
        self.pin = user_pin

        user_balance = int(input('enter balance:'))
        self.balance = user_balance

        print('PIN CREATED SUCCESSFULLY')
        self.menu()

    def change_pin(self):       # function for changing pin
        old_pin = input('enter old pin:')

        if old_pin == self.pin:
            # let the person change the pin
            new_pin = input('enter new pin:')
            self.pin = new_pin
            print('PIN CHANGE SUCCESSFUL')
            self.menu()
        else:
            print("can't change the pin")
            self.menu()

    def check_balance(self):        # function for checking balance
        user_pin = input('enter your pin:')
        if user_pin == self.pin:
            print('your balance is', self.balance)
            self.menu()
        else:
            print("can't show the balance")
            self.menu()

    def withdraw(self):         # function for withdrawing money
        user_pin = input('enter your pin:')
        if user_pin == self.pin:
            # ask for withdrawal amount and also show the balance left
            withdrawal_amount = int(input('enter the withdrawal amount:'))
            if withdrawal_amount <= self.balance:
                self.balance = self.balance - withdrawal_amount
                print(withdrawal_amount, 'withdrawn successful')
                print('balance left in the account:', self.balance)
            else:
                print('not enough balance')
        else:
            print("can't withdraw money")
        self.menu()

obj = Atm()     # objectname = classname()

# constructor is executed as we create the object of the class

print(type(obj))    # <class '__main__.Atm'>

# obj.pin   # object can access the things that are present in class