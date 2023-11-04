from pydantic import BaseModel

class Data(BaseModel):
    temperature: float
    humidity: float
    tvoc: float
    eco2: float
    rawH2: float
    raw_ethanol: float
    pressure: float
    nc_05: float

class PredictOutput(BaseModel):
    ans:int