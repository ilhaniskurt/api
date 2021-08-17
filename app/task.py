import shutil
#import patoolib
#from zipfile import ZipFile
import os
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def index():
  return {"App":"task.py"}


@app.post("/file")
def check_file(file: UploadFile = File(...)):
  # Check Folder
  if not os.path.exists("./files"):
    os.mkdir("./files")

  # Download the file from user
  filepath = "./files/" + file.filename
  tmpfilepath = "./file/tmp_" + file.filename[:-4]

  with open(filepath, 'wb') as buffer:
    shutil.copyfileobj(file.file, buffer)
  
  # .apk check
  if file.filename.lower().endswith('.apk'):
    # tmp copy
    if not os.path.exists(tmpfilepath):
      os.mkdir(tmpfilepath)
    # alter format
    shutil.copyfile(filepath, tmpfilepath +"/" + file.filename[:-4]+".zip")
    return {"filename":file.filename,"extension":".apk"}
  return {"filename":file.filename}






#patoolib.extract_archive("./files/tmp_"+file.filename[:-4]+"/"+file.filename[:-4]+".rar", outdir="./files/tmp_"+file.filename[:-4])
  # Unzip with ZipFile 
  #with ZipFile("./files/tmp_"+file.filename[:-4]+"/"+file.filename[:-4]+".zip", 'r') as zip_ref:
   #zip_ref.extractall("./files/tmp_"+file.filename[:-4])