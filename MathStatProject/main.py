from Hypothesis.HypothesisTesting import hypothesis_testing_param
from constants import round_digits_count
from handlers.Correlation import get_correlation
from handlers.DataHandler import handle_data
from DataReader import get_data, get_data_info
from handlers.Outliers import get_outliers
from plots.Boxplot import build_boxplot
from plots.Hist import plot_hist
from plots.LinearRegression import plot_linear_regression
from plots.Scatter import scatter_plot

data = get_data()
get_data_info(data)

print("\n \nAGE INFO")
print(handle_data(data["Age"]))

print("\n \nWEIGHT INFO")
print(handle_data(data["Weight"]))

print(f'\n\nКоэффициент корреляции: {round(get_correlation(data["Age"], data["Obesity"]), round_digits_count)}')

print(f'Выбросы:\n{get_outliers(data["Age"])}')

plot_linear_regression(data["Age"], data["Weight"])

plot_hist(data["Weight"], int(134/5))

build_boxplot(data["Weight"])

scatter_plot(data["Age"], data["Weight"])
hypothesis_testing_param(data["Weight"], 65)



#hypothesis_testing_distribution(data['Age'])
