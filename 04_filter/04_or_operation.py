people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

import pandas as pd

df = pd.DataFrame (people)
print('\ndf:')
print(df)

fil = (df['last'] == 'Schafer') | (df['first'] == 'John')

# filter out with Series (fil) and 'email' column.
print("\ndf.loc[fil, 'email']:")
print(df.loc[fil, 'email'])
