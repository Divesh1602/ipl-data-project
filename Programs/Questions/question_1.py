"""
This program is ploting a chart of the total runs 
scored by each teams over the history of IPL
"""

import csv
import matplotlib.pyplot as plt

def execute():
    """This function is used to calculate the data needed to plot the graph """
    total_runs_scored = {}
    with open("../../Data/deliveries.csv",mode = 'r',encoding="utf-8") as file:
        deliveries_data = csv.DictReader(file)
        for row in deliveries_data:
            if row["batting_team"] in total_runs_scored:
                total_runs_scored[row["batting_team"]] += int(row["total_runs"])
            else:
                total_runs_scored[row["batting_team"]] = int(row["total_runs"])
    return total_runs_scored

def transform(total_runs_scored):
    """This function is used to Transform the data that is accepted by matplotlib """
    team_names_list = list(total_runs_scored.keys())
    runs_scored_list = list(total_runs_scored.values())
    plot(team_names_list,runs_scored_list)


def plot(team_names_list,runs_scored_list):
    """This function is used to plot the graph as per requirements """
    colors = [
    'b', 
    'g',
    'r',
    'c',
    'm',
    'y',
    'k',
    'tab:blue',
    'tab:orange',
    'tab:green',
    'tab:red',
    'tab:purple',
    'tab:brown',
    'tab:pink'
    ]
    plt.figure(figsize = (20 ,15))  # Set the figure size to 10x6 inches
    plt.bar(team_names_list,runs_scored_list,label = team_names_list,color = colors)
    plt.xticks(rotation = 270,fontsize = 10)           #Rotated the names on x-axis
    plt.legend(bbox_to_anchor = (0.40, 1.15), ncol = 3)
    plt.xlabel(r'Teams $\longrightarrow$')
    plt.ylabel(r"Runs $\longrightarrow$")
    plt.title("Total runs scored by teams")
    plt.savefig(
    "../figures/question_1_fig.png",
    bbox_inches = 'tight'
    )    #Saving the figure in the given paths
    plt.show()

if __name__ == "__main__":
    data_dict=execute()
    transform(data_dict)
