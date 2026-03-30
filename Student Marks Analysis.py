import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Ishita", "Arjun", "Sara"],
    "Maths": [78, 85, 67, 90, 55, 88, None, 72],
    "Science": [82, 79, 70, 92, 60, None, 75, 68],
    "English": [75, 88, 65, 91, 58, 84, 77, None]
}
df
df = pd.DataFrame(data)
df.isnull().sum()
df['Maths']=df['Maths'].fillna(df['Maths'].mean())
df['Science']=df['Science'].fillna(df['Science'].mean())
df['English']=df['English'].fillna(df['English'].mean())
df['Total Marks'] = df[['Maths','Science','English']].sum(axis=1)
df.sort_values('Total Marks',ascending=True)
df[['Maths','Science','English']].mean()
df.loc[df['Maths'].idxmax(), 'Name']
df.loc[df['English'].idxmax(), 'Name']
df.loc[df['Science'].idxmax(), 'Name']
