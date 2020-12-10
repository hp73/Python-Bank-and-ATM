Project 11,12 - Python Bank and ATM
CSCI 101 Fall 2019
By Harry Pinkerton and Justin Park
Required to run: python 3.7


===bankmanager.py===
When run, displays a bankmanager GUI where the user is able to access all members of the bank. By default, data for the bank is stored in bank.dat. 

--Variables--
bank: Bank object that the ATM class accesses from bank.py
position: position in the queue for accounts
name: the name of the owner of the account
pin: the unique 4 digit number that every individual in the bank has to differentiate individuals with the same name
balance: the amount of money an account currently has
interest: calculated percentage interest based on a default rate
nameLabel: where "name" is displayed on the GUI
pinLabel: where "pin" is displayed on the GUI
balanceLabel: where "balance" is displayed on the GUI
statusLabel: where "status" is displayed on the GUI
nameField: where the specified user's name is displayed
pinField: where the specified pin is displayed
balanceField: where the specified blanace is displayed
hostField: where the host ip for the bank is displayed
statusField: where the specified status is displayed
newButton: the button that is linked with the newAccount method
updateButton: the button that is linked with the updateAccount method
removeButton: the button that is linked with the removeAccount method
interestButton: the button that is linked with the computeInterest method
previousButton: the button that is linked with the previousAccount method
nextButton: the button that is linked with the nextAccount method
saveButton: the button that is linked with the saveBank method
serverButton: the button that is linked with the startServer method
findAccount: the button that is linked with the findAccount method
keys: list of keys from a given bank object

--Methods--
create_widgets(): displays all of the widgets on the GUI to be interacted with
displayAccount(): displays a given account to the GUI and disables certain unecessary buttons
newAccount(): generates a new account to be stored in the bank
updateAccount(): updates someone's name, pin, balance, or posiion in the bank
removeAccount(): deletes a user's information from the bank and updates every other person's position in the queue
computeInterest(): calculates the interest of a user given their current balance
previousAccount(): moves the position of the queue back one position
nextAccount(): moves the position of the queue forward one position
saveBank(): Saves the current bank information
findAccount(): finds a user's account in the queue given a name and pin number 
updateStatus(): Displays message in status field.
startServer(): Starts up the bank server at default localhost and port 50000


===atm.py===
When run, displays an atm GUI where the user is able to access the bank given a name and pin number. BankManager must be running and the server connection
established before this program may run.

--Variables--
bank: Bank object that the ATM class accesses from bank.py
account: a unique name and pin combination that is associated with an individuals' balance
name: the name of the owner of the account
pin: the unique 4 digit number that every individual in the bank has to differentiate individuals with the same name
balance: the amount of money an account currently has
amount: amount of money being deposited or withdrawn from an account
message: message displayed in the "Status" section of the GUI given an action
nameLabel: where "name" is displayed on the GUI
pinLabel: where "pin" is displayed on the GUI
amountLabel: where "amount" is displayed on the GUI
statusLabel: where "status" is displayed on the GUI
nameField: where the user inputs their name to login
pinField: where the user inputs their pin to login
amountField: where the user inputs the amount they wish to deposit or withdraw from their account
statusField: where the atm client displays the status of the account given a user action
balanceButton: where the user clicks to check the balance of their account
depositButton: where the user clicks to desposit a specified amount into their account
withdrawButton: where the user clicks to withdraw a specified amount into their account
loginButton: where the user clicks after inputting their name and pin number into the respective fields to login

--Methods--
create_widgets(): displays all of the widgets on the GUI to be interacted with
login(): checks to see if there is a valid pin and name combination in the bank data and greets the user upon entry
logout(): clears all fields and enables a new login from a new user
getBalance(): retrieves the balance from a unqiue account
deposit(): inserts a specified amount into a unique account 
withdraw(): withdraws a specified amount from a unique account given the account has as much as or more than the amount specified


===bank.py===
Returns all of the SavingsAccounts from a specified file to the command line  

--Classes--
SavingsAccount: SavingsAccount class that stores a user's name, pin, and balance
Bank:  Bank class that represents a bank as a collection of savinings accounts 

--Variables--
name: the name of the owner of the account
pin: the pin of the owner of the account
balance: the amount of money an account currently has
amount: amount of money being deposited or withdrawn from an account
interest: calculated percentage interest based on a default rate
fileName: name of file where bank information is stored
accounts: list of SavingsAccount objects 
fileObj: file object to be loaded given a fileName
key: unqique identifier for an account
keylist: list of all keys for all SavingsAccounts
names: List of default names if a new, random bank is to be generated
bank: bank object where SavingsAccounts are stored

--Methods--
getBalance(): returns the balance of a specified account
getName(): returns the name of a specified account
getPin(): returns the pin of a specified account
deposit(): deposits a set amount of money into a unqiue account
withdraw(): withdraws a set amount of money from a unique account given the account has a high enough balance
makeKey(): returns a key for the account
add(): Adds the account to the bank
remove(): removes the account from the bank and and returns it, or None if the account does not exist.
get(): returns the account from the bank, or returns None if the account does not exist.
computeInterest(): computes and returns the interest on all accounts.
getKeys(): Returns a sorted list of keys
save(): Saves picked accounts to a file. The parameter allows the user to change file names


===atmClient.py===
Represents the client for a bank ATM.  Behaves like a Bank with the get method and an account with the getBalance, deposit, and withdraw
methods. By default, runs on localhost, but has the functionality to work across different ip addresses and ports.

--Variables--
address: host and port number
server: establishes a server for the atm to run on given a host ip and port number
message: message to be decoded from the GUI to the server

--Methods--
getBalance(): returns the balance of a specified account
deposit(): deposits amount and returns None if successful, or an error message if not
withdraw(): Withdraws amount and returns None if successful, or an error message if not.
get(): returns the client's account if it exists, or None if not


===bankserver.py===
Represents the client for a bank ATM.  Behaves like a Bank with the get method and an account with the getBalance, deposit, and withdraw
methods. By default, runs on localhost, but has the functionality to work across different ip addresses and ports.

--Variables--
client: current bank manager client
account: a unique name and pin combination that is associated with an individuals' balance
myView: text based updates based on the connection of the server
message: message to be decoded from the GUI to the server
bank: specified bank where SavingsAccount data will be pulled

--Methods--
run(): opens the server's socket, waits for connections from clients, and serves them.
reply(): parses the message into a commmand and its arguments and dispatches them to the appropriate method.
deposit(): deposits amount and returns success or error message
withdraw(): withdraws amount and returns success or error message
getBalance(): returns the balance as a string.
logout(): clears the current account from being displayed on the GUI
login(): attempts to login and returns success or failure


