people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

import pandas as pd

df = pd.DataFrame (people)
print('\ndf:')
print(df)
# to display the email column
print("\ndf['email']:")
print(df['email'])
# To assign the 'email' as the index
df.set_index('email')
print("\ndf.set_index('email'):")
print(df.set_index('email'))
print('\ndf:')
print(df)

print("\ndf.set_index('email', inplace=True):")
print(df.set_index('email', inplace=True))
print('\ndf:')
print(df)
print('\ndf.index:')
print(df.index)
print("\ndf.loc['CoreyMSchafer@gmail.com']:")
print(df.loc['CoreyMSchafer@gmail.com'])
print("\ndf.loc['CoreyMSchafer@gmail.com', 'last']:")
print(df.loc['CoreyMSchafer@gmail.com', 'last'])
print("\ndf.iloc[0]:")
print(df.iloc[0])