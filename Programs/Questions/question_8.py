"""This program is ploting extra runs conceded per team in the year 2016 """
import csv
import matplotlib.pyplot as plt

def execute():
    """This function is used to calculate the data needed to plot the graph """
    economy_data_dict = {}
    with open(
    	"../../Data/matches.csv",
    	'r',
    	encoding = 'utf-8') as file1,open(
    	"../../Data/deliveries.csv",
    	'r',
    	encoding = 'utf-8') as file2:
        matches_data = csv.DictReader(file1)
        deliveries_data = csv.DictReader(file2)
        match_id_list = []
        for row in matches_data:
            if row["season"] == '2015':
                match_id_list.append(row["id"])

        for row in deliveries_data:
            if row["match_id"] in match_id_list:
                if row["bowler"] in economy_data_dict:
                    economy_data_dict[row["bowler"]][0] += int(row["total_runs"])
                    economy_data_dict[row["bowler"]][1] += 1
                    economy_data_dict[row["bowler"]][2] = economy_data_dict[row["bowler"]][1] // 6
                    if economy_data_dict[row["bowler"]][2] != 0:
                        economy_data_dict[row["bowler"]][3] = round(
                        	economy_data_dict[row["bowler"]][0] / economy_data_dict[row["bowler"]][2],
                        	1)
                    else:
                        economy_data_dict[row["bowler"]][3] = 0.0
                else:
                    economy_data_dict[row["bowler"]] = [int(row["total_runs"]), 1, 0, 0]
    return economy_data_dict

def transform(economy_data_dict):
    """
    This function is used to Transform the
    data that is accepted by matplotlib
    """
    sorted_economy_data_dict = dict(
    	sorted(economy_data_dict.items(),
    	key = lambda item: item[1][3]))
    bowlers_list = list(sorted_economy_data_dict.keys())[:10]
    economy_list = []
    i = 0
    for _,bowling_data in sorted_economy_data_dict.items():
        economy_list.append(bowling_data[3])
        i += 1
        if i == 10:
            break
    plot(bowlers_list,economy_list)



def plot(bowlers_list,economy_list):
    """This function is used to plot the graph as per requirements """
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue', 'tab:orange', 'tab:green']
    plt.figure(figsize = (15, 15))  # Set the figure size to 10x6 inches
    plt.bar(bowlers_list,economy_list,label = bowlers_list,color = colors)
    plt.xticks(rotation = 270,fontsize = 10)           #Rotated the names on x-axis
    plt.legend(bbox_to_anchor =(1, 1.15), ncol = 3)
    plt.xlabel(r'Bowlers $\longrightarrow$')
    plt.ylabel(r"Economy $\longrightarrow$")
    plt.title("Top 10 Bowler in year 2015")
    plt.savefig(
    "../figures/question_8_fig.png",
    bbox_inches = 'tight'
    )    #Saving the figure in the given paths
    plt.show()

if __name__ == "__main__":
    data_dict = execute()
    transform(data_dict)
