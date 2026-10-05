import csv
import os
from data_loader import load_race_data
from elo_model import calculate_elo


race_data = load_race_data("data/race_results.csv")
elo_ratings = calculate_elo(race_data)

os.makedirs("data", exist_ok=True)
with open("data/drivers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["driver_id", "elo"])
    for driver, rating in elo_ratings.items():
        writer.writerow([driver, round(rating, 2)])
