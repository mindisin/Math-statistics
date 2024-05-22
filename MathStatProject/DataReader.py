import pandas as pd
from pandas import Series
from constants import filepath


def get_data():
    file_path = filepath

    # Чтение данных из CSV файла с указанным разделителем
    data = pd.read_csv(file_path, delimiter=';')

    new_column_data = []

    item = data["NObeyesdad"]

    for i in range(len(data)):
        if item[i] == "Insufficient_Weight":
            new_column_data.append(-1)
        elif item[i] == "Normal_Weight":
            new_column_data.append(0)
        elif item[i] == "Overweight_Level_I":
            new_column_data.append(1)
        elif item[i] == "Overweight_Level_II":
            new_column_data.append(2)
        elif item[i] == "Obesity_Type_I":
            new_column_data.append(3)
        elif item[i] == "Obesity_Type_II":
            new_column_data.append(4)
        elif item[i] == "Obesity_Type_III":
            new_column_data.append(5)

    desired_columns = ["Gender", "Age", "Weight"]
    new_data = data.loc[:, desired_columns]
    new_data["Obesity"] = new_column_data

    return new_data

def get_data_info(data):
    # количество наблюдений
    observations_number = data.shape[0]

    # количество переменных
    variables_number = data.shape[1]

    # типы данных
    types = data.dtypes

    print("Количество наблюдений: ", observations_number, '\n',
          "Количество переменных", variables_number, '\n',
          "Типы данных: ", types)

    # Поиск пустых значений
    empty_values = data[data.isnull().any(axis=1)]

    if empty_values.empty:
        print("Пустых значений нет")
    else:
        # Вывод найденных пустых значений
        print("Пустые значения в данных:")
        print(empty_values)

        # Удаление всех записей с пустыми значениями
        cleaned_data = data.dropna()

        # Вывод количества записей до и после удаления пустых значений
        print("\nКоличество записей до удаления пустых значений:", len(data))
        print("Количество записей после удаления пустых значений:", len(cleaned_data))

def prepare_data_hypo(data: Series):
    above_equals_trirty = []
    lower_trirty = []
    new_data = pd.DataFrame()

    for item in data:
        if item >= 30.0:
            above_equals_trirty.append(item)
        else:
            lower_trirty.append(item)

    return lower_trirty, above_equals_trirty