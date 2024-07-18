import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(data, x, hue, title="", xlabel="", ylabel=""):
    plt.figure(figsize = (8,8))
    splot = sns.countplot(data = data, x=x, palette='GnBu', hue=hue)
    sns.set_style('ticks')
    total = float(len(data))
    for p in splot.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height() / total)
        x = p.get_x() + p.get_width()
        y = p.get_height()
        splot.annotate(percentage, (x,y), ha = 'center', va = 'center')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show() 