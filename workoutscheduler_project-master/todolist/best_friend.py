import pandas as pd 

def riri(name):

        matrix = []
        ha = []
        f = open(name, 'r')
        csvReader = pd.read_csv(name)
        ha.append(csvReader.groupby('User')['User'].count())
        

        f.close()
        return ha
