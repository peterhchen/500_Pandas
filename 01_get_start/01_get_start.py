import pandas as pd
df = pd.read_csv('../csv_data/survey_results_public.csv')
# set display to 85 columns
#pd.set_option ('display.max_columns', 85)
#pd.set_option ('display.max_rows', 85)
print('\ndf:')
print(df)               # [88883 rows x 85 columns]
# df.shape: shape is an attribute, not a method.
print('\ndf.shape:')
print(df.shape)         # (99993, 85)
# df.info(): info is a method
print ('\ndf.info():')
print (df.info())
# df.head(): first 5 rows
print ('\ndf.head():')
print (df.head())

schema_df = pd.read_csv('../csv_data/survey_results_schema.csv')
print('\nschema_df:')
print(schema_df) 