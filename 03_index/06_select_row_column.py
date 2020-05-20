

import pandas as pd
df = pd.read_csv('../csv_data/survey_results_public.csv')
# pd.set_option('display.max_columns', 85)
# pd.set_option('display.max_rows', 5)
print ('\ndf.head():')
print (df.head())
df = pd.read_csv('../csv_data/survey_results_public.csv', index_col='Respondent')
print ('\ndf.head():')
print (df.head())

schema_df = pd.read_csv('../csv_data/survey_results_schema.csv')
print('\nschema_df.head():')
print(schema_df.head()) 
schema_df = pd.read_csv('../csv_data/survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_rows', 85)
print('\nschema_df:')
print(schema_df) 

print("\nschema_df.loc['MgrIdiot', 'QuestionText']:")
print(schema_df.loc['MgrIdiot', 'QuestionText'])
