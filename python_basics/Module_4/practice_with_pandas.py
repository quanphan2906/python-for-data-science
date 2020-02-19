#import lib
import pandas as pd

#import data
data = pd.read_csv("../uk-500.csv")

#clearPrint func
def clearPrint(message, variable):
    print("-------------")
    print(message)
    print("\n")
    print(variable)
    print("\n")

#Quick summary of data
clearPrint("Columns of data frame", data.columns) #500 records, 11 variables
clearPrint("Get unique value of a column of the df", data["city"].unique())
clearPrint("Rows of data frame", data.index) #500 records, 11 variables
clearPrint("Quick summary to data", data.describe())

#View data
clearPrint("First rows of the data", data.head())

#sorting by column
clearPrint("Sorting by a column", data.sort_values(by="first_name"))

#-------------------
#INDEXING
    #set index
data.set_index("first_name", inplace = True)


clearPrint("Getting a single column", data["city"]) #return a Series
clearPrint("Getting rows", data[0:3])
clearPrint("Getting a single row", data[1:2]) #or data.iloc[[1], :]

    #selection by label
    #in orde to select by label, setting index of data frame is required
clearPrint("Retrieve Aleshia's lastname", data.loc["Aleshia", "last_name"])
clearPrint("Select a cross section by label", data.loc["Aleshia"])
clearPrint("Select on a multi-axis by label", data.loc[:, ["last_name", "city"]])
clearPrint("Label slicing on rows and columns", data.loc["Aleshia":"Tyisha", "company_name":"city"])
clearPrint("Input an array of labels and columns", data.loc[["Aleshia", "Evan", "Tyisha"], ["company_name", "city"]])

    #seleciton by index
clearPrint("Cross section by position", data.iloc[1:3]) #or data.iloc[1:3, :]

    #boolean indexing
clearPrint("Selection by boolean", data.loc[data["city"] == "Abbey Ward", ["company_name", "city"]])
