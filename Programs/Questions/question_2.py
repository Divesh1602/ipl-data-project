"""This program is ploting only top 10 batsmen by runs scored in RCB. """
import csv
import matplotlib.pyplot as plt

def execute():
    """This function is used to calculate the data needed to plot the graph """
    total_runs_scored = {}
    with open("../../Data/deliveries.csv", 'r', encoding="utf-8") as file:
        deliveries_data = csv.DictReader(file)
        for row in deliveries_data:
            if row["batting_team"] == "Royal Challengers Bangalore":
                if row["batsman"] in total_runs_scored:
                    total_runs_scored[row["batsman"]] += int(row["batsman_runs"])
                else:
                    total_runs_scored[row["batsman"]] = int(row["batsman_runs"])
    return total_runs_scored

def transform(total_runs_scored):
    """This function is used to Transform the data that is accepted by matplotlib """
    total_runs_scored_sorted = dict(
        sorted(total_runs_scored.items(),
        key=lambda item: item[1],
        reverse=True)
        )
    batsman_list = list(total_runs_scored_sorted.keys())[:10]
    runs_scored_list = list(total_runs_scored_sorted.values())[:10]
    plot(batsman_list, runs_scored_list)

def plot(batsman_list, runs_scored_list):
    """This function is used to plot the graph as per requirements """
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:blue', 'tab:orange', 'tab:green']
    plt.figure(figsize=(15, 10))  # Set the figure size to 10x6 inches
    plt.bar(batsman_list, runs_scored_list, label=batsman_list, color=colors)
    plt.xticks(rotation=270, fontsize=10)  # Rotated the names on x-axis
    plt.legend(bbox_to_anchor=(1, 1.15), ncol=3)
    plt.xlabel(r'Batsman $\longrightarrow$')
    plt.ylabel(r"Runs $\longrightarrow$")
    plt.title("Top 10 Batsman")
    plt.savefig(
    "../figures/question_2_fig.png",
    bbox_inches='tight'
    )  # Saving the figure in the given paths
    plt.show()

if __name__ == "__main__":
    data_dict = execute()
    transform(data_dict)
