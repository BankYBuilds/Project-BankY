#CSV Data Analyzer
import pandas as pd

data = pd.read_csv("student_dataset.csv")

records = data["Name"].count()
print(f"The numbers of students recorded are {records}")

mean_attendance = data["Attendance"].mean()
print(f"The average attendance recorded is {mean_attendance}")

mean_studyHours = data["Study_Hours"].mean()
print(f"The average study hours of the students is {mean_studyHours}")

geophysics_data = data[data["Department"] == "Geophysics"]  
mean_scoreGeophysics = geophysics_data["Score"].mean()
print(f'The mean score for Geophysics is: {mean_scoreGeophysics}')

computerscience_data = data[data["Department"] == "Computer Science"]
mean_scoreComputerScience = computerscience_data["Score"].mean()
print(f'The mean score for Computer Science is: {mean_scoreComputerScience}')

physics_data = data[data["Department"] == "Physics"]
mean_scorePhysics = physics_data["Score"].mean()
print(f'The mean score for Physics is: {mean_scorePhysics}')

Geology_data = data[data["Department"] == "Geology"]
mean_ScoreGeology = Geology_data["Score"].mean()
print(f"The mean score for Geology is: {mean_ScoreGeology}")

top_students = (
    data.sort_values(by="Score", ascending=False)
    .drop_duplicates(subset="Department")
)

print(top_students[["Department", "Name", "Score"]])