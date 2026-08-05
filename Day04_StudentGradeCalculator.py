#STUDENT GRADE CALCULATOR

grades = {
    'Physiscs' : 68,
    'Mathematics' : 78,
    'Use of English' : 57,
    'Chemistry' : 57,
    'Biology' : 65
}

for value in grades.values():
      avg = sum(grades.values())/len(grades.values())
      if avg >= 70:
            grade = "A"
            status = "Pass"
      elif avg  >= 60:
            grade = "B"
            status = "Pass"
      elif avg  >= 50:
            grade = "C"
            status = "Pass"
      elif avg  >= 45:
            grade = "D"
            status = "Pass"
      else:
            grade = "F"
            status = "Fail"


hg = max(grades.values())
lg = min(grades.values())


for subject, scores in grades.items():
      print(f'{subject}: {scores}')

print(f"Highest Score:", hg)
print(f'Lowest Score:', lg)
print(f'Final Grade:', grade)
print("Status:", status)