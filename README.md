# EasyColab
Easy to use tools to be used on Google Colab. This Python package implements some of the most useful commands such as mounting Google drive folders, download of big files and zip/unzip files. 

## How to install
1. Open a Google Colab Session.
2. On a new cell, type:
```
!pip install easycolab
```
3. Try importing in order to check if the installation worked:
```
import easycolab as ec
```


## Implemented Features
Open the following link on Playground mode in order to test the implemented features: https://colab.research.google.com/drive/1hJYJpy4TtKUy2i7IK7YnIwk3kHhXe-WV

- Mount on Google Drive
```
>>> import easycolab as ec
>>> ec.mount()
```

- Unzip File
```
>>> import easycolab as ec
>>> ec.unzip(path)
```


- Download large files
```
>>> url = "https://raw.githubusercontent.com/mlampros/DataSets/master/cifar_10.zip"
>>> ec.download_large_file(url, target_path='cifar.zip')
```


