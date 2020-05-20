people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

import pandas as pd

df = pd.DataFrame (people)
print('\ndf:')
print(df)
print("\ndf['last'] == 'Doe':")
print(df['last'] == 'Doe')

fil = (df['last'] == 'Doe')
print('\nfil:')
print(fil)
print('\ntype(fil):')
print(type(fil))
print('\ndf[fil]:')
print(df[fil])

# The second way, we can use loc. This is a preferred way.
print('\ndf.loc[fil]:')
print(df.loc[fil])

# filter out with Series (fil) and 'email' column.
print("\ndf.loc[fil, 'email']:")
print(df.loc[fil, 'email'])
