class ExpenseTracker:
    # class attribute
    expense_tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget


home_tracker = ExpenseTracker("Home", 3000, 10000)
print(home_tracker.tracker_category)
shopping_tracker = ExpenseTracker("Shopping", 1000, 5000)
print(shopping_tracker.tracker_category)


print(home_tracker.__dict__)  # to print the value of attribute in form of dictionary
# {'tracker_category': 'Home', 'opening_balance': 3000, 'budget': 10000} is the output of above line
print(getattr(shopping_tracker, 'opening_balance'))


# print(getattr(shopping_tracker, 'opening')) passing which is not present gives error here
print(hasattr(shopping_tracker, 'opening'))


# above line to print true or false that the value is present or not in attribute

print(delattr(home_tracker, "opening_balance"))  # used to delete a particular value from the attribute
print(home_tracker.__dict__)
