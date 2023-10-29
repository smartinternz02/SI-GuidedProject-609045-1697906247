import pickle
import uvicorn
from fastapi import FastAPI,HTTPException,status
from schemas import Data,PredictOutput

app = FastAPI()
MODEL = pickle.load(open("model.pkl","rb"))

@app.post("/model",response_model=PredictOutput)
def predict(body:Data):
    try:
        res = MODEL.predict([[body.temparature,body.humidity,body.tvoc,body.eco2,body.rawH2,body.raw_ethanol,body.pressure,body.nc_05]])
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail="server error")
    return {"ans":int(res[0])}
if __name__ == "__main__":
    uvicorn.run(app="main:app",port=8080,reload=True)