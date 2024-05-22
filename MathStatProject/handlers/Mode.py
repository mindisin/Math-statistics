from numpy import ndarray
import numpy as np

def get_mode(data):
    values, counts = np.unique(data, return_counts=True)

    if len(values) == len(data):
        return None

    mode_indexes = np.argwhere(counts == np.max(counts))

    return values[mode_indexes].flatten()