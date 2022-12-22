import warnings
import pickle
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

warnings.filterwarnings("ignore")


app = FastAPI()

model = pickle.load(open('modelrffinal.pickle', 'rb'))


class Data(BaseModel):
    population_density: float
    retail_and_recreation_percent_change_from_baseline: float
    grocery_and_pharmacy_percent_change_from_baseline: float
    parks_percent_change_from_baseline: float
    transit_stations_percent_change_from_baseline: float
    workplaces_percent_change_from_baseline: float
    residential_percent_change_from_baseline: float
    Completeness_pct: float
    Administered_Dose1_Recip: float
    Administered_Dose1_Pop_Pct: float
    Administered_Dose1_Recip_12Plus: float
    Administered_Dose1_Recip_12PlusPop_Pct: float
    Administered_Dose1_Recip_18Plus: float
    Administered_Dose1_Recip_18PlusPop_Pct: float
    Administered_Dose1_Recip_65Plus: float
    Administered_Dose1_Recip_65PlusPop_Pct: float
    Series_Complete_Pop_Pct_SVI: float
    Series_Complete_12PlusPop_Pct_SVI: float
    Series_Complete_18PlusPop_Pct_SVI: float
    Series_Complete_65PlusPop_Pct_SVI: float
    Series_Complete_Pop_Pct_UR_Equity: float
    Series_Complete_12PlusPop_Pct_UR_Equity: float
    Series_Complete_18PlusPop_Pct_UR_Equity: float
    Series_Complete_65PlusPop_Pct_UR_Equity: float


@app.post("/predict")
def predict(data: Data):
    input = [values for values in data.dict().values()]
    results = model.predict([input])  # should be a 2d array
    return {'Risk analysis': results[0]}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, host="127.0.0.1", port=5000)
