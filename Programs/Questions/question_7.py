import csv
import matplotlib.pyplot as plt

# Doing calculation to get the spicific data as per reuirements
extra_runs_data_dict={}

with open("../../Data/matches.csv",'r') as file1,open("../../Data/deliveries.csv",'r') as file2:

    matches_data=csv.DictReader(file1)
    deliveries_data=csv.DictReader(file2)
    match_id_list=[]
    for row in matches_data:
        if row["season"]=='2016':
        	match_id_list.append(row["id"])
		    

    for row in deliveries_data:
    	if row["match_id"] in match_id_list:
    		if row["batting_team"] in extra_runs_data_dict:
    			extra_runs_data_dict[row["batting_team"]]+=int(row["extra_runs"])
    		else:
    			extra_runs_data_dict[row["batting_team"]]=int(row["extra_runs"])
	



colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue']
extra_runs_team_list=list(extra_runs_data_dict.keys())
extra_runs_list=list(extra_runs_data_dict.values())

# Plotting the chart
plt.figure(figsize=(15, 15))  # Set the figure size to 10x6 inches    
plt.bar(extra_runs_team_list,extra_runs_list,label=extra_runs_team_list,color=colors)    
plt.xticks(rotation=270,fontsize=10)           #Rotated the names on x-axis
plt.legend(bbox_to_anchor =(1, 1.15), ncol = 3)
plt.xlabel(r'Teams $\longrightarrow$')
plt.ylabel(r"Runs $\longrightarrow$")
plt.title("Extra runs given by team in year 2016")
plt.savefig("../figures/question_7_fig.png",bbox_inches='tight')    #Saving the figure in the given paths
plt.show()