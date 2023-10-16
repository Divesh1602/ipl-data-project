import sys
from array import array
import matplotlib.pyplot as plt

# Adding the path so that it can find the desired file in the given path also
sys.path.append("/home/divesh/Desktop/Python/Projects/IPL-project/Programs")
from data import extracting_matches_data 

# Calling function from different file to get the data
matches_data_list=extracting_matches_data()

# Doing calculation to get the spicific data as per reuirements
matches_data_dict={}
i=1
while i<len(matches_data_list):
    
    if matches_data_list[i]["team1"] in matches_data_dict:
        if matches_data_list[i]["season"] in matches_data_dict[matches_data_list[i]["team1"]]:
            matches_data_dict[matches_data_list[i]["team1"]][matches_data_list[i]["season"]]+=1
        else:
            matches_data_dict[matches_data_list[i]["team1"]][matches_data_list[i]["season"]]=1
    else:
        matches_data_dict[matches_data_list[i]["team1"]]={}
        matches_data_dict[matches_data_list[i]["team1"]][matches_data_list[i]["season"]]=1

    if matches_data_list[i]["team2"] in matches_data_dict:
        if matches_data_list[i]["season"] in matches_data_dict[matches_data_list[i]["team2"]]:
            matches_data_dict[matches_data_list[i]["team2"]][matches_data_list[i]["season"]]+=1
        else:
            matches_data_dict[matches_data_list[i]["team2"]][matches_data_list[i]["season"]]=1
    else:
        matches_data_dict[matches_data_list[i]["team2"]]={}
        matches_data_dict[matches_data_list[i]["team2"]][matches_data_list[i]["season"]]=1
    i+=1



color_dict = {
    "2008": "Crimson",
    "2009": "Aquamarine",
    "2010": "Blue",
    "2011": "RoyalBlue",
    "2012": "GoldenRod",
    "2013": "LimeGreen",
    "2014": "Fuchsia",
    "2015": "Gold",
    "2016": "MediumOrchid",
    "2017": "Indigo"
}
for p_id,p_info in matches_data_dict.items():
    print(p_id)
    print(p_info)
# print(matches_data_dict)
# Plotting the bar graph
for team_name,team_data in matches_data_dict.items():
    bottom=0
    season=list(team_data.keys())
    matches_played=list(team_data.values())
    i=0
    while i < len(season):
        plt.bar(team_name,matches_played[i],bottom=bottom,label=season[i])
        bottom+=matches_played[i]
        i+=1


plt.legend(color_dict)
plt.title("Matches played by team in each season")
plt.xlabel(r"Teams $\longrightarrow$")
plt.ylabel(r"Matches played $\longrightarrow$")
plt.xticks(rotation=270)
plt.savefig("../figures/question_4_fig.png",bbox_inches='tight')  #Saving the image in different location
plt.show()