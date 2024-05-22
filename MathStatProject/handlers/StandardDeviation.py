from handlers.DisplacedDispersion import get_displaced_dispersion

def get_standard_deviation(data):
    return get_displaced_dispersion(data) ** 0.5