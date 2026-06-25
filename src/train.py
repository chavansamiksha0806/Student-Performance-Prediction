import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv(
"dataset/student_data.csv"
)

data.columns = (
data.columns.str.strip()
)

X = data[
[
"Study_Hours",
"Attendance",
"Assignment",
"Previous_Marks"
]
]

y = data["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

model = LinearRegression()

model.fit(
X_train,
y_train
)

joblib.dump(
model,
"models/student_model.pkl"
)

print(
"Training Complete"
)