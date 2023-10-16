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
	
	if deliveries_data_list[i]["batting_team"] in total_runs_scored:
		total_runs_scored[deliveries_data_list[i]["batting_team"]]+=int(deliveries_data_list[i]["total_runs"])
	else:
		total_runs_scored[deliveries_data_list[i]["batting_team"]]=int(deliveries_data_list[i]["total_runs"])
	i+=1

team_names_list=list(total_runs_scored.keys())
runs_scored_list=list(total_runs_scored.values())
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink']


# For debugging purpose
# i=0
# while i<len(team_names_list):
# 	print("{} :{}".format(team_names_list[i],runs_scored_list[i]))
# 	i+=1


# Plotting the graph
plt.figure(figsize=(20 ,15))  # Set the figure size to 10x6 inches    
plt.bar(team_names_list,runs_scored_list,label=team_names_list,color=colors)    
plt.xticks(rotation=270,fontsize=10)           #Rotated the names on x-axis
plt.legend(bbox_to_anchor =(0.40, 1.15), ncol = 3)
plt.xlabel(r'Teams $\longrightarrow$')
plt.ylabel(r"Runs $\longrightarrow$")
plt.title("Total runs scored by teams")
plt.savefig("../figures/question_1_fig.png",bbox_inches='tight')    #Saving the figure in the given paths
plt.show()