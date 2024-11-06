import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'Age': [22, 29, 34, 28, 45, 36, 32, 30, 40, 31, 29, 26, 24],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male', 'Female'],
    'Mental_Health_Condition': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Gender', hue='Mental_Health_Condition')
plt.title('Mental Health Condition Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(8, 5))
sns.histplot(data=df[df['Mental_Health_Condition'] == 'Yes'], x='Age', bins=5, kde=True, color='blue')
plt.title('Age Distribution of People with Mental Health Conditions')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()