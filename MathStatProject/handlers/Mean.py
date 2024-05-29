from handlers.SampleSize import get_sample_size

def get_mean(data):
    return sum(data) / get_sample_size(data)