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
	if matches_data_list[j]["season"]=='2015':
		match_id_list.append(matches_data_list[j]["id"])
	j+=1


economy_data_dict={}
i=1
while i<len(deliveries_data_list):
   
	if deliveries_data_list[i]["match_id"] in match_id_list:
		if deliveries_data_list[i]["bowler"] in economy_data_dict:
			economy_data_dict[deliveries_data_list[i]["bowler"]][0]+=int(deliveries_data_list[i]["total_runs"])
			economy_data_dict[deliveries_data_list[i]["bowler"]][1]+=1
			economy_data_dict[deliveries_data_list[i]["bowler"]][2]=economy_data_dict[deliveries_data_list[i]["bowler"]][1]//6
			if economy_data_dict[deliveries_data_list[i]["bowler"]][2]!=0:
				economy_data_dict[deliveries_data_list[i]["bowler"]][3]=round(economy_data_dict[deliveries_data_list[i]["bowler"]][0]/economy_data_dict[deliveries_data_list[i]["bowler"]][2],1)
			else:
				economy_data_dict[deliveries_data_list[i]["bowler"]][3]=0.0
		
		else:
			   economy_data_dict[deliveries_data_list[i]["bowler"]]=[int(deliveries_data_list[i]["total_runs"]),1,0,0]
				
		
	i+=1


sorted_economy_data_dict=dict(sorted(economy_data_dict.items(), key=lambda item: item[1][3]))
bowlers_list=list(sorted_economy_data_dict.keys())[:10]
economy_list=[]
i=0
for bowler,bowling_data in sorted_economy_data_dict.items():
	economy_list.append(bowling_data[3])
	i+=1
	if(i==10):
		break

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue', 'tab:orange', 'tab:green']



# Plotting the chart
plt.figure(figsize=(15, 15))  # Set the figure size to 10x6 inches    
plt.bar(bowlers_list,economy_list,label=bowlers_list,color=colors)    
plt.xticks(rotation=270,fontsize=10)           #Rotated the names on x-axis
plt.legend(bbox_to_anchor =(1, 1.15), ncol = 3)
plt.xlabel(r'Bowlers $\longrightarrow$')
plt.ylabel(r"Economy $\longrightarrow$")
plt.title("Top 10 Bowler in year 2015")
plt.savefig("../figures/question_8_fig.png",bbox_inches='tight')    #Saving the figure in the given paths
plt.show()