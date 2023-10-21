"""This program is ploting a chart of number of umpires by in IPL by country """
import csv
import matplotlib.pyplot as plt


def execute():
    """This function is used to calculate the data needed to plot the graph """
    umpires_country_dict = {}
    with open("../../Data/umpires.csv", 'r', encoding='utf-8') as file:
        umpires_data = csv.DictReader(file)
        for row in umpires_data:
            if row[" country"] != " India":
                if row[" country"] in umpires_country_dict:
                    umpires_country_dict[row[" country"]] += 1
                else:
                    umpires_country_dict[row[" country"]] = 1
        return umpires_country_dict


def transform(umpires_country_dict):
    """
    This function is used to Transform the
    data that is accepted by matplotlib
    """
    umpires_country = list(umpires_country_dict.keys())
    umpires_count = list(umpires_country_dict.values())
    plot(umpires_country, umpires_count)


def plot(umpires_country, umpires_count):
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
    'tab:green'
    ]
    plt.figure(figsize = (15,8))
    plt.bar(
    umpires_country,umpires_count,
    label = umpires_country,
    color = colors
    )  #Creating the chart
    plt.xlabel(r"Country $\longrightarrow$")
    plt.ylabel(r"Number of umpires $\longrightarrow$")
    plt.legend()
    plt.title("Count of umpire")
    plt.savefig(
    "../figures/question_3_fig.png", 
    bbox_inches = 'tight'
    )  #Saving the image in different location
    plt.show()

if __name__ == "__main__":
    data_dict = execute()
    transform(data_dict)
