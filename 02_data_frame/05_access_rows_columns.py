# Python dictionary has key and value
# This is a single person
person = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMSchafer@gmail.com"
}

# Make the dictionary a list.
# We have single list with one person.
people = {
    "first": ["Corey"],
    "last": ["Schafer"],
    "email": ["CoreyMSchafer@gmail.com"]
}

# We can have multiple persons.
# The key is the columns and values are the rows. 
# The pandas data frame is row and columns.
people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

import pandas as pd

df = pd.DataFrame (people)
print("\ndf.iloc[[0, 1], [1, 2]:")
print(df.iloc[[0, 1], [1, 2]])