#CSV DATA ANALYZER 2.0

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_performance.csv")

department = data["Department"]
student_number = data["Student"].count()
avg_score = data["Score"].mean()
max_score = data["Score"].max()
avg_study = data["Study Hours"].mean()
geology = data[data["Department"] == "Geology"]
physics = data[data["Department"] == "Physics"]
physics_scores = physics["Score"].sum()
geology_scores = geology["Score"].sum()
avg_physics = physics['Score'].mean()
avg_geology = geology["Score"].mean() 
top_students = (
    data.sort_values(by="Score", ascending=False)
    .drop_duplicates(subset="Department")
)
print(f"The number of Students is {student_number}")
print(f"The Average score is: {avg_score}")
print(f"The Highest score is: {max_score}")
print(f"The Average study time is: {avg_study}")
if physics_scores > geology_scores:
    print(f"The department with the highest score is Physics: {physics_scores}")
else:
    print(f"The department with the highest score is Geology: {geology_scores}")
print(top_students[["Department", "Student", "Score"]])

category_department = data.groupby("Department")["Score"].mean()
plt.bar(category_department.index, category_department.values)
plt.xlabel("Department")
plt.ylabel("Average Score")
plt.title("Average Score by Department")
plt.show()