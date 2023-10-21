"""
This program is ploting a stacked bar chart of ...
    number of games played
    by team
    by season
 """
import csv
import matplotlib.pyplot as plt

def execute():
    """This function is used to calculate the data needed to plot the graph """
    matches_data_dict = {}
    with open("../../Data/matches.csv",'r',encoding='utf-8') as file:
        matches_data = csv.DictReader(file)
        for row in matches_data:
            if row["team1"] in matches_data_dict:
                if row["season"] in matches_data_dict[row["team1"]]:
                    matches_data_dict[row["team1"]][row["season"]] += 1
                else:
                    matches_data_dict[row["team1"]][row["season"]] = 1
            else:
                matches_data_dict[row["team1"]] = {}
                matches_data_dict[row["team1"]][row["season"]] = 1

            if row["team2"] in matches_data_dict:
                if row["season"] in matches_data_dict[row["team2"]]:
                    matches_data_dict[row["team2"]][row["season"]] += 1
                else:
                    matches_data_dict[row["team2"]][row["season"]] = 1
            else:
                matches_data_dict[row["team2"]] = {}
                matches_data_dict[row["team2"]][row["season"]] = 1
    return matches_data_dict

def plot(matches_data_dict):
    """This function is used to plot the graph as per requirements """
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
    color_dict_keys = list(color_dict.keys())
    color_dict_values = list(color_dict.values())
    i = 0
    while i < len(color_dict_values):
        plt.bar(0,0,color = color_dict_values[i],label = color_dict_keys[i])
        i += 1

    # Plotting the bar graph
    for team_name,team_data in matches_data_dict.items():
        bottom = 0
        team_data_keys = list(team_data.keys())
        team_data_keys.sort()
        sorted_team_data_dict = {i: team_data[i] for i in team_data_keys}
        season = list(sorted_team_data_dict.keys())
        matches_played = list(sorted_team_data_dict.values())
        i = 0
        while i < len(season):
            plt.bar(
            team_name,matches_played[i],
            bottom = bottom,
            label = season[i],
            color = color_dict[season[i]])
            bottom += matches_played[i]
            i += 1

    plt.legend(color_dict.keys())
    plt.title("Matches played by team in each season")
    plt.xlabel(r"Teams $\longrightarrow$")
    plt.ylabel(r"Matches played $\longrightarrow$")
    plt.xticks(rotation = 270)
    plt.savefig(
    "../figures/question_4_fig.png",
    bbox_inches = 'tight'
    )  #Saving the image in different location
    plt.show()

if __name__ == "__main__":
    data_dict = execute()
    plot(data_dict)
