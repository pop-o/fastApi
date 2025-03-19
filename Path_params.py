from fastapi import FastAPI
from enum import Enum


class ModelName(str,Enum):
    alexnet="alexnet"
    vggnet="vggnet"
    mobilenet="mobilenet"

app = FastAPI()

#first try
@app.get('/')
async def first():
    return {"message":"hello world!"}

#parameters passed to the path.
@app.get('/items/{item_id}')
async def path_param(item_id:int):
    return {"item_id":item_id } 

@app.get('/users/me')
async def say_hello_to_current_user():
    return {"message":f"Hello active user"}

@app.get('/users/{username}')
async def say_hello_to_user(username:str):
    return {"message":f"hello {username}"}

@app.get('/users/{username}/{location}')
async def say_hello_to_user_with_location(username:str,location:str):
    return {"message":f"hello {username} from {location}"}


#predefined path values   
@app.get("/model/{model_name}")
async def model_details(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"Model":model_name,"Details":"Alexnet lol"}
    
    if model_name.value=="vggnet":
        return {"Model":model_name,"Details":"Vggnet lol"}
    
    if model_name is ModelName.mobilenet:
        return {"Model":model_name,"Details":"Mobilenet lol"}
    
    return {"Model":model_name,"Details":"No model name available"}


#file path to be sent
@app.get("/file/{file_path:path}")
async def get_file(file_path:str):
    return {"file_path":file_path}
    


