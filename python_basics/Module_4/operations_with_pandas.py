#import lib
import pandas as pd
import numpy as np

#create data
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

#clearPrint func
def clearPrint(message = "", variable = ""):
    print("-------------")
    print(message)
    print("\n")
    print(variable)
    print("\n")

#view the data
clearPrint("view the first rows of data", df.head())

#Operations
    #descriptive analysis
clearPrint("mean of each column", df.mean())
clearPrint("mean of each rows", df.mean(1))
    #map
clearPrint("Add 10 to each element of column 2", df["B"].map(lambda x: 10+x)) #map to apply func to each ele of an axis
    #apply functions to data
clearPrint("Apply functions to data", df.apply(np.cumsum)) #apply to apply a func along the axis
clearPrint("Apply functions to data", df.apply(lambda x: x.max() - x.min()))
    #applyMap: apply func to each ele in df
clearPrint("add 2 to each ele of func", df.applymap(lambda x: x+2))

#Merge data
    #concat rows
clearPrint("Print df", df)
pieces = [df[:2], df[2:4], df[4:]] #ATTENTION: write df[:2], it only takes from column 0 to 1
clearPrint("print pieces of data frame", pieces)
clearPrint("print concatenated pieces", pd.concat(pieces))

    #join data
left = pd.DataFrame({
    "key": ["foo", "bar"],
    "lval": [1, 2]
})

right = pd.DataFrame({
    "key": ["foo", "bar"],
    "lval": [4, 5]
})

mergedDataFrame = pd.merge(left, right, on="key")
clearPrint("Merged data based on key", mergedDataFrame)

#Grouping
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                            'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                        'C': np.random.randn(8),
                        'D': np.random.randn(8)})

clearPrint("new dataframe", df)
groupedDataFrame = df.groupby("A").sum()
clearPrint("groupedDataFrame", groupedDataFrame)
#hierarchical grouping
hierarchicalgroupedDataFrame = df.groupby(["A", "B"]).sum()
clearPrint("hierarchicalgroupedDataFrame", hierarchicalgroupedDataFrame)

#practice a little
df["level"] = df["B"].astype("category")
clearPrint("Category of df", df["level"])
df["level"].cat.categories = ["beginner", "expert", "amateur"]
clearPrint("df sum by categories", df.groupby("level").sum())

#Categoricals
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})

#convert a column to category
df["grade"] = df["raw_grade"].astype("category")
#rename category
df["grade"].cat.categories = ["very good", "good", "very bad"]
#reorder categories and add missing categories
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
#sort according to categorical order
clearPrint("new df with category", df.sort_values(by="grade"))
#show number of records in each category
clearPrint("number of records in each category", df.groupby("grade").size())