import pandas as pd
import os

df = pd.read_csv("Student Grading & Report System/studentReports.csv")
df.columns = df.columns.str.strip()

output_dir = "Student Grading & Report System/Student Report Card"
os.makedirs(output_dir, exist_ok=True)

def OverallGPA(grade):
    if grade >= 90:
        return 4
    elif grade >= 80:
        return 3
    elif grade >= 70:
        return 2
    elif grade >= 60:
        return 1
    else:
        return 0
    
def gradeOverall(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
    
for _, row in df.iterrows():
    name = row ['Student Name']
    email = row ['Student Email']

    scores = row.drop(['Student Name', 'Student Email']).astype(int)
    average = scores.mean()
    grade = gradeOverall(average)
    gpas = [OverallGPA(score) for score in scores]
    gpa = sum(gpas) / len(gpas)

    report = f"Grade Report for {name}\n"
    report += f"Student Email:{email}\n\n"
    report += "-----------------------------------\n"
    report += "Grades: "
    for subject, score in scores.items():
        report += f"- {subject}: {score}\n"
    report += "-----------------------------------\n\n"
    report += f"Grade Score: {average:.2f}\n"
    report += f"Final Grade: {grade}\n"
    report += f"GPA: {gpa:.2f}\n"

    filename = f"{output_dir}/{name.replace(' ', '_')}_report.txt"
    with open(filename, "w") as f:
        f.write(report)

print("Report Cards for each student have been generated.")
