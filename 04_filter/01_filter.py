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
