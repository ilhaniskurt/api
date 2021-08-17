import shutil
from zipfile import ZipFile
import os
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def index():
  return {"App":"task.py"}


@app.post("/file")
def check_file(file: UploadFile = File(...)):
  # Path variables
  filepath = "./files/" + file.filename
  tmpdirpath = "./files/tmp_" + file.filename[:-4] + "/"
  # Check Files Folder
  if not os.path.exists("./files"):
    os.mkdir("./files")
  # Download the file from user
  with open(filepath, 'wb') as buffer:
    shutil.copyfileobj(file.file, buffer)
  
  format = formatCheck(file, filepath, tmpdirpath)
  return format
  
def formatCheck(file, filepath, tmpdirpath):
  # Check Temp Path
  if not os.path.exists(tmpdirpath):
      os.mkdir(tmpdirpath)  
  # .apk check
  if file.filename.lower().endswith('.apk'):
    # alter format to .jar
    shutil.copyfile(filepath, tmpdirpath + file.filename[:-4]+".jar")
    # Unzip jar
    with ZipFile(tmpdirpath + file.filename[:-4] + ".jar", 'r') as zip_ref:
      zip_ref.extractall(tmpdirpath)
    # scan for 'classes.dex'
    if os.path.exists(tmpdirpath + "classes.dex"):
      # remove tmp
      shutil.rmtree(tmpdirpath)
      return {"filename":file.filename,"format":"APK","found":"classes.dex"}
    # remove tmp
    shutil.rmtree(tmpdirpath)
    return {"filename":file.filename,"format":"JAR"}
  return {"filename":file.filename,"format":"not supported"}