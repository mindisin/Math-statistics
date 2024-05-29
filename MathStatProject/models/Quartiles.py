from constants import round_digits_count
class Quartiles:
    def __init__(self,
                 first_quantile = None,
                 second_quantile = None,
                 third_quantile = None):
        self.first_quantile = first_quantile
        self.second_quantile = second_quantile
        self.third_quantile = third_quantile

    def __str__(self) -> str:
        return (f'Квантили(25%, 50%, 75%): '
                f'{self.first_quantile.__round__(round_digits_count)}\t'
                f'{self.second_quantile.__round__(round_digits_count)}\t'
                f'{self.third_quantile.__round__(round_digits_count)}')