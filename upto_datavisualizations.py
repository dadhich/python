#
import pandas as pd
import numpy as np

df = pd.read_csv("C:\\AbhishekDadhichCodes\\Python\\python\\datasets\\WA_Fn-UseC_-HR-Employee-Attrition.csv")
df.shape
df.columns
df.head(5)
df.tail(5)

# high-level info of entire data frame
df.info()

# detailed stats of each column like count, mean, std, min, max, percentiles
df.describe()

df.min() # min value for each column
df["Age"].max() # max value for Age column
df["JobSatisfaction"]
df2 = df[["JobSatisfaction","Attrition", "Age"]]

# iloc = index location (splitting dataframe into [number of rows][number of columns])
df.iloc[0:10,0:4] # first 10 rows and first 4 columns
df.iloc[:,:] # all rows and all columns
df.iloc[500:,:4] # all rows from 500th row and all columns up to 4th column
df.iloc[:500,[1,3,9]] # all rows upto 500th row and only columns at index 1,3 and 9

# add a new column to an existing data frame
df["col1"] = 1 # adds new column "col1" and puts 1 in all rows
# another example of adding a new column
df["OverallSatisfaction"] = df["EnvironmentSatisfaction"] * df["JobSatisfaction"]

# delete a column from a dataframe
del df["OverallSatisfaction"]

#filter rows
df[ df["Age"] < 40 ] # all records with Age < 40
df[ (df["Age"] < 40) & (df["MonthlyRate"] > 10000) ] # all records with Age < 40 and monthly rate > 10,000

# distinct/unique values in a column
df["BusinessTravel"].unique()

# Sorting - Pandas sort_values() function sorts a data frame in Ascending or Descending order of passed Column.
# DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
# by: Single/List of column names to sort Data Frame by.
# axis: 0 or ‘index’ for rows and 1 or ‘columns’ for Column.
# ascending: Boolean value which sorts Data frame in ascending order if True.
# inplace: Boolean value. Makes the changes in passed data frame itself if True.
# kind: String which can have three inputs(‘quicksort’, ‘mergesort’ or ‘heapsort’) of algorithm used to sort data frame.
# na_position: Takes two string input ‘last’ or ‘first’ to set position of Null values. Default is ‘last’.
df.sort_values(["MonthlyRate","JobSatisfaction"],ascending=[0,1])
df.sort_values(["MonthlyRate"],ascending=False)

# group by: A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.
# DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs)
# More details: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
df1=df.groupby(["Department"],as_index=False)["Age","MonthlyIncome"].mean()

# merge - like sql joins
left_df = df
right_df = df.groupby(["Department"],as_index=False)["JobSatisfaction"].mean()
merged_df = pd.merge(left_df,right_df,how="inner",on=["Department"])

# join
left_df = df.iloc[:,:]
right_df = df.iloc[500:,:]
joined_df = left_df.join(right_df,how="right")

#concat
df_a = df.groupby(["Department"],as_index=False)["JobSatisfaction"].mean()
df_b = df.groupby(["Department"],as_index=False)["JobSatisfaction"].var()
concated_df = pd.concat([df_a,df_b],axis=1)

# pivot
df_c = df.groupby(["Department","Age"],as_index=False)["JobSatisfaction"].mean()
pivoted_df = df_c.pivot(index="Department",columns="Age",values="JobSatisfaction")