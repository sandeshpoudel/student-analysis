import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import pyreadstat  # This reads .sav files

# Load the .sav file
df, meta = pyreadstat.read_sav('SPSS-Ready-Data.sav')  # Replace with your filename

# to export in csv format
                # # Export to CSV
                # df.to_csv('exported_data.csv', index=False)
                # print("Export complete. File saved as 'exported_data.csv'")


#I created satisfaction column
satisfaction_cols = [
    '@14.Realworld_Use',
    '@15.Thecourse_uptodate',
    '@16.Thecoursecontribute_careerplans',
    '@17.Course_theoryandpractical',
    '@18.Teacher_subjectareas',
    '@19.Classroomteaching',
    '@20.Teachers_available',
    '@21.Practical_effective',
    '@22.Teaching_practical',
    '@23.Thelibrary_resource',
    '@24.Com_Internet',
    '@25.Thecampus_Software',
    '@26.Projector',
    '@27.Campus_support_assignmentsandpr',
    '@28.staff_cooperativeandhelpful',
    '@29.Toiletsandsanitation',
    '@30.Drinkingwater',
    '@31.canteen',
    '@32.ECA',
    '@33.Internalassessment',
    '@34.Teachers_feedback',
    '@35.Makeupexams',
    '@36.Finalexams',
    '@37.Results_published'
]


# See first few rows
# print(df.head())



# Add an 'average satisfaction' column per respondent
df['Avg_Satisfaction'] = df[satisfaction_cols].mean(axis=1)

# Group by semester
semester_satisfaction = df.groupby('@3.Semester')['Avg_Satisfaction'].mean().sort_index()

print("Average Satisfaction by Semester:")
print(semester_satisfaction)



semester_satisfaction.plot(kind='line', marker = 'o')
plt.title("Average Satisfaction by Semester")
plt.xlabel("Semester")
plt.ylabel("Mean Satisfaction Score")
plt.tight_layout()
plt.show()
