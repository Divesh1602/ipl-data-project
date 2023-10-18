import matplotlib.pyplot as plt
import csv

# Doing calculation to get the spicific data as per reuirements
umpires_country_dict={}
with open("../../Data/umpires.csv",mode='r') as file:
	umpires_data=csv.DictReader(file)
	for row in umpires_data:
		if row[" country"]!=" India":
			if row[" country"] in umpires_country_dict:
				umpires_country_dict[row[" country"]]+=1
			else:
				umpires_country_dict[row[" country"]]=1






umpires_country=list(umpires_country_dict.keys())
umpires_number=list(umpires_country_dict.values())
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue', 'tab:orange', 'tab:green']

# Plotting the chart
plt.figure(figsize=(15,8))
plt.bar(umpires_country,umpires_number,label=umpires_country,color=colors)  #Creating the chart
plt.xlabel(r"Country $\longrightarrow$")
plt.ylabel(r"Number of umpires $\longrightarrow$")
plt.legend()
plt.title("Count of umpire")
plt.savefig("../figures/question_3_fig.png",bbox_inches='tight')  #Saving the image in different location
plt.show()