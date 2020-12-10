"""
Author: Justin Park and Harry Pinkerton
File: bankmanager.py
Project 11

This module defines the BanManager class, which provides a window
for bank managers to maintain accounts.
"""

from breezypythongui import EasyFrame
from bank import SavingsAccount, Bank

class BankManager(EasyFrame):
    """Represents an ATM window."""

    COLOR = "#FFCCCC"

    # The window tracks the bank, the current account, and its
    # position is a sorted list of accounts (by key)
    # The current account and position are None if the bank is empty

    def __init__(self, bank):
        """Initialize the frame and establish the data model."""
        EasyFrame.__init__(self, title = "Bank Management",
                           background = BankManager.COLOR)
        self.bank = bank
        self.position = None
        self.create_widgets()
        self.displayAccount()

    def create_widgets(self):
        """Create and add the widgets to the frame."""
        self.nameLabel = self.addLabel(row = 0, column = 0,
                                       text = "Name")
        self.pinLabel = self.addLabel(row = 1, column = 0,
                                      text = "Pin")
        self.balanceLabel = self.addLabel(row = 2, column = 0,
                                          text = "Balance")
        self.statusLabel = self.addLabel(row = 3, column = 0,
                                         text = "Status")
        self.nameField = self.addTextField(row = 0, column = 1,
                                           text = "")
        self.pinField = self.addTextField(row = 1, column = 1,
                                          text = "")
        self.balanceField = self.addFloatField(row = 2, column = 1,
                                               value = 0.0)
        self.statusField = self.addTextField(row = 3, column = 1,
                                             text = "")
        self.newButton = self.addButton(row = 0, column = 2,
                                        text = "New account",
                                        command = self.newAccount)
        self.updateButton = self.addButton(row = 1, column = 2,
                                           text = "Update account",
                                           command = self.updateAccount)
        self.removeButton = self.addButton(row = 2, column = 2,
                                           text = "Remove account",
                                           command = self.removeAccount)
        self.interestButton = self.addButton(row = 3, column = 2,
                                             text = "Compute interest",
                                             command = self.computeInterest)
        self.previousButton = self.addButton(row = 4, column = 0,
                                             text = "Previous account",
                                             command = self.previousAccount)
        self.nextButton = self.addButton(row = 4, column = 1,
                                         text = "Next account",
                                         command = self.nextAccount)
        self.saveButton = self.addButton(row = 4, column = 2,
                                         text = "Save to file",
                                         command = self.saveBank)
        self.findaccount= self.addButton(row = 4, column =3,
                                         text = "Find account",
                                         command = self.findAccount)
        self.nameLabel["background"] = BankManager.COLOR
        self.pinLabel["background"] = BankManager.COLOR
        self.balanceLabel["background"] = BankManager.COLOR
        self.statusLabel["background"] = BankManager.COLOR


    def displayAccount(self):
        keys = self.bank.getKeys()
        if len(keys) == 0:
            self.nameField.setText("")
            self.pinField.setText("")
            self.balanceField.setNumber(0.0)
            self.statusField.setText("")
            self.updateButton["state"] = "disabled"
            self.removeButton["state"] = "disabled"
            self.interestButton["state"] = "disabled"
            self.previousButton["state"] = "disabled"
            self.nextButton["state"] = "disabled"
            return
        elif not self.position:   # For startup
            self.position = 0
        key = keys[self.position]
        [name, pin] = key.split("/")
        self.account = self.bank.get(name, pin)
        self.nameField.setText(self.account.getName())
        self.pinField.setText(self.account.getPin())
        self.balanceField.setNumber(self.account.getBalance())
        self.statusField.setText("")
        self.updateButton["state"] = "normal"
        self.removeButton["state"] = "normal"
        self.interestButton["state"] = "normal"
        if self.position == 0:
            self.previousButton["state"] = "disabled"
        else:
            self.previousButton["state"] = "normal"
        if self.position == len(keys) - 1:
            self.nextButton["state"] = "disabled"
        else:
            self.nextButton["state"] = "normal"
        
    def newAccount(self):
        name = self.nameField.getText()
        pin = self.pinField.getText()
        balance = self.balanceField.getNumber()
        newAccount = SavingsAccount(name, pin, balance)
        self.bank.add(newAccount)
        self.position = self.bank.getKeys().index(self.bank.makeKey(name, pin))
        self.displayAccount()
        self.statusField.setText("Account added.")

    def updateAccount(self):
        name = self.nameField.getText()
        pin = self.pinField.getText()
        balance = self.balanceField.getNumber()
        newAccount = SavingsAccount(name, pin, balance)
        self.bank.remove(self.account.getName(), self.account.getPin())
        self.bank.add(newAccount)
        self.position = self.bank.getKeys().index(self.bank.makeKey(name, pin))
        self.displayAccount()
        self.statusField.setText("Account updated.")

    def removeAccount(self):
        self.bank.remove(self.account.getName(), self.account.getPin())
        if self.position > 0:
            self.position -= 1
        self.displayAccount()
        self.statusField.setText("Account removed.")

    def computeInterest(self):
        interest = self.bank.computeInterest()
        self.statusField.setText("Total interest: $" + str(interest))

    def previousAccount(self):
        self.position -= 1
        self.displayAccount()

    def nextAccount(self):
        self.position += 1
        self.displayAccount()

    def saveBank(self):
        self.bank.save()
        self.statusField.setText("Bank saved.")

    def findAccount(self):
        nameinput=self.prompterBox(title = "Find Account", promptString = "Enter the name", inputText = "",
                    fieldWidth = 20)
        pinnumber=self.prompterBox(title = "Find Account", promptString = "Enter the pin", inputText = "",
                    fieldWidth = 20)
        indexkey = self.bank.get(nameinput, pinnumber)
        if indexkey:
            self.position = self.bank.getKeys().index(self.bank.makeKey(nameinput,pinnumber))
            self.displayAccount()
        else:
            self.statusField.setText("This account doesn't exist.")
            
        

         
def main(fileName = "bank.dat"):
    """Creates the bank with the optional file name,
    wraps the window around it, and opens the window.
    Saves the bank when the window closes."""
    bank = Bank(fileName)
    print(bank)
    manager = BankManager(bank)
    manager.mainloop()
    bank.save()

if __name__ == "__main__":
    main()
