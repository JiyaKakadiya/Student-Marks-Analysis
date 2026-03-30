import pandas as pd

# Step 1: Create DataFrame
data = {
    "Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Ishita", "Arjun", "Sara"],
    "Maths": [78, 85, 67, 90, 55, 88, None, 72],
    "Science": [82, 79, 70, 92, 60, None, 75, 68],
    "English": [75, 88, 65, 91, 58, 84, 77, None]
}

df = pd.DataFrame(data)

print("\n===== ORIGINAL DATAFRAME =====")
print(df)


# Step 2: Check Null Values
print("\n===== NULL VALUES =====")
print(df.isnull().sum())


# Step 3: Fill Null Values with Mean
df['Maths'] = df['Maths'].fillna(df['Maths'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
df['English'] = df['English'].fillna(df['English'].mean())

print("\n===== DATAFRAME AFTER FILLING NULL VALUES =====")
print(df)


# Step 4: Create Total Marks Column
df['Total Marks'] = df[['Maths', 'Science', 'English']].sum(axis=1)

print("\n===== DATAFRAME WITH TOTAL MARKS =====")
print(df)


# Step 5: Sort by Total Marks
sorted_df = df.sort_values(by='Total Marks', ascending=False)

print("\n===== SORTED DATAFRAME (HIGHEST TO LOWEST) =====")
print(sorted_df)


# Step 6: Mean of Each Subject
print("\n===== MEAN MARKS =====")
print(df[['Maths', 'Science', 'English']].mean())


# Step 7: Top Scorers
print("\n===== TOP SCORERS =====")
print("Maths Topper:", df.loc[df['Maths'].idxmax(), 'Name'])
print("Science Topper:", df.loc[df['Science'].idxmax(), 'Name'])
print("English Topper:", df.loc[df['English'].idxmax(), 'Name'])
