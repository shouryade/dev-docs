## Working with ML Models using FastAPI

The code in app.py uses a model called `modelrffinal.pickle` which predicts the risk of a person catching COVID-19.  
Working with ML Models in FastAPI is quite easy, although some important things which are needed to be checked are :

[x] The framework used by the model is installed as a dependency in the project. (Check Pipfile)  
[x] Data class is instantiated for feeding only the required data to the model after converting it into 2D array from form data.  
[x] Once form data is received from client, pass only the values in the 2D array from the key-value pair received.  
[x] Use `[[]]` for workaround of 2D arrays, better not use reshape.
