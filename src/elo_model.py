import numpy as np


def calculate_elo(data: np.ndarray, initial_elo: float = 1500.0, k_factor: float = 32.0) -> dict[str, float]:
    drivers = np.unique(data["driver_id"])
    elo = {driver: initial_elo for driver in drivers}

    races = np.unique(data["race_id"])
    for race_id in races:
        race_data = data[data["race_id"] == race_id]
        race_drivers = race_data["driver_id"]
        positions = race_data["position"]
        n = len(race_drivers)

        r = np.array([elo[d] for d in race_drivers])
        r_vertical = r.reshape(n, 1)

        positions_vertical = positions.reshape(n, 1)

        e_matrix = 1.0 / (1.0 + 10.0 ** ((r - r_vertical) / 400.0))
        s_matrix = (positions_vertical < positions).astype(float)

        e_i = np.sum(e_matrix, axis=1) - 0.5
        s_i = np.sum(s_matrix, axis=1)

        new_r = r + (k_factor / (n - 1)) * (s_i - e_i)

        for driver, new_rating in zip(race_drivers, new_r):
            elo[driver] = new_rating

    return elo
