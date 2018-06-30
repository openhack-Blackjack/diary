import csv
import operator

def riri():
	ha = []
	f = open('openhack2.csv', 'r')
	csvReader = csv.reader(f)
	for row in csvReader:
		ha.append(row[1])
	my_dict ={i:ha.count(i) for i in ha}
	sort_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse = True)
	f.close()
	return sort_dict
dd = riri()


for d in dd:
	print(d[1])