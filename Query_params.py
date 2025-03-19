from fastapi import FastAPI


app = FastAPI()
#query params
fake_db=[
            {"item_name":"momo"},
            {"item_name":"naan"},
            {"item_name":"laphing"},           
            {"item_name":"samosa"},           
        ]    

    

@app.get("/item/")
async def query_param(skip:int=0,limit:int=10):
    return fake_db[skip:skip+limit]

@app.get("/location/{location_name}")
async def get_location_detail(location_name:str,is_available: bool | None =True):
    if is_available == True:
        return {f"Location {location_name} is available"}
    else:
        return {f"Location {location_name} is not available"}
    
@app.get("/college/{college_name}/{course_name}")
async def get_course_details(college_name:str,course_name:str,course_price:int | None = None,is_availabe:bool | None=False):
    if is_availabe == True:
        if course_price:
            return f"{course_name} is available at {college_name} for {course_price}"
        else:
            return f"{course_name} is available at {college_name}"
    else:
        return f"{course_name} is not available at {college_name}"