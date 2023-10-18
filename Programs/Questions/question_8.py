import csv
import matplotlib.pyplot as plt


# Doing calculation to get the spicific data as per reuirements
economy_data_dict={}
with open("../../Data/matches.csv",'r') as file1,open("../../Data/deliveries.csv",'r') as file2:

    matches_data=csv.DictReader(file1)
    deliveries_data=csv.DictReader(file2)
    match_id_list=[]
    for row in matches_data:
        if row["season"]=='2015':
        	match_id_list.append(row["id"])
		    

    for row in deliveries_data:
    	if row["match_id"] in match_id_list:
    		if row["bowler"] in economy_data_dict:
    			economy_data_dict[row["bowler"]][0]+=int(row["total_runs"])
    			economy_data_dict[row["bowler"]][1]+=1
    			economy_data_dict[row["bowler"]][2]=economy_data_dict[row["bowler"]][1]//6
    			if economy_data_dict[row["bowler"]][2]!=0:
    				economy_data_dict[row["bowler"]][3]=round(economy_data_dict[row["bowler"]][0]/economy_data_dict[row["bowler"]][2],1)
    			else:
    				economy_data_dict[row["bowler"]][3]=0.0
    		else:
    			economy_data_dict[row["bowler"]]=[int(row["total_runs"]),1,0,0]
	




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