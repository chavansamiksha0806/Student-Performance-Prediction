import joblib
model=joblib.load(
    "models/student_model.pkl"
    )
# result=model.predict(
#     [
#         [5, 90, 85, 80]
#         ]
# )
# print("Predicted Final Marks:",result)

Study_Hours=float(
    input("Enter Study Hours: ")
    )
Attendance=float(
    input("Enter Attendance: ")
    )
Assignment=float(
    input("Enter Assignment Score: ")
    )
Previous_Marks=float(
    input("Enter Previous Marks: ")
    )

result=model.predict(
    [
        [
            Study_Hours,
              Attendance,
                Assignment,
                  Previous_Marks
        ]
    ]
)
print("\nPredicted Final Marks:", 
      round(result[0], 2)
      )
if result[0] >= 90:
    print("Performance:Excellent")
elif result[0] >= 80:
    print("Performance:Good")
elif  result[0]>=70:
    print("Performance:Average")
else:
    print("Performance:Needs Improvement")