from typing import Optional

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/all-countries")
def execute_man_power_all_countries_spider():
    os.system("python3 run_spider_man_power_all_countries.py")
    return {"Status": "Countries has been scraped"}


@app.post("/{id}")
def execute_man_power_country_by_id_spider(id: str):
    os.system(f"python3 run_spider_man_power_country_by_id.py {id}")
    return {"Status": f"Country with id: {id} has been scraped"}
