import AccountNumberGenerator

class Account():

    # global accountName
    # global accountType
    # global balance
    # global accountNumber

    def __init__(self, accountName, accountType, balance=0):
        self.accountName = accountName
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = AccountNumberGenerator.generateAccountNumber(11)
        print("{} account have been created successfully\n AccountNumber :: {}".format(self.accountType, self.accountNumber))

    def withDraw(self, withDrawAmount):
        self.balance = self.balance - withDrawAmount
        print ("Available balance in the account is ${}".format(self.balance))

    def deposit(self, depositAmount):
        self.balance = self.balance + depositAmount
        print ("Available balance in the account is ${}".format(self.balance))

    def __repr__(self):
        return "Account for {} has been created successfully with initial deposit {}".format()

if __name__ == "__main__":

    def accountTypeSelection(num):
        accountType = {"1":"Saving", "2":"Checking"}
        if num == 1:
            return accountType.get(num)
        else:
            return accountType.get(num)


    def selectionExecutor(options):
        if options == 1:
            try:
                accountHolderName = str(input("Enter Account holder Full Name::"))
                accountType = input("Select the Type of account\n1. Saving\n2. Checking")
                balance = float(input("Enter the initial balance"))
                newAccount = Account(accountHolderName, accountTypeSelection(accountType), balance)
            except NameError:
                print("Error in conversion")


    print("*********************Welcome Demo Banking System*********************")
    print("Please select the options below\n1. Create new Account\n2. Check Balance\n3. Deposit Amount\n4. WithDrawl ")

    options = input("Select the options:: ")
    selectionExecutor(options)