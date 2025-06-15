class ExpenseTracker:
    # Class Attribution
    version_application = 0.1
    '''This is a docstring which defines the purpose of class, just like comments'''

    def __init__(self, tracker_category, opening_balance, budget):
        # Instance/Object Attribute
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

    # Instance Method
    def get_original_balanced(self):
        return self.opening_balance

    def check_balance(self, limit=100000):
        if self.budget >= limit:
            return True
        else:
            return "Your opening balance is less than limit"

    @staticmethod
    # @staticmethod is compulsory to addd because it defines the use of def used below
    def convert_amount(amount):
        return float(amount)


obj = ExpenseTracker("Home", 0, 10000)
print(obj.get_original_balanced())

obj1 = ExpenseTracker("Home", 50, 10000)
print(obj1.get_original_balanced())

obj2 = ExpenseTracker("Home", 50, 10000)
print(obj2.check_balance(limit=100000))

print(obj.convert_amount(20000))
