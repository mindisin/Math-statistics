from handlers.Mean import get_mean
from handlers.SampleSize import get_sample_size


def get_no_displaced_dispersion(data):
    mean = get_mean(data)
    n = get_sample_size(data)
    return sum((data_item - mean)**2 for data_item in data) / (n - 1)