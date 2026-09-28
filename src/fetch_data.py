import json
import csv
import urllib.request


def fetch_and_save_2026_data(output_path: str = "data/race_results.csv"):
    # Temporary buffer to store all parsed race results in memory before saving
    rows = []
    round_num = 1

    while True:
        url = f"https://api.jolpi.ca/ergast/f1/2026/{round_num}/results.json"
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0"}
        )

        try:
            # Open HTTP connection and parse raw JSON response into a Python dictionary
            with urllib.request.urlopen(req) as response:
                races = json.loads(response.read().decode())["MRData"][
                    "RaceTable"
                ]["Races"]
        except Exception:
            # Stop the loop on network failure or invalid response
            break

        if not races:
            break

        race = races[0]
        race_round = int(race["round"])
        for result in race["Results"]:
            rows.append([
                race_round,
                result["Driver"]["driverId"],  # "hamilton"
                result["Constructor"]["constructorId"],  # "ferrari"
                int(result["position"]),  # 1
            ])

        print(f"Downloaded round {round_num}: {race['raceName']}")
        round_num += 1

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["race_id", "driver_id", "constructor_id", "position"]
        )
        writer.writerows(rows)


if __name__ == "__main__":
    fetch_and_save_2026_data()
