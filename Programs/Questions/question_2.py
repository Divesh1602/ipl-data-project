import sys
import matplotlib.pyplot as plt

# Adding the path so that it can find the desired file in the given path also
sys.path.append("/home/divesh/Desktop/Python/Projects/IPL-project/Programs")
from data import extracting_deliveries_data 

# Calling function from different file to get the data
deliveries_data_list=extracting_deliveries_data()

# Doing calculation to get the spicific data as per reuirements
total_runs_scored={}
i=1
while i<len(deliveries_data_list):
	if deliveries_data_list[i]["batting_team"]=="Royal Challengers Bangalore":
		if deliveries_data_list[i]["batsman"] in total_runs_scored:
			total_runs_scored[deliveries_data_list[i]["batsman"]]+=int(deliveries_data_list[i]["batsman_runs"])
		else:
			total_runs_scored[deliveries_data_list[i]["batsman"]]=int(deliveries_data_list[i]["batsman_runs"])
	i+=1
total_runs_scored_sorted = dict(sorted(total_runs_scored.items(), key=lambda item: item[1],reverse=True))
batsman_list=list(total_runs_scored_sorted.keys())[:10]
runs_scored_list=list(total_runs_scored_sorted.values())[:10]
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue', 'tab:orange', 'tab:green']

# For debugging purpose
# i=0
# while i<len(batsman_list):
# 	print("{} :{}".format(batsman_list[i],runs_scored_list[i]))
# 	i+=1


# Plotting the chart
plt.figure(figsize=(15, 10))  # Set the figure size to 10x6 inches    
plt.bar(batsman_list,runs_scored_list,label=batsman_list,color=colors)    
plt.xticks(rotation=270,fontsize=10)           #Rotated the names on x-axis
plt.legend(bbox_to_anchor =(1, 1.15), ncol = 3)
plt.xlabel(r'Batsman $\longrightarrow$')
plt.ylabel(r"Runs $\longrightarrow$")
plt.title("Top 10 Batsman")
plt.savefig("../figures/question_2_fig.png",bbox_inches='tight')    #Saving the figure in the given paths
plt.show()