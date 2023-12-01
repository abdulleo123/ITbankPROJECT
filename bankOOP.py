class Bankkonto:

    def __init__(self, saldo, fornavn, etternavn):
        self.saldo = saldo
        self.navn = fornavn
        self.etternavn = etternavn

    def settPenger(self, amount):
        self.saldo += amount
        print(f"You inserted this amount: {amount}")
        self.displayAccountInfo()
        return self.saldo

    def taUtPenger(self, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                print("Please enter a positive withdrawal amount.")
                print("---------------------------------------------")
                return self.saldo
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the withdrawal amount.")
            return self.saldo

        self.saldo -= amount
        if self.saldo < 0:
            print("You are in debt")
            print(f"Withdrawal failed. Current balance: {self.saldo + amount}")
        else:
            print(f"You have taken out this amount: {amount}")
        self.displayAccountInfo()
        return self.saldo

    def displayAccountInfo(self):
        print(f"Account Information: {self.navn} {self.etternavn}, Balance: {self.saldo}")


class Sparekonto(Bankkonto):
    uttak_limit = 8

    def taUtPenger(self, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                print("Please enter a positive withdrawal amount.")
                return self.saldo
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the withdrawal amount.")
            return self.saldo

        self.saldo -= amount
        if self.saldo < 0:
            print("You are in debt")
            print(f"Withdrawal failed. Current balance: {self.saldo + amount}")
        else:
            print(f"You have taken out this amount: {amount}")
            print(f"You have {self.uttak_limit} withdrawals left.")
        self.displayAccountInfo()
        return self.saldo


class BSUKonto(Bankkonto):
    uttak_limit = 1

    def taUtPenger(self, amount):
        if BSUKonto.uttak_limit > 0 and amount == self.saldo:
            self.saldo -= amount
            BSUKonto.uttak_limit -= 1
            if self.saldo < 0:
                print("You are in debt")
            print(f"You have taken out this amount: {amount}")
            print(f"You have no withdrawals left.")
        else:
            print("You have exceeded the maximum number of withdrawals (1).")
        self.displayAccountInfo()
        return self.saldo
