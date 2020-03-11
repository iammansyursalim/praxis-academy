class ATMmachine():
    def checkBalance(self):
        print('your current balance is '+BalanceInquiry.getBalanceInquiry())

    def withdrawmoney(self):
        if(BalanceInquiry.getBalanceInquiry == 0):
            print('your current balance is zero')
            print('cannot draw')
            print('deposit money first')
        elif(BalanceInquiry.getBalanceInquiry<=500):
            print("You do not have sufficient money to withdraw")
            print("Checked your balance to see your money in the bank.")
        elif(Withdraw.getwithdraw > BalanceInquiry.getBalanceInquiry):
            print("The amount you withdraw is greater than to your balance")
            print("Please check the amount you entered.")
        else:
            BalanceInquiry.getBalanceInquiry = BalanceInquiry.getBalanceInquiry - Withdraw.getwithdraw
            print("You withdraw the amount of Php " + Withdraw.getwithdraw)

    def depositmoney(self):
        print("\tYou deposited the amount of " + Deposit.getdeposit());

    def main(self):
        print("SELAMAT DATANG DI ATM BANK BAGOOD")
        print("1.Deposit")
        print("2.withdar")
        print('3. balance inquiry')
        opt = int(input("Silahkan pilih menu : "))
        if opt == 1:
            print("")
            print("masukkan jumlah uang untuk deposit")
            Deposit.setdeposit = Deposit.getdeposit()
            BalanceInquiry.getBalanceInquiry = Deposit.setdeposit + BalanceInquiry.getBalanceInquiry
            Deposit.depositmoney()
            breakpoint()

        if opt == 2:
            print("\n\tTo withdraw, make sure that you have sufficient balance in your account.")
            print()
            print("\tEnter amount of money to withdraw: ")
            Withdraw.setwithdraw = Withdraw.getwithdraw()
            Withdraw()
            breakpoint()

        if opt == 3:
            checkBalance()
            breakpoint()

class Withdraw(ATMmachine):
    def setwitdraw(self):
        withdraw = 0

    def getwithdraw(self,withdraw=0):
        return withdraw

class BalanceInquiry(ATMmachine):
    def setBalanceInqury(self):
        balanceinquiry = 0

    def getBalanceInquiry(self,balanceinquiry=0):
        return balanceinquiry

class Deposit(ATMmachine, BalanceInquiry, Withdraw):
    def setdeposit(self, deposit = 0):
        return deposit

    def getdeposit(self, deposit=0):
        return deposit

