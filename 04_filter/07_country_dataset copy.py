people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

import pandas as pd
df = pd.read_csv('../csv_data/survey_results_public.csv')
#set display to 85 columns
pd.set_option ('display.max_columns', 85)
pd.set_option ('display.max_rows', 85)
#print ('\ndf.head(5):')
#print (df.head(5))

countries = ['United States', 'India']
fil = df['Country'].isin(countries)

# filter out with Series (fil) and 'email' column.
print("\ndf.loc[fil, 'Country']:")
print(df.loc[fil, 'Country'])
