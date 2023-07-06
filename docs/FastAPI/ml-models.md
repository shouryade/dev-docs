## Working with ML Models using FastAPI

Often for projects, where I am using FastAPI, a simple model returns some predicted output after taking some inputs.
In this case processing/returning the data becomes hard.

Here in this example code, `modelrffinal.pickle` is a model which predicts the risk of a person catching COVID-19.

```py title="app.py" linenums="1" hl_lines="10 11 12 16 17"
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
    # add other features here

@app.post("/predict")
def predict(data: Data):
    input = [values for values in data.dict().values()]
    results = model.predict([input])  # should be a 2D array
    return {'Risk analysis': results[0]}
```

Working with ML Models in FastAPI is quite easy, although some important things which are needed to be checked are :

- The framework used by the model is installed as a dependency in the project. (Check Pipfile)
- Data class is instantiated for feeding only the required data to the model after converting it into 2D array from form data.
- Once form data is received from client, pass only the values in the 2D array from the key-value pair received.
- Use `[[]]` for workaround of 2D arrays, better not use reshape.
