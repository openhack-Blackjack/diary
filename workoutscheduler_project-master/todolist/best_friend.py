import pandas as pd 

def riri(name):


    ha = []

    csvReader = pd.read_csv('openhack2.csv')
    ha.append(csvReader.groupby('User')['User'].count())
    
    for a in ha:    
    	print(a)

    f.close()
    return ha
