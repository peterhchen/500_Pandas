import pandas as pd
df = pd.read_csv('../csv_data/survey_results_public.csv')
# set display to 85 columns
print('\ndf.head():')
print(df.head())

print("\ndf.columns")
print(df.columns)

print("\ndf.loc[0:2, 'Respondent':'Hobbyist']:")
print(df.loc[0:2, 'Respondent':'Hobbyist'])
