"""
Author: Justin Park and Harry Pinkerton
File: atm.py
Project 11

This module defines the ATM class, which provides a window
for bank customers to perform deposits, withdrawals, and check
balances.
"""

from breezypythongui import EasyFrame
from bank import SavingsAccount, Bank, createBank

class ATM(EasyFrame):
    """Represents an ATM window."""

    COLOR = "#CCEEFF"

    # The window tracks the bank and the current account
    # The current account is None at startup and logout

    def __init__(self, bank):
        """Initialize the frame and establish the data model."""
        EasyFrame.__init__(self, title = "ATM", background = ATM.COLOR)
        self.bank = bank
        self.account = None
        self.create_widgets()

    def create_widgets(self):
        """Create and add the widgets to the frame."""
        self.nameLabel = self.addLabel(row = 0, column = 0,
                                       text = "Name")
        self.pinLabel = self.addLabel(row = 1, column = 0,
                                      text = "Pin")
        self.amountLabel = self.addLabel(row = 2, column = 0,
                                         text = "Amount")
        self.statusLabel = self.addLabel(row = 3, column = 0,
                                         text = "Status")
        self.nameField = self.addTextField(row = 0, column = 1,
                                           text = "")
        self.pinField = self.addTextField(row = 1, column = 1,
                                          text = "")
        self.amountField = self.addFloatField(row = 2, column = 1,
                                              value = 0.0)
        self.statusField = self.addTextField(row = 3, column = 1,
                                             text = "Welcome to the Bank!")
        self.balanceButton = self.addButton(row = 0, column = 2,
                                            text = "Balance",
                                            command = self.getBalance,
                                            state = "disabled")
        self.depositButton = self.addButton(row = 1, column = 2,
                                            text = "Deposit",
                                            command = self.deposit,
                                            state = "disabled")
        self.withdrawButton = self.addButton(row = 2, column = 2,
                                             text = "Withdraw",
                                             command = self.withdraw,
                                             state = "disabled")
        self.loginButton = self.addButton(row = 3, column = 2,
                                          text = "Login",
                                          command = self.login)
        self.nameLabel["background"] = ATM.COLOR
        self.pinLabel["background"] = ATM.COLOR
        self.amountLabel["background"] = ATM.COLOR
        self.statusLabel["background"] = ATM.COLOR
 
    def login(self):
        """Attempts to login the customer.  If successful,
        enables the buttons, including logout."""
        name = self.nameField.getText()
        pin = self.pinField.getText()
        self.account = self.bank.get(name, pin)
        if self.account:
            self.statusField.setText("Hello, " + name + "!")
            self.balanceButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.loginButton["text"] = "logout"
            self.loginButton["command"] = self.logout
        else:
            self.statusField.setText("Name and pin not found!")
            
    def logout(self):
        """Logs the cusomer out, clears the fields, disables the
        buttons, and enables login."""
        self.account = None
        self.nameField.setText("")
        self.pinField.setText("")
        self.amountField.setNumber(0.0)
        self.statusField.setText("Welcome to the Bank!")
        self.balanceButton["state"] = "disabled"
        self.depositButton["state"] = "disabled"
        self.withdrawButton["state"] = "disabled"
        self.loginButton["text"] = "login"
        self.loginButton["command"] = self.login

    def getBalance(self):
        """Displays the current balance in the status field."""
        balance = self.account.getBalance()
        self.statusField.setText("Balance: $" + str(balance))

    def deposit(self):
        """Attempts a deposit. If not successful, displays
        error message in statusfield; otherwise, announces
        success."""
        amount = self.amountField.getNumber()
        message = self.account.deposit(amount)
        if message:
            self.statusField.setText(message)
        else:
            self.statusField.setText("Deposit successful!")
        
    def withdraw(self):
        """Attempts a withdrawal. If not successful, displays
        error message in statusfield; otherwise, announces
        success."""
        amount = self.amountField.getNumber()
        message = self.account.withdraw(amount)
        if message:
            self.statusField.setText(message)
        else:
            self.statusField.setText("Withdrawal successful!")
        
def main(fileName = "bank.dat"):
    """Creates the bank with the optional file name,
    wraps the window around it, and opens the window.
    Saves the bank when the window closes."""
    if not fileName:
        bank = createBank(5)
    else:
        bank = Bank(fileName)
    print(bank)
    atm = ATM(bank)
    atm.mainloop()

if __name__ == "__main__":
    main()
