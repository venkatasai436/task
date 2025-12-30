
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 1: Load the Titanic dataset
# We load the CSV file into a DataFrame
# A DataFrame is a table-like structure (rows & columns)

df = pd.read_csv("/content/Titanic-Dataset.csv")
# STEP 2: Understand the dataset (MOST IMPORTANT STEP)
# 2.1 View first 5 rows
# This helps us understand column names and sample values
df.head()

# 2.2 Dataset structure
# Shows column names, data types, and missing values
df.info()

# 2.3 Check missing values column-wise
# Real-world datasets are messy → this is mandatory
df.isnull().sum()

# 2.4 Statistical summary of numerical columns
# Gives mean, median, min, max, etc.
df.describe()
# QUESTION 1: Survival Rate by Passenger Class
# Group passengers by class (1st, 2nd, 3rd)
# Take the mean of Survived column
# Mean works because Survived = 1 (yes), 0 (no)

survival_by_class = df.groupby("Pclass")["Survived"].mean()
print("\nSurvival Rate by Passenger Class:")
print(survival_by_class)

# QUESTION 2: Gender Bias in Survival
# Survival rate by gender
survival_by_gender = df.groupby("Sex")["Survived"].mean()
print("\nSurvival Rate by Gender:")
print(survival_by_gender)

# Overall survival rate
overall_survival = df["Survived"].mean()
print("\nOverall Survival Rate:", overall_survival)

# QUESTION 3: Cabin Availability Analysis
# Create a new feature:
# True → passenger has cabin info
# False → cabin info missing (mostly lower class)

df["Has_Cabin"] = df["Cabin"].notnull()

# Compare survival rates
cabin_survival = df.groupby("Has_Cabin")["Survived"].mean()
print("\nSurvival Based on Cabin Availability:")
print(cabin_survival)

# QUESTION 4: Family Size Impact
# Feature engineering:
# FamilySize = siblings/spouse + parents/children + self

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Correlation with survival
family_corr = df["FamilySize"].corr(df["Survived"])
print("\nCorrelation between Family Size and Survival:", family_corr)

# Visualization
df["FamilySize"].hist(bins=10)
plt.xlabel("Family Size")
plt.ylabel("Passenger Count")
plt.title("Family Size Distribution")
plt.show()

# QUESTION 5: Age Distribution – Survivors vs Non-Survivors
# Separate survived and not survived passengers
survived = df[df["Survived"] == 1]
not_survived = df[df["Survived"] == 0]
# Plot age distributions
survived["Age"].plot(kind="hist", bins=20, alpha=0.7, label="Survived")
not_survived["Age"].plot(kind="hist", bins=20, alpha=0.7, label="Not Survived")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()
plt.title("Age Distribution by Survival")
plt.show()


# QUESTION 6: Embarkation Port Analysis

# Fill missing Embarked values with mode (most common value)
# We avoid inplace=True to be future-proof

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Survival rate per port
embarked_survival = df.groupby("Embarked")["Survived"].mean()
print("\nSurvival Rate by Embarkation Port:")
print(embarked_survival)

# QUESTION 7: Ticket Class vs Survival


# Extract first character from Ticket (ticket prefix)
df["Ticket_Class"] = df["Ticket"].str[0]

ticket_survival = df.groupby("Ticket_Class")["Survived"].mean()
print("\nSurvival Rate by Ticket Class:")
print(ticket_survival)


# QUESTION 8: Missing Fare Handling


# Check missing Fare values
print("\nMissing Fare Values:", df["Fare"].isnull().sum())

# Fill missing Fare using median Fare of passenger class
df["Fare"] = df.groupby("Pclass")["Fare"].transform(
    lambda x: x.fillna(x.median())
)

# QUESTION 9: Correlation Matrix Analysis

# Select numerical columns
corr_matrix = df[["Survived", "Age", "Fare"]].corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

# Heatmap visualization
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# QUESTION 10: Advanced Family Size Analysi

# Family size without counting self
df["FamilySize2"] = df["SibSp"] + df["Parch"]

# Categorize family types
df["FamilyGroup"] = df["FamilySize2"].apply(
    lambda x: "Solo" if x == 0 else "Small Family" if x == 1 else "Large Family"
)

family_group_survival = df.groupby("FamilyGroup")["Survived"].mean()
print("\nSurvival Rate by Family Group:")
print(family_group_survival)

