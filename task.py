import shutil
#import patoolib
#from zipfile import ZipFile
import os
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/file")
def check_file(file: UploadFile = File(...)):
  # Check Folder
  if not os.path.exists("./files"):
    os.mkdir("./files")
    
  # Download the file from user
  with open("./files/"+file.filename, 'wb') as buffer:
    shutil.copyfileobj(file.file, buffer)
  
  # .apk check
  if file.filename.lower().endswith('.apk'):
    # tmp copy
    if not os.path.exists("./files/tmp_"+file.filename[:-4]):
      os.mkdir("./files/tmp_"+file.filename[:-4])
    shutil.copyfile("./files/"+file.filename, "./files/tmp_"+file.filename[:-4]+"/"+file.filename[:-4]+".zip")
    
    #patoolib.extract_archive("./files/tmp_"+file.filename[:-4]+"/"+file.filename[:-4]+".rar", outdir="./files/tmp_"+file.filename[:-4])

    # Unzip with ZipFile 
    #with ZipFile("./files/tmp_"+file.filename[:-4]+"/"+file.filename[:-4]+".zip", 'r') as zip_ref:
      #zip_ref.extractall("./files/tmp_"+file.filename[:-4])
    return {"filename":file.filename,"extension":".apk"}
  
  return {"filename":file.filename}
