
# Detect Smoke With The Help Of IOT Data And Trigger A Fire Alarm

Detect Smoke With The Help Of IOT Data And Trigger A Fire Alarm using
Machine Learning This machine learning project aims to use IoT data to
enhance smoke detection and fire alarm triggering for improved safety and
security. It addresses the limitations of traditional fire detection systems,focusing on early detection, remote monitoring, and data-driven decision
making. The project aims to make fire alarm systems more effective,
adaptable in various settings, including residential, commercial, industrial,
and public spaces. The objectives include developing machine learning
models, assessing their performance, confirming the solution's effectiveness.

## API Reference
FastAPI
https://fastapi.tiangolo.com/

#### Get all items
$ pip install fastapi

$ pip install "uvicorn[standard]

---> 100%
```http
Create a file main.py with:

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

Description                |
|FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

The key features are:

Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
Fast to code: Increase the speed to develop features by about 200% to 300%. 
Fewer bugs: Reduce about 40% of human (developer) induced errors. 
Intuitive: Great editor support. Completion everywhere. Less time debugging.
Easy: Designed to be easy to use and learn. Less time reading docs.
Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
Robust: Get production-ready code. With automatic interactive documentation.
Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema. 
 . 

from fastapi import FastAPI, HTTPException, Depends, Header

app = FastAPI()

API_KEY = "your_secret_api_key"

# Dependency to validate the API key
def validate_api_key(api_key: str = Header(...)):

    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

# Use the dependency to protect a route
@app.get("/protected-route")
async def protected_route(api_key: str = Depends(validate_api_key)):
    return {"message": "This is a protected route"}




## Installation

pip install -r requirements.txt

## Deployment

To deploy this project run

```python
   run main.py
```


## Documentation
This project documentation is available in the below link.
[Documentation](https://drive.google.com/file/d/1Z1Rnj3JTxQxbfphYmLrkL3ptpuQJB3MF/view?usp=sharing)


## Appendix

Any additional information goes here

System Architecture - 
https://github.com/smartinternz02/SI-GuidedProject-609045-1697906247/blob/e4023b9ab90ff0a2bc653057e789573680cf8500/Project_Design_phase/Solution%20Architecture.pdf

Machine Learning Model Details -
https://github.com/smartinternz02/SI-GuidedProject-609045-1697906247/blob/e4023b9ab90ff0a2bc653057e789573680cf8500/app/prediction%20model.ipynb

API Documentation - https://github.com/smartinternz02/SI-GuidedProject-609045-1697906247/tree/e4023b9ab90ff0a2bc653057e789573680cf8500/app

User Manual - https://github.com/smartinternz02/SI-GuidedProject-609045-1697906247/blob/e4023b9ab90ff0a2bc653057e789573680cf8500/Project_Development_Phase/Project_Manual.pdf

#key feautures

Early Smoke Detection

Reduced False Alarms

Remote Monitoring

Customization

Integration with Emergency Services

Adaptability 

Efficiency and Energy Conservation
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Used By

This project is used by the following companies:

- SMARTINTERNZ


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

We would like to express our gratitude to the open-source community and contributors for making FireGuard possible.
