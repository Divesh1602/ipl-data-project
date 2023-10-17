import sys
import matplotlib.pyplot as plt

# Adding the path so that it can find the desired file in the given path also
sys.path.append("/home/divesh/Desktop/Python/Projects/IPL-project/Programs")
from data import extracting_matches_data,extracting_deliveries_data

# Calling function from different file to get the data
matches_data_list=extracting_matches_data()
deliveries_data_list=extracting_deliveries_data()
# Doing calculation to get the spicific data as per reuirements
match_id_list=[]
j=1 
while j<len(matches_data_list):
	if matches_data_list[j]["season"]=='2016':
		match_id_list.append(matches_data_list[j]["id"])
	j+=1

extra_runs_data_dict={}
i=1
while i<len(deliveries_data_list):

	if deliveries_data_list[i]["match_id"] in match_id_list:
		if deliveries_data_list[i]["batting_team"] in extra_runs_data_dict:
			extra_runs_data_dict[deliveries_data_list[i]["batting_team"]]+=int(deliveries_data_list[i]["extra_runs"])
		else:
			extra_runs_data_dict[deliveries_data_list[i]["batting_team"]]=int(deliveries_data_list[i]["extra_runs"])
		
	i+=1

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