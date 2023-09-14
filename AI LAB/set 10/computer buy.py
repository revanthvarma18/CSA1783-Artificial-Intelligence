# Import necessary libraries
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define the dataset
data = [
    ["<=30", "<=30", "high", "no", "fair", "no"],
    ["<=30", "<=30", "high", "no", "excellent", "no"],
    ["31...40", "<=30", "high", "no", "fair", "yes"],
    [">40", "medium", "high", "no", "fair", "yes"],
    [">40", "low", "high", "yes", "fair", "yes"],
    [">40", "low", "medium", "yes", "fair", "yes"],
    ["31...40", "low", "medium", "yes", "excellent", "no"],
    ["<=30", "medium", "medium", "no", "excellent", "yes"],
    ["<=30", "high", "no", "no", "fair", "no"],
    [">40", "medium", "no", "yes", "fair", "yes"],
    ["<=30", "medium", "no", "yes", "excellent", "yes"],
    ["31...40", "medium", "high", "no", "excellent", "yes"],
    ["31...40", ">40", "medium", "yes", "fair", "yes"],
    [">40", ">40", "low", "yes", "fair", "yes"],
    ["<=30", "<=30", "high", "no", "fair", "no"],
]

# Define the column names
columns = ["age", "income", "student", "credit", "rating", "buys_computer"]

# Create a DataFrame from the dataset
import pandas as pd
df = pd.DataFrame(data, columns=columns)

# Encode categorical variables
le = preprocessing.LabelEncoder()
for column in columns:
    df[column] = le.fit_transform(df[column])

# Define the features (X) and target (y)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Predict on the testing data
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
