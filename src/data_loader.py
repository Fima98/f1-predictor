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

    #   WHAT IT DOES:
    #   Loads numerical or structured data from a text/CSV file into a NumPy array.

    # PARAMETERS:
    #   - filepath (str / Path): Path to the target text or CSV file.
    #   - delimiter (str): Character used to separate values in each row (e.g., ',').
    #   - skip_header (int): Number of lines to skip at the beginning of the file (e.g., 1 for header row).
    #   - dtype (dtype / list): Target data type for the returned array or per-column data structure.
    #   - encoding (str): Text encoding used to read the file (e.g., 'utf-8').

    # HOW IT WORKS:
    #   It opens the file line by line, splits each line using the specified delimiter, ignores
    #   the header row, converts each column to its designated data type, and packs the entire
    #   dataset into a structured 1D NumPy array.

    return data
