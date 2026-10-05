import numpy as np


def load_race_data(filepath: str) -> np.ndarray:

    dtype = [
        ('race_id', 'i4'),      # 32-bit signed integer (4-byte int)
        ('driver_id', 'U20'),   # Unicode string (up to 20 characters)
        ('constructor_id', 'U20'),
        ('position', 'i4')
    ]

    data = np.genfromtxt(
        filepath,
        delimiter=',',
        skip_header=1,
        dtype=dtype,
        encoding='utf-8'
    )
    return data


if __name__ == '__main__':
    print(load_race_data('data/race_results.csv'))
