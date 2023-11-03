import pickle
import uvicorn
from fastapi import FastAPI,HTTPException,status,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas import Data,PredictOutput

app = FastAPI()
MODEL = pickle.load(open("model.pkl","rb"))

templates = Jinja2Templates(directory="templates")


@app.post("/model",response_model=PredictOutput)
def predict(body:Data):
    try:
        res = MODEL.predict([[body.temparature,body.humidity,body.tvoc,body.eco2,body.rawH2,body.raw_ethanol,body.pressure,body.nc_05]])
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail="server error")
    return {"ans":int(res[0])}

@app.exception_handler(HTTPException)
async def custom_404(request:Request,exec):
    return templates.TemplateResponse("404.html",{"request":request},status_code=404)

@app.get("/{path:path}")
async def not_found(path: str):
    raise HTTPException(status_code=404, detail="Not Found")

if __name__ == "__main__":
    uvicorn.run(app="main:app",port=8080,reload=True)