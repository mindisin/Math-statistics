from handlers.Mean import get_mean
from handlers.SampleSize import get_sample_size

def get_displaced_dispersion(data):
    return sum((data_item - get_mean(data))**2 for data_item in data) / get_sample_size(data)