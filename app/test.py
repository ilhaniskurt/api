from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Personel(BaseModel):
  level: int
  name: str
  title: str

class UpdatePersonel(BaseModel):
  level: Optional[int] = None
  name: Optional[str] = None
  title: Optional[str] = None

personels = {
  1: {
      "level" : 1, 
      "name" : "ilhan",
      "title" : "admin"
      }
}


@app.post("/create-personel/{personel_id}")
def create_personel(personel_id: int, personel: Personel):
  if personel_id in personels:
    return {"Error":"Personel already exists"}
  personels[personel_id] = personel
  return {"Success":"Personel created"}

@app.put("/update-personel/{personel_id}")
def update_personel(personel_id: int, personel: UpdatePersonel):
  if personel_id not in personels:
    return {"Error","Personel does not exist"}
  
  if personel.name != None:
    personels[personel_id]["name"] = personel.name

  if personel.level != None:
    personels[personel_id]["level"] = personel.level

  if personel.title != None:
    personels[personel_id]["title"] = personel.title

  return {"Success":"Personel updated"}

@app.delete("/delete-personel/{personel_id}")
def delete_personel(personel_id: int):
  if personel_id not in personels:
    return {"Error":"Personel does not exist"}
  
  del personels[personel_id]
  return {"Success":"Personel has been deleted"}

@app.get("/")
def index():
  return {"App":"test.py"}

@app.get("/get-personel/{personel_id}")
def get_personel(personel_id: int = Path(None, description="Personel ID", gt=0, le=len(personels)+1 )):
  if personel_id not in personels:
    return {"Error":"Personel does not exist"}
  return personels[personel_id] 

@app.get("/get-personel-by")
def get_personel_by(title : Optional[str] = None):
  for personel_id in personels:
    if personels[personel_id]["title"] == title:
      return personels[personel_id]
  return {"Data":"404 Not Found"}