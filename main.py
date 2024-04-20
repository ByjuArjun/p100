class ATM():
    def __init__(self, pin, cardnumber):
        self.pin=pin
        self.cardnumber=cardnumber 
    
    def show(self):
        print("Your Pin Is", self.pin)
        print("Your CardNumber Is", self.cardnumber)
    
    def CashWithdrawl(self):
        global amount
        amount=int(input("How Much Do You Want To Withdraw?"))
        print("You have Withdrawn $",amount)

    def BalanceEnquiry(self):
        global amount
        balance = 5000000
        total = balance-amount
        print(total)

p1=ATM(1087654321, "5346-6789-9912")
p1.show()
p1.CashWithdrawl()
p1.BalanceEnquiry()
