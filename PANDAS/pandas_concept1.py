# import pandas as pd
# shop = pd.read_csv('./PANDAS/shop.csv')
# print(shop.head())
# print()
# print(shop.tail())
# print()
# print(shop.head(3))
# print()
# print(shop.tail(4))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the data from CSV file. Replace 'student_data.csv' with your actual file path.
data = pd.read_csv('student_data.csv')

# Let's assume our columns are as follows:
# - 'study_hours': number of hours a student studies per week
# - 'sleep_hours': number of hours a student sleeps per day
# - 'avg_grade': average grade of the student
# - 'dropout': binary target variable (1 if dropped out, 0 if not)

# Check for missing data and remove any rows with missing values.
data = data.dropna()

# Define features and target variables.
X = data[['study_hours', 'sleep_hours']]
y = data['dropout']

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression classifier.
clf = LogisticRegression()

# Train the model using the training sets.
clf.fit(X_train, y_train)

# Make predictions using the testing set.
y_pred = clf.predict(X_test)

# Check the accuracy of our classifier
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Visualize the results (optional)
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap="YlGnBu")
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()