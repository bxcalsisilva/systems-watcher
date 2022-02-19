from os import sep
from pathlib import Path
from datetime import date, timedelta
import pandas as pd


data_dir = Path("../data/SFCR_Aplicada")

locations = ["PUCP", "UNAJ", "UNI", "UNJBG", "UNSA", "UNTRM"]

systems = [
    {"technology": "PERC", "id": "SFCR1"},
    {"technology": "HIT", "id": "SFCR2"},
    {"technology": "CIGS", "id": "SFCR3"},
]

start_dt = date(2020, 1, 1)
end_dt = date.today() - timedelta(days=1)

print("start_dt", start_dt, "end_dt", end_dt)

for location in locations:
    for system in systems:
        print(location, system["technology"], system["id"])

        data_system = pd.DataFrame()

        dt = start_dt
        while dt <= end_dt:

            filename = f"{system['id']}-{system['technology']}-{location}_{str(dt).replace('-','_')}.csv"
            filepath = data_dir / f"{location}/{dt.year}/{str(dt)[:7].replace('-','_')}"

            try:
                df = pd.read_csv((filepath / filename).resolve(), header=None, sep=";")

                data_system = pd.concat([data_system, df], ignore_index=True)
            except:
                print("no file found for", dt, "filepath", filename)
                dt += timedelta(days=1)
                continue

            dt += timedelta(days=1)

        data_system.to_csv(
            f"../data/aggregated/{location}_{system['technology']}.csv",
            index=False,
        )
