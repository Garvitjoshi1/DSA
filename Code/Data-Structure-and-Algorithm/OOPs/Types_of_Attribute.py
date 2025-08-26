class ExpenseTracker:
    # Class Attribution
    version_application = 0.1
    '''Class Expense Tracker'''

    def __init__(self, tracker_category, opening_balance, budget):
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget


home_tracker = ExpenseTracker("Home", 1000, 60000)
shopping_tracker = ExpenseTracker("shopping", 1000, 5000)
print(home_tracker.tracker_category)
print(getattr(home_tracker, "tracker_category"))
print(home_tracker.__dict__)
print(home_tracker.version_application)
print(shopping_tracker.version_application)

home_tracker.version_application = 0.2
# easy to update values
print(home_tracker.version_application)
