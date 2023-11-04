import pickle
import uvicorn
from fastapi import FastAPI,HTTPException,status,Request
from fastapi.templating import Jinja2Templates
from schemas import Data,PredictOutput
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
app = FastAPI()

origins = ["*"]  # Replace "*" with the specific origins you want to allow, or use a list of allowed domains

app.mount("/static",StaticFiles(directory="static"),name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Set this to True if your API supports credentials (e.g., cookies)
    allow_methods=["*"],     # You can specify the HTTP methods you want to allow
    allow_headers=["*"],     # You can specify the HTTP headers you want to allow
)

MODEL = pickle.load(open("model.pkl","rb"))

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request},status_code=200)

@app.post("/model",response_model=PredictOutput)
def predict(body:Data):
    try:
        res = MODEL.predict([[body.temperature,body.humidity,body.tvoc,body.eco2,body.rawH2,body.raw_ethanol,body.pressure,body.nc_05]])
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