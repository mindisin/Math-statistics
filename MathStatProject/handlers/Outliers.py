from handlers.Quantiles import get_third_quantile, get_first_quantile


def get_outliers(data):
    third_quantile = get_third_quantile(data)
    first_quantile = get_first_quantile(data)

    interquartile_range = third_quantile - first_quantile

    lower_bound = first_quantile - 1.5 * interquartile_range
    upper_bound = third_quantile + 1.5 * interquartile_range

    print("\n\nНижняя граница:", lower_bound)
    print("Верхняя граница:", upper_bound)

    return data[(data < lower_bound) | (data > upper_bound)]