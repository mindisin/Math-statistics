from handlers.SampleSize import get_sample_size
def get_first_quantile(data):
    n = get_sample_size(data)
    return data[n // 4] if n % 4 != 0 else (data[n // 4 + 1] + data[n // 4]) / 2

def get_third_quantile(data):
    n = get_sample_size(data)
    return data[(3 * n) // 4] if n % 4 != 0 else (data[(3 * n) // 4 + 1] + data[(3 * n) // 4]) / 2
