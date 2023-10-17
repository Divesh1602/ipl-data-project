import matplotlib.pyplot as plt
import sys

# Adding the path so that it can find the desired file in the given path also
sys.path.append("/home/divesh/Desktop/Python/Projects/IPL-project/Programs")
from data import extracting_umpires_data 

# Calling function from different file to get the data
umpires_data_list=extracting_umpires_data()
print(umpires_data_list)
# Doing calculation to get the spicific data as per reuirements
umpires_country_dict={}
i=1
while i<len(umpires_data_list):
	if umpires_data_list[i][" country"]!=" India":
		if umpires_data_list[i][" country"] in umpires_country_dict:
			umpires_country_dict[umpires_data_list[i][" country"]]+=1
		else:
			umpires_country_dict[umpires_data_list[i][" country"]]=1
	i+=1


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