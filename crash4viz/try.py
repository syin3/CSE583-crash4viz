from matplotlib import pyplot as plt

plot_sink = None

plt.bar([2013, 2014, 2015, 2016, 2017], [36685, 40638, 44471, 48525, 47238])
plt.title("Accident counts by year")
plt.ylabel("Accident counts")
plt.xlabel("Year")

if plot_sink is None:
    plot_sink = '../outputs'

plt.savefig(plot_sink + '/year_plot.png')