# Backup-app-google-driver

## Overview
* A Backup application to upload files with encryption to the google drive.

## Get Google Drive API
  https://developers.google.com/drive/api/quickstart/python?hl=en
  
  if you still need help to get the api key :
  https://www.youtube.com/watch?v=fkWM7A-MxR0&t=661s&ab_channel=NeuralNine
    

## Run locally
Install dependencies in a virtual environment is recommended.

### Virtual environment and Libraries in Linux/Windows:

```python 
Linux:
  python3 -m venv env
  source ./env/bin/activate
  pip3 install -r requirements.txt
  deactivate
  
Windows:
  python3 -m venv env
  .\env\Scripts\activate
  pip3 install -r requirements.txt
  deactivate
```
## Usage:

```shell
Usage: run.py [-h] [-e] [-d] [-c] [-f FOLDER] [-p PASSWORD] [-o OUTPUT] [-uf UPLOAD_FOLDER] [-fn FOLDER_NAME] [-df DOWNLOAD_FOLDER]

Application of file Encryption and Decryption with inbuilt upload to the cloud

options:
  -h, --help            show this help message and exit

Folder-Options:
  -e, --encryption      enable status for encryption of files
  -d, --decryption      enable status for decryption of files
  -c, --cloud           Enable upload files to the Cloud

Folder-path/key:
  -f FOLDER, --folder FOLDER
                        Path to the directory
  -p PASSWORD, --password PASSWORD
                        Password for symmetric encryption of files
  -o OUTPUT, --output OUTPUT
                        output the files to a chosen path

Cloud-Settings:
  -uf UPLOAD_FOLDER, --upload_folder UPLOAD_FOLDER
                        Path to the folder to upload to the cloud
  -fn FOLDER_NAME, --folder_name FOLDER_NAME
                        folder name to upload to cloud
  -df DOWNLOAD_FOLDER, --download_folder DOWNLOAD_FOLDER
                        Path to download folder in the cloud
```


## Example commands

### Encrypt files to be uploaded
```
python3 run.py -e -f path/to/folder -p Mypassword -o out/put/folder
```
### Decrypt files encrypted
```
python3 run.py -d -f path/to/folder -p Mypassword -o out/put/folder
```
### Upload files to the cloud
```
python3 run.py -c -uf path/to/folder -fn MyfolderName
```
### Downloads files from the cloud

```
python3 run.py -c -df path/folder/to/cloud -o output/folder/of/cloud
```

## License

* See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).


## :mortar_board: Author



<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/Alanghj">
                <img src="https://user-images.githubusercontent.com/81534309/151803029-df474faf-bb04-4c5b-8b0d-072d7b4b40b1.png" width="150px;" alt="Image Alanghj" />
                <br />
                <sub><b>Alanghj</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   Made by <a href="/" target="#"> Alanghj</a>
</h4>
