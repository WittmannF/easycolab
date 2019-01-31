# EasyColab
Easy access to the most useful commands of Google Colab. This Python package is like an API for simplifying some commands that have to be used all the time when initializing Colab sections such as mounting Google drive folders, download of big files and zip/unzip files. 

## How to install
1. Open a Google Colab Session.
2. On a new cell, type:
```
!pip install easycolab
```
3. Try importing easycolab to check if the installation worked:
```
import easycolab as ec
```


## Implemented Features
Open the following link on Playground mode in order to test the implemented features: https://colab.research.google.com/drive/1hJYJpy4TtKUy2i7IK7YnIwk3kHhXe-WV

- Mount on Google Drive
```
>>> ec.mount()
```

- Open Google Drive folder:

```
>>> ec.openmydrive()
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

## Licence
MIT
