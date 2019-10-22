
class account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return "Account owner: {}\nAccount balance: ${}".format(self.name,self.balance)

    def owner(self):
        print(self.name)

    def balance(self):
        print(self.balance)

    def deposite(self,amount):
        self.balance = self.balance + amount
        print("DEPOSITE ACCEPTED!!")
        return self.balance

    def withdraw(self,amount):
        if (amount > self.balance):
            print("Funds Unavailable")
        else :
            self.balance -= amount
            print('Withdrawal Accepted!')



acct1 = account('Jose',100)
print(acct1)
acct1.owner()
#acct1.balance() still has problem TypeError: 'int' object is not callable
acct1.deposite(50)
acct1.withdraw(75)
acct1.withdraw(500)
