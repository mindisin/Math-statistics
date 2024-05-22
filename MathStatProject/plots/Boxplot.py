import matplotlib.pyplot as plt

def build_boxplot(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot(data,
               showfliers=True,
               patch_artist=True,
               medianprops={"linewidth": 2, "color": "red"},
               flierprops={"markersize": 5})
    ax.set_ylim(min(data), max(data))
    ax.grid()

    # Настройка меток и заголовка
    ylabel = ''
    if data.name == "Weight":
        ylabel = "kilograms"
    elif data.name == "Age":
        ylabel = "years"

    plt.xlabel(data.name)
    plt.ylabel(ylabel)
    plt.title('Боксплот')

    plt.show()