class ExpenseTracker:
    """this is a class to do expense tracking"""

    # '''line to add''' this method is considered as ideal to let reader know what's in the class.
    def __init__(self):
        pass


# below is the way to build a object
obj1 = ExpenseTracker()


# ExpenseTracker() used to call the value of class.

class ExpenseTracker:
    """this is a class to do expense tracking"""

    # '''line to add''' this method is considered as ideal to let reader know what's in the class.
    def __init__(self, date, description, transaction, type, amount):
        self.date = date  # to add these values to self of the class.
        self.description = description
        self.transaction = transaction
        self.type = type
        self.amount = amount


# obj2 = ExpenseTracker()  this line does work because values of def not defined in class
obj2 = ExpenseTracker(24, "Hello", 5000, "Debit", "Lacs")
print(obj2.transaction)
obj3 = ExpenseTracker(25, "Hi again", 25000, "Credit", "Lacs")
print(obj3.transaction)
# https://docs.python.org/3/contents.html refer this to learn more from python documentation
