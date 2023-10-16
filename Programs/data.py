import csv

def extracting_matches_data():
	matches_data = open("/home/divesh/Desktop/Python/Projects/IPL-project/Data/matches.csv")
	matches_csv_data=csv.DictReader(matches_data)
	matches_data_list=list(matches_csv_data)
	matches_data.close()
	return matches_data_list


def extracting_deliveries_data():
	deliveries_data= open("/home/divesh/Desktop/Python/Projects/IPL-project/Data/deliveries.csv")
	deliveries_csv_data=csv.DictReader(deliveries_data)
	deliveries_data_list=list(deliveries_csv_data)
	deliveries_data.close()
	return deliveries_data_list

def extracting_umpires_data():
	umpires_data= open("/home/divesh/Desktop/Python/Projects/IPL-project/Data/umpires.csv")
	umpires_csv_data=csv.DictReader(umpires_data)
	umpires_data_list=list(umpires_csv_data)
	umpires_data.close()
	return umpires_data_list

