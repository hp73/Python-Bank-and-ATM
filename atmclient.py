"""
Author: Justin Park and Harry Pinkerton
File: atmclient.py
Project 12

Client for the ATM. Behaves like a Bank with the get method
or a SavingsAccount with the getBalance, deposit, and withdraw methods.
"""

from socket import *
from codecs import decode

BUFSIZE = 1024
CODE = "ascii"

class ATMClient(object):
    """Represents the client for a bank ATM.  Behaves like a Bank with the
    get method and an account with the getBalance, deposit, and withdraw
    methods."""

    def __init__(self, host, port):
        """Initialize the client."""
        address = (host, port)
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.connect(address)                         
        message = decode(self.server.recv(BUFSIZE), CODE)

    def get(self, name, pin):
        """Returns the client's account if it exists, or None if not."""
        self.server.send(bytes(name + "\n" + pin, CODE))
        message = decode(self.server.recv(BUFSIZE), CODE)
        if message == "success":
            return self
        else:
            return None

    def getBalance(self):
        """Returns the balance of the account."""
        self.server.send(bytes("balance\n" + "nada", CODE))
        message = decode(self.server.recv(BUFSIZE), CODE)
        return float(message)                        

    def deposit(self, amount):
        """Deposits amount and returns None if successful,
        or an error message if not."""
        self.server.send(bytes("deposit\n" + str(amount), CODE))
        message = decode(self.server.recv(BUFSIZE), CODE)
        if message == "success": return None
        else: return message

    def withdraw(self, amount):
        """Withdraws amount and returns None if successful,
        or an error message if not."""
        self.server.send(bytes("withdraw\n" + str(amount), CODE))
        message = decode(self.server.recv(BUFSIZE), CODE)
        if message == "success": return None
        else: return message
