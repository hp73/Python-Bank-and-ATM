"""
Author: Justin Park and Harry Pinkerton
File: bankserver.py
Project 12

Server for a bank.  Handles multiple clients
concurrently.
"""

from socket import *
from threading import Thread
from codecs import decode

BUFSIZE = 1024
CODE = 'ascii'

class ClientHandler(Thread):
    """Represents a client handler for a client session."""
    
    def __init__(self, client, bank, myView):
        Thread.__init__(self)
        self.client = client
        self.bank = bank
        self.account = None
        self.myView = myView

    def run(self):
        self.client.send(bytes("Connected to server", CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE), CODE)
            if not message:
                self.myView.updateStatus('Client disconnected')
                self.client.close()
                break
            else:
                self.client.send(bytes(self.reply(message), CODE))

    def reply(self, message):
        """Parses the message into a commmand and its arguments
        and dispatches them to the appropriate method."""
        [command, argument] = message.split("\n")
        if command == "deposit":
            return self.deposit(argument)
        elif command == "withdraw":
            return self.withdraw(argument)
        elif command == "balance":
            return self.getBalance()
        elif command == "logout":
            return self.logout()
        else:
            return self.login(command, argument)


    def deposit(self, amount):
        """Deposits amount and returns success or error message."""
        message = self.account.deposit(float(amount))
        if message:
            return message
        else:
            self.myView.displayAccount()
            return "success"

    def withdraw(self, amount):
        """Withdraws amount and returns success or error message."""
        message = self.account.withdraw(float(amount))
        if message:
            return message
        else:
            self.myView.displayAccount()
            return "success"
        
    def getBalance(self):
        """Returns the balance as a string."""
        return str(self.account.getBalance())

    def logout(self):
        """Returns the balance as a string."""
        self.account = None
        return "Welcome to the bank!"
   
    def login(self, name, pin):
        """Attempts to login and returns success or failure"""
        self.account = self.bank.get(name, pin)
        if self.account:
            return "success"
        else:
            return "faliure"
       
class BankServer(Thread):
    """Represents a server to handle multiple clients."""

    def __init__(self, host, port, bank, myView):
        """Sets the initial state of the server."""
        Thread.__init__(self)
        self.address = (host, port)
        self.bank = bank
        self.myView = myView
        self.isRunning = True

    def run(self):
        """Opens the server's socket, waits for connections
        from clients, and serves them."""
        try:
            self.server = socket(AF_INET, SOCK_STREAM)
            self.server.bind(self.address)
            self.server.listen(5)           # Allows up to 5 waiting clients

            while True:
                self.myView.updateStatus('Waiting for connection ...')
                client, address = self.server.accept()
                self.myView.updateStatus('... connected from ' + str(address))
                handler = ClientHandler(client, self.bank, self.myView)
                handler.start()

        except Exception as message:
            self.myView.updateStatus(message)
        self.server.close()
        self.myView.updateStatus("Server shutting down.")
