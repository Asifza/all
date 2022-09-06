class Bank:
    def __init__(self, customer, account_no, Balance):
        self.customer = customer
        self.account_no = account_no
        self.Balance = Balance
    def withdraw(self, withdrew):
        self.withdrew = withdrew
        if self.withdrew>self.Balance:
            print(" Enter a Valid Amount, you dont have enough Balance")
        else:
            self.Balance = self.Balance - self.withdrew
            print(f"You have withdrawn {self.withdrew} Rs! Your Account Balance is {self.Balance}")
    def deposit(self, Depost):
        self.Depost = Depost
        self.Balance = self.Balance + self.Depost
        print(f"You have Depositted {self.Depost} Rs! Your Account Balance is {self.Balance}")
#cust_Balances = {1234:{"Sadik": 5000}, 9876:{"Kashif": 1000}, 5678:{"Shadab": 3000}}
#cust_name = input("Enter your Name: ")
#cust_account_no = int(input("Enter your Account No: "))
cust1 = Bank("Owais", 123456789, 100)
print(f"Welcome {cust1.customer}\n Your Account No is {cust1.account_no} \n Your Account Balance is {cust1.Balance} Rs")
option1 =int(input("What would you like to do today\n for Deposit press 1 \n for Withdrawal press 2\n for nothing press any key\n"))
if option1==1:
    Depost = int(input("Enter the amount you want to Deposit: "))
    cust1.deposit(Depost)

elif option1==2:
    withdrew = int(input("Enter the amount you want to Withdraw: "))
    cust1.withdraw(withdrew)
else:
    exit