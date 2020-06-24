# importing needed libraries
import pandas as pd
import seaborn as sns

# assigning url of dataset to variable 'csv_url'
csv_url = 'https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv'
read_data = pd.read_csv(csv_url)  # reading dataset

# saving dataset as csv for use in tableau
save_data = read_data.to_csv('data.csv')
print(read_data)  # checking the data

# creating pivot table
pivot_table = read_data.pivot_table(
    index='continent', columns='year', values='lifeExp')
print(pivot_table)

data_plot = sns.heatmap(pivot_table)  # plotting heatmap
plot = data_plot.get_figure()  # getting plotted figure for saving
plot.savefig('Seaborn_HeatMap.png')  # saving plot
