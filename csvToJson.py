import csv
import json



csvfile = open('PosicaoInst.csv', 'r')


fieldnames = ("unidade","posicao")
reader = csv.DictReader( csvfile, fieldnames, delimiter=';')
firstline = True
a = []	
for row in reader:
	if firstline:
		firstline = False
		continue
	#print(row)
	#json.dump(row, jsonfile)
	#jsonfile.write('\n')
	a += ["""{
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [%s]
            },
            "properties": {
              "unidade": "%s"
            }
          }""" % (row['posicao'],row['unidade'].rstrip())]
  	
with open('PI-test2.json', 'w') as jsonfile:
	jsonfile.write("""
			{
        "type": "FeatureCollection",
        "features": [
		""")
	firstline = True  	
  	for ele in a:
  		if firstline:
  			firstline = False
  			jsonfile.write(ele)	
  			continue
  		jsonfile.write(ele)
  	jsonfile.write("""
        		]
        	}
		""")