# class credit_card :
#   def __init__(self, name, number, limit, min_pay):
#     self.name = name
#     self.number = number
#     self.limit = limit
#     self.min_pay = min_pay
#     self.saldo = 0

#   def transaksi(self,nominal):
#     if nominal > 0:
#       self.saldo -= nominal
#       return f"Transaksi berhasil dilakukan, saldo terakhir menjadi Rp. {self.saldo}"
#     else:
#       return "Mohon maaf, Transaksi anda belum berhasil"

#   def saldo_terakhir(self):
#     return f"Saat ini saldo anda sekarang berjumlah Rp. {self.saldo}"
  
#   def hitung_kredit_sisa(self):
#     kredit_sisa = self.limit - self.saldo 
#     return f"Saat ini saldo anda tersisa Rp. {kredit_sisa}"
  
#   def pembayaran_kredit(self,tagihan):
#     if tagihan < self.min_pay :
#       return "Mohon maaf, pembayaran tagihan anda belum memenuhi"
#     elif tagihan > self.limit :
#       return "Mohon maaf, pembayaran tagihan anda sudah melebihi batas"
#     else:
#       self.saldo += tagihan
#       return f"Selamat, pembayaran tagihan anda sebesar Rp. {tagihan} berhasil! saldo anda bertambah menjadi Rp. {self.saldo}"

#   def tampilan(self):
#     info = f"Nomor kartu anda adalah: {self.number}\n"
#     info += f"Nama anda adalah: {self.name}\n"
#     info += f"Batas maksimum kartu kredit anda adalah: {self.limit}\n"
#     info += f"Minimal pembayaran anda adalah: {self.min_pay}\n"
#     info += f"Saldo anda adalah: {self.saldo}"
#     return info

# kartu_saya = credit_card("Theresia", "3476-7261-0964-4635", 10000000, 100000)
# print("\nInformasi kartu kredit")
# print(kartu_saya.tampilan())

# print("\nLakukan pembayaran")
# print(kartu_saya.transaksi(200000))
# print(kartu_saya.saldo_terakhir())

# print("\nMembayar tagihan kartu kredit")
# print(kartu_saya.pembayaran_kredit(700000))
# print(kartu_saya.saldo_terakhir())

# print("\nMenghitung kredit yang tersisa")
# print(kartu_saya.hitung_kredit_sisa())

#NIM:23031554110; Gatiari Dwi Panefi; 2023G
class CreditCard:
    def __init__(self, card_number, name, max_limit, min_payment):
        self.card_number = card_number
        self.name = name
        self.max_limit = max_limit
        self.min_payment = min_payment
        self.balance = 0

    def make_payment(self, quantity):
        if quantity <= 0:
            return f"Invalid payment quantity!"
        if self.balance + quantity <= self.max_limit:
            self.balance += quantity
            return f"""Payment of Rp.{quantity} SUCCESSFULLY!
            \nYour remaining balance: Rp.{self.balance}"""
        else:
            return f"Payment exceeds the maximum credit limit."

    def check_balance(self):
        return f"Current balance: Rp.{self.balance}"

    def calculate_remaining_credit(self):
        return f"Remaining credit: Rp.{self.max_limit - self.balance}"

    def pay_credit_card_bill(self, bill_quantity):
        if bill_quantity < self.min_payment:
            return f"Minimum payment not met. Please pay the minimum quantity."
        if bill_quantity <= self.balance:
            self.balance -= bill_quantity
            return f"""Credit card bill of Rp.{bill_quantity} paid SUCCESSFULLY!
            \nYour remaining balance: Rp.{self.balance}"""
        else:
            return f"""Insufficient funds to pay the bill :(
                \nPleasemake sure you have input an enough amount"""

if __name__ == "__main__":
    card = CreditCard("0000-0230-3155-4110", "Gatiari Panefi", 100000, 10000)
    
    print(card.check_balance())
    print(card.make_payment(int(input("Make payment minimum amount is Rp10000 = "))))
    print(card.check_balance())
    print(card.calculate_remaining_credit())
    print(card.pay_credit_card_bill(10000))
    print(card.check_balance())
    print(card.calculate_remaining_credit())
