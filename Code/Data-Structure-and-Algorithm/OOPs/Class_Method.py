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

    @classmethod  # to define for class
    def convert_amount(amount):
        return float(amount)

    def get_attributes_fromstring(cls, diary_entry: str):
        tracking_category, opening_balance, budget = diary_entry.split(" ")

        return ExpenseTracker(tracking_category.capitalize(),
                              cls.convert_amount(opening_balance),
                              cls.convert_amount(budget))


print("home".capitalize())
print("home 0 1000".split(" "))

ClassObject = ExpenseTracker.get_attributes_fromstring("shopping 100 5000")
print(ClassObject.__dict__)

