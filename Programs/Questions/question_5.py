"""This program is ploting number of matches played per year for all the years in IPL. """
import csv
import matplotlib.pyplot as plt

def execute():
    """This function is used to calculate the data needed to plot the graph """
    matches_data_dict={}
    with open("../../Data/matches.csv",'r',encoding='utf-8') as file:
        matches_data=csv.DictReader(file)
        for row in matches_data:
            if row["season"] in matches_data_dict:
                matches_data_dict[row["season"]]+=1
            else:
                matches_data_dict[row["season"]]=1
    return matches_data_dict

def transform(matches_data_dict):
    """
    This function is used to Transform the
    data that is accepted by matplotlib
    """
    seasons=list(dict(sorted(matches_data_dict.items())).keys())
    number_of_matches=list(dict(sorted(matches_data_dict.items())).values())
    plot(seasons,number_of_matches)


def plot(seasons,number_of_matches):
    """This function is used to plot the graph as per requirements """
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
    plt.figure(figsize=(10,8))
    plt.bar(seasons,number_of_matches,color=color_dict.values(),label=seasons)
    plt.legend(ncol=3)
    plt.title("Matches played by team in each season")
    plt.xlabel(r"seasons $\longrightarrow$")
    plt.ylabel(r"Matches played $\longrightarrow$")
    plt.savefig(
    "../figures/question_5_fig.png",
    bbox_inches='tight'
    )  #Saving the image in different location
    plt.show()

if __name__ == "__main__":
    data_dict = execute()
    transform(data_dict)
