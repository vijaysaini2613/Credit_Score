from tkinter import *
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/credit_data.csv")
X = df.drop("Approved", axis=1)
y = df["Approved"]

# Encode target
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train model
model = RandomForestClassifier()
model.fit(X, y_encoded)

# Predictor function
def predict():
    age = int(e1.get())
    income = int(e2.get())
    debt = int(e3.get())
    past_due = int(e4.get())
    credit_years = int(e5.get())
    loan_amount = int(e6.get())

    input_data = pd.DataFrame([[age, income, debt, past_due, credit_years, loan_amount]],
                              columns=X.columns)
    pred = model.predict(input_data)[0]
    result = le.inverse_transform([pred])[0]
    result_label.config(text=f"Prediction: {result}")

# GUI window
root = Tk()
root.title("Credit Score Predictor")
root.geometry("400x500")
root.config(bg="skyblue")

# Heading
title = Label(root, text="CrediClear", fg="black", bg="skyblue", font=("Aharoni", 40, "bold"))
title.grid(row=1, column=0, columnspan=3, pady=10)

subtitle = Label(root, text="– Your Path to Approval.", fg="yellow", bg="skyblue", font=("Elephant", 20))
subtitle.grid(row=2, column=0, columnspan=2)

author = Label(root, text="A project by - VIJAY K SAINI", fg="green", bg="skyblue", font=("Elephant", 10))
author.grid(row=14, column=1, sticky=E, pady=10)

# Input labels and fields
Label(root, text="Age", bg="skyblue").grid(row=4, column=0, sticky=W, padx=20, pady=5)
e1 = Entry(root)
e1.grid(row=4, column=1, pady=5)

Label(root, text="Income", bg="skyblue").grid(row=5, column=0, sticky=W, padx=20, pady=5)
e2 = Entry(root)
e2.grid(row=5, column=1, pady=5)

Label(root, text="Debt", bg="skyblue").grid(row=6, column=0, sticky=W, padx=20, pady=5)
e3 = Entry(root)
e3.grid(row=6, column=1, pady=5)

Label(root, text="Past Due Payments", bg="skyblue").grid(row=7, column=0, sticky=W, padx=20, pady=5)
e4 = Entry(root)
e4.grid(row=7, column=1, pady=5)

Label(root, text="Credit History (Years)", bg="skyblue").grid(row=8, column=0, sticky=W, padx=20, pady=5)
e5 = Entry(root)
e5.grid(row=8, column=1, pady=5)

Label(root, text="Loan Amount", bg="skyblue").grid(row=9, column=0, sticky=W, padx=20, pady=5)
e6 = Entry(root)
e6.grid(row=9, column=1, pady=5)

# Buttons
Button(root, text='Predict', command=predict, bg="lightgreen").grid(row=11, column=0, pady=20)
Button(root, text='Exit', command=root.quit, bg="lightcoral").grid(row=11, column=1, pady=20)

# Prediction label
result_label = Label(root, text="Prediction: ", bg="black", fg="white", font=("Arial", 12))
result_label.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()
# Run the GUI