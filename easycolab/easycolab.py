from google.colab import drive
import os

__all__ = ["mount", "download_large_file", "unzip", "zip", "openmydrive"]

def mount(path='/content/gdrive'):
    drive.mount(path)

import requests
def download_large_file(url, target_path='out.zip'):
  # Download the file if it does not exist
  if not os.path.isfile(target_path):
    response = requests.get(url, stream=True)
    handle = open(target_path, "wb")
    print('Downloading...')
    for chunk in response.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    print('Done!')
  else:
    print('File already exists')

import zipfile
def unzip(zip_path, destination_path='.'):
  with zipfile.ZipFile(zip_path,"r") as zip_ref:
      zip_ref.extractall(destination_path)

import shutil
def zip(filename, root_dir, extension='zip'):
    shutil.make_archive(filename, extension, root_dir)

def openmydrive():
    try:
        os.system("cd /content/gdrive/My Drive/")
    except:
        print('command unsuccessfull')

