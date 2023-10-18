import csv
import matplotlib.pyplot as plt


# Doing calculation to get the spicific data as per reuirements
total_runs_scored={}
with open("../../Data/deliveries.csv",mode='r') as file:
	deliveries_data=csv.DictReader(file)
	for row in deliveries_data:
		if row["batting_team"]=="Royal Challengers Bangalore":
			if row["batsman"] in total_runs_scored:
				total_runs_scored[row["batsman"]]+=int(row["batsman_runs"])
			else:
				total_runs_scored[row["batsman"]]=int(row["batsman_runs"])
		


total_runs_scored_sorted = dict(sorted(total_runs_scored.items(), key=lambda item: item[1],reverse=True))
batsman_list=list(total_runs_scored_sorted.keys())[:10]
runs_scored_list=list(total_runs_scored_sorted.values())[:10]
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue', 'tab:orange', 'tab:green']


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