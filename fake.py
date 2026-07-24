import numpy as np

day = np.array(["SUNDAY",
                 "MODAY",
                 "TUSEDAY",
                 "WENESDAY",
                 "THURSDAY",
                 "FRIDAY",
                 "SATURDAY"])

expense = np.array([234,566,134,978,876,654,423])

highest = np.argmax(expense)
highest_expense_day = day[highest]

print(highest_expense_day)