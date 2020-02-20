import pandas as pd
import numpy as np
import bs4
import requests
import matplotlib.pyplot as plt

def get_basketball_stats(link='https://en.wikipedia.org/wiki/Michael_Jordan'):
    # read the webpage 
    response = requests.get(link)
    # create a BeautifulSoup object to parse the HTML  
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # the player stats are defined  with the attribute CSS class set to 'wikitable sortable'; 
    #therefore we create a tag object "table"
    table=soup.find(class_='wikitable sortable')

    #the headers of the table are the first table row (tr) we create a tag object that has the first row  
    headers=table.tr
    #the table column names are displayed  as an abbreviation; therefore we find all the abbr tags and returs an Iterator
    titles=headers.find_all("abbr")
    #we create a dictionary  and pass the table headers as the keys 
    data = {title['title']:[] for title in titles}
   #we will store each column as a list in a dictionary, the header of the column will be the dictionary key 

    #we iterate over each table row by fining each table tag tr and assign it to the objed
    for row in table.find_all('tr')[1:]:
    
        #we iterate over each cell in the table, as each cell corresponds to a different column we all obtain the correspondin key corresponding the column n 
        for key,a in zip(data.keys(),row.find_all("td")[2:]):
            # we append each elment and strip any extra HTML contnet 
            data[key].append(''.join(c for c in a.text if (c.isdigit() or c == ".")))

    # we remove extra rows by finding the smallest list     
    Min=min([len(x)  for x in data.values()])
    #we convert the elements in the key to floats 
    for key in data.keys():
    
        data[key]=list(map(lambda x: float(x), data[key][:Min]))
       
    return data

#create dataframes
links=['https://en.wikipedia.org/wiki/Michael_Jordan'\
    ,'https://en.wikipedia.org/wiki/Kobe_Bryant'\
    ,'https://en.wikipedia.org/wiki/LeBron_James'\
    ,'https://en.wikipedia.org/wiki/Stephen_Curry']

names=['Michael Jordan','Kobe Bryant','Lebron James','Stephen Curry']

micheal_jordan_dict = get_basketball_stats(links[0])
kode_bryant_dict = get_basketball_stats(links[1])
lebron_james_dict = get_basketball_stats(links[2])
stephen_curry_dict = get_basketball_stats(links[3])

micheal_jordan_stats = pd.DataFrame(micheal_jordan_dict)
kode_bryant_stats = pd.DataFrame(kode_bryant_dict)
lebron_james_stats = pd.DataFrame(lebron_james_dict)
stephen_curry_stats = pd.DataFrame(stephen_curry_dict)

#first five columns of the data
def displayStats(name, df):
    print(name)
    print(df.iloc[:, 0:4])
    print("\n")
    
dfs = [micheal_jordan_stats, kode_bryant_stats, lebron_james_stats, lebron_james_stats]

for i in range(4):
    displayStats(names[i], dfs[i])

#plot the data
def plotStats (name, df):
    plt.plot(df[['Points per game']], label = name)
    plt.legend()
    plt.xlabel('years')
    plt.ylabel('Points per game')
    
for i in range(4):
    plotStats(names[i], dfs[i])
    
print(lebron_james_stats[["Points per game"]])