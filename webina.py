from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
import io
import subprocess 
from fastapi.responses import JSONResponse
import uvicorn
from typing import Union

# uvicorn.run(app, host="0.0.0.0")


    


#@app.get("/items/{item_id}")
#async def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}




# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")



# # @app.post("/analizar/")
# async def analyze_image (file: UploadFile = File(...)):
#     contents = await file.read()
#     with open("funka.py", "wb") as f:
#         f.write(contents)
#     result = subprocess.run(["python3", "funka.py"], capture_output=True, text=True)
#     return JSONResponse(content={"output": result.stdout})