import pandas as pd
df = pd.read_csv('../csv_data/survey_results_public.csv')
# set display to 85 columns
print('\ndf.head():')
print(df.head())

print("\ndf['Hobbyist']")
print(df['Hobbyist'])
print("\ndf['Hobbyist'].value_counts()")
print(df['Hobbyist'].value_counts())

print('\ndf.iloc[[0,1], [1,2]]:')
print(df.iloc[[0,1], [0,1,2]])

print("\ndf.loc[[0,1], ['Respondent','MainBranch', 'Hobbyist']]:")
print(df.loc[[0,1], ['Respondent','MainBranch', 'Hobbyist']])

