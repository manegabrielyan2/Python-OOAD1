#bank accout
from datetime import timedelta, timezone, datetime

class BankAccount:
    def __init__(self , acc):
        self.id = 0
        self.account_number = acc
        self._firstname = ''
        self._lastname = ''
        self._time_zone = 0
        self._balance = 0
        
    def set_firstname(self , name):
        if  ( not isinstance(name , str) or name == ''):
            raise ValueError('Name cannot be empty')
        self._firstname = name

    
    def set_lastnamename(self , lastname):
        if  ( not isinstance(lastname , str) or lastname == ''):
            raise ValueError('Lastname cannot be empty')
        self._lastname = lastname

    def set_timezone(self , time):
        time = datetime.now() + timedelta(hours=time)
        # offset = timedelta(hours=time)
        # current_utc_time = datetime.now(timezone.utc)
        # current_time_in_preferred_zone = current_utc_time + offset
        self._time_zone = time
        
    def get_timezone(self):
        return self._time_zone

    def set_balance(self , balance):
        if not isinstance(balance , int) or balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance
        
    def get_balance(self):
        return self._balance
    
    def get_id(self):
        return self.id

    def deposit(self , sum):
        self.set_balance(self.get_balance() + sum)
        self.id += 1

    def withdrawal(self , sum):
        n = self.get_balance()
        if self.get_balance() < sum:
            raise ValueError('Withdrawal declined due to lack of funds.')
        self.set_balance(self.get_balance() - sum)
        self.id += 1
        if n == self.get_balance():
            return False
    def interest_rate(self , rate):
        old = self.get_balance()
        self.set_balance(old + (old * rate) / 100 )
        self.id += 1

    def confirmation(self , transaction = 'x' ):
        if (transaction == 'withdrawal' and self.withdrawal()):
            return f"W - {self.account_number} - {self.get_timezone()} - {self.id} "
        if transaction == 'deposit' :
            return f"D - {self.account_number} - {self.get_timezone()} - {self.id} "
        if transaction == 'interest rate':
            return f"I - {self.account_number} - {self.get_timezone()} - {self.id} " 
        if not self.withdrawal():
            return f"X - {self.account_number} - {self.get_timezone()} - {self.id} " 
        




n = BankAccount(234546)
n.set_timezone(4)
# print(n.get_timezone())
n.set_firstname('Mane')
n.set_lastnamename('G')
n.set_balance(1200)
n.withdrawal(200)
n.deposit(100)
print(n.confirmation('deposit'))