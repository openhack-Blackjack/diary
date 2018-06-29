import csv

def riri(name):

	matrix = []
	ha = []
	f = open(name, 'r')
	csvReader = csv.reader(f)
	for row in csvReader:
		matrix.append(row)
		if 'https://' in row[2]:
			ha.append(row[2])


	f.close()
	return ha
