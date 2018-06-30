import pandas as pd 

def riri(name):
	ha = []
	
	f = open('openhack2.csv', 'r')
	csvReader = pd.read_csv(f)
	ha.append(csvReader.groupby('User')['User'].count())
	f.close()

	print(ha)
	return ha
