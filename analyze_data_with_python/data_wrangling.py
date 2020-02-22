import pandas as pd
import matplotlib.pylab as plt
import numpy as np

#prepare clearPrint function
def clearPrint(message = "", variable = ""):
    print("-------------")
    print(message)
    print("\n")
    print(variable)
    print("\n")

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

#param names set the headers for columns
df = pd.read_csv(filename, names = headers)
#preview the data
clearPrint("first five rows before cleaning", df.head())

#------------------
#IDENTIFY AND HANDLE MISSING DATA

#replace "?" with NaN
df.replace("?", np.nan, inplace = True)
print("first five rows after changing", df.head())
