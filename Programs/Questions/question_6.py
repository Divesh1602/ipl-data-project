import sys
import matplotlib.pyplot as plt


# Adding the path so that it can find the desired file in the given path also
sys.path.append("/home/divesh/Desktop/Python/Projects/IPL-project/Programs")
from data import extracting_matches_data 

# Calling function from different file to get the data
matches_data_list=extracting_matches_data()

# Doing calculation to get the spicific data as per reuirements
winner_team_dict={}
i=1
while i<len(matches_data_list):
    
    if matches_data_list[i]["result"] == "normal":
        if matches_data_list[i]["winner"] in winner_team_dict:
            if matches_data_list[i]["season"] in winner_team_dict[matches_data_list[i]["winner"]]:
                winner_team_dict[matches_data_list[i]["winner"]][matches_data_list[i]["season"]]+=1
            else:
                winner_team_dict[matches_data_list[i]["winner"]][matches_data_list[i]["season"]]=1
        else:
            winner_team_dict[matches_data_list[i]["winner"]]={}
            winner_team_dict[matches_data_list[i]["winner"]][matches_data_list[i]["season"]]=1

   
    i+=1



color_dict = {
    "2008": "b",
    "2009": "g",
    "2010": "r",
    "2011": "c",
    "2012": "m",
    "2013": "y",
    "2014": "k",
    "2015": "blueviolet",
    "2016": "orange",
    "2017": "dimgray"
}



# labeling the legends
color_dict_keys=list(color_dict.keys())
color_dict_values=list(color_dict.values())
i=0
while i<len(color_dict_values):
    plt.bar(0,0,color=color_dict_values[i],label=color_dict_keys[i])
    i+=1

# Plotting the bar graph
for winner_team_name,team_data in winner_team_dict.items():
    bottom=0
    team_data_keys=list(team_data.keys())
    team_data_keys.sort()
    sorted_team_data_dict={i: team_data[i] for i in team_data_keys}
    season=list(sorted_team_data_dict.keys())
    matches_played=list(sorted_team_data_dict.values())
    i=0
    while i < len(season):
        plt.bar(winner_team_name,matches_played[i],bottom=bottom,label=season[i],color=color_dict[season[i]])
        bottom+=matches_played[i]
        i+=1


plt.legend(color_dict.keys())
plt.title("Games won by team in each season")
plt.xlabel(r"Teams $\longrightarrow$")
plt.ylabel(r"Matches played $\longrightarrow$")
plt.xticks(rotation=270)
plt.savefig("../figures/question_6_fig.png",bbox_inches='tight')  #Saving the image in different location
plt.show()



