import pandas
import matplotlib.pyplot as plt
from ordered_set import OrderedSet


df = pandas.read_excel('files/data.xlsx', sheet_name='Sheet1')
autumn_data = df.loc[df['Semester'] == 3]
year = OrderedSet()
schools = set()

# OVERALL INTEREST IN IUB
interest_by_year = autumn_data.groupby(['year'])
students = []
for interest in interest_by_year:
    year.update(interest[1]['year'].unique())
    students.append(interest[1].sum()['no. of Student'])
plt.style.use('seaborn-whitegrid')
plt.title('Overall interest in IUB @ Autumn')
plt.xlabel('Year')
plt.ylabel('No of Students')
plt.plot(year, students)
plt.show()


# SCHOOLWISE INTEREST IN IUB
schoolwise_interest = autumn_data.groupby(['School', 'year'])
students = []
for interest in schoolwise_interest:
    year.update(interest[1]['year'].unique())
    schools.update(interest[1]['School'].unique())
    students.append(interest[1].sum()['no. of Student'])
plt.style.use('seaborn-whitegrid')
plt.title('Schoolwise interest in IUB @ Autumn')
plt.xlabel('Year')
plt.ylabel('No of Students')
plt.stackplot(year, students)
plt.show()
