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
  # Check Folder
  if not os.path.exists("./files"):
    os.mkdir("./files")

  # Download the file from user
  filepath = "./files/" + file.filename
  tmpdirpath = "./files/tmp_" + file.filename[:-4] + "/"

  with open(filepath, 'wb') as buffer:
    shutil.copyfileobj(file.file, buffer)
  
  # .apk check
  if file.filename.lower().endswith('.apk'):
    # tmp copy
    if not os.path.exists(tmpdirpath):
      os.mkdir(tmpdirpath)
    # alter format
    shutil.copyfile(filepath, tmpdirpath + file.filename[:-4]+".jar")
    with ZipFile(tmpdirpath + file.filename[:-4] + ".jar", 'r') as zip_ref:
      zip_ref.extractall(tmpdirpath)

    # scan for 'classes.dex'
    if os.path.exists(tmpdirpath + "classes.dex"):
      # remove tmp
      shutil.rmtree(tmpdirpath)
      return {"filename":file.filename,"extension":".apk","found":"classes.dex"}
    # remove tmp
    shutil.rmtree(tmpdirpath)
    return {"filename":file.filename,"extension":".apk"}
  return {"filename":file.filename}