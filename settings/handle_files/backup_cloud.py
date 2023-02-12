from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import sys
import os
import io



class Upload_cloud:
    def __init__(self):
        self.scopes =  ["https://www.googleapis.com/auth/drive"]
        self.credentials = None


    def token_validation(self):
        token_json = "settings/keys/token.json"
        credentials_json = "settings/keys/credentials.json"

        if os.path.exists(token_json):
            self.credentials = Credentials.from_authorized_user_file(token_json, self.scopes)
        
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())   
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_json, self.scopes)
                self.credentials = flow.run_local_server(port=0)

            with open(token_json, 'w') as self.token:
                self.token.write(self.credentials.to_json())
        
        
    def run_cloud(self, upload_folder:str, download_folder:str, out_path:str, folder_name:str):
        if upload_folder is not None:
            self.upload_cloud(upload_folder, folder_name)

        if download_folder is not None:
            self.download_cloud(download_folder, out_path)


    def upload_cloud(self, upload_folder:str, folder_name:str):
        self.token_validation()
        validation_file = []

        service = build("drive", "v3", credentials=self.credentials)
        response = service.files().list(q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'", spaces='drive').execute()
        
        if not response['files']:
            file_metadata = {
                "name": folder_name,
                "mimeType": "application/vnd.google-apps.folder"
            }
            folder_created = service.files().create(body=file_metadata, fields="id").execute()
            folder_id = folder_created.get('id') 
        else:
            folder_id = response['files'][0]['id']

        response_media_update = service.files().list(q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'").execute()
        folder_id_result = response_media_update.get('files', [])
        id_folder = folder_id_result[0].get('id')

        results = service.files().list(q=f"'{id_folder}' in parents").execute()
        items = results.get('files', [])

        if not items:
            for file in os.listdir(upload_folder): 
                sys.stdout.write(f"\r[+] Uploading file: {file}")
                sys.stdout.flush()

                file_settings = {"name": file, "parents": [folder_id]} 
                media_upload = MediaFileUpload(f'{upload_folder}/{file}', chunksize=1024 * 1024, resumable=True) 
                service.files().create(body=file_settings, media_body=media_upload, fields='id').execute()
            
            return sys.stdout.write('\n')

        for value in items:
            validation_file.append(value['name'])

        for file_name in os.listdir(upload_folder):
            for item in items:
                sys.stdout.write(f"\r[+] Uploading file: {file_name}")
                sys.stdout.flush()

                item_id = item.get('id')
                media_to_upload = MediaFileUpload(f'{upload_folder}/{file_name}', chunksize=1024 * 1024, resumable=True)
                try:
                    if file_name not in validation_file:
                        file_settings = {"name": file_name, "parents": [folder_id]}
                        service.files().create(body=file_settings, media_body=media_to_upload, fields='id').execute()
                        break
                    service.files().update(fileId=item_id, media_body=media_to_upload).execute()
                    break
                except Exception as err:
                    print(f'Failed to upload {file_name}: {err}')
                    
        return sys.stdout.write('\n')
                    

    def download_cloud(self, download_folder:str, out_path:str):
        self.token_validation()

        service = build("drive", "v3", credentials=self.credentials)
        folder_id = service.files().list(q=f"mimeType = 'application/vnd.google-apps.folder' and name = '{download_folder}'").execute()

        if not folder_id['files']:
            print(f"[-] Invalid folder name: -df {download_folder}")
            return False

        folder_id_result = folder_id.get('files', [])
        id_folder = folder_id_result[0].get('id')

        results = service.files().list(q=f"'{id_folder}' in parents").execute()
        items = results.get('files', [])

        if not os.path.isdir(f'{out_path}/{download_folder}'):
            os.makedirs(f'{out_path}/{download_folder}')

        for _, item in enumerate(items):
            file_id = item.get('id')
            file_name = item.get('name')
            file_request = service.files().get_media(fileId=file_id)
            file_han = io.BytesIO()
            download_midia = MediaIoBaseDownload(file_han, file_request)

            done = False
            while done is False:
                _, done = download_midia.next_chunk()
                sys.stdout.write(f"\r[+] Downloading file: {file_name}")
                sys.stdout.flush()

            file_han.seek(0)
            with open(os.path.join(f'{out_path}/{download_folder}/{file_name}'), 'wb') as file:
                file.write(file_han.read())
                file.close()
        
        return sys.stdout.write('\n')