from settings.handle_files.backup_cloud import Upload_cloud
from settings.handle_files.handle_file import Handle_files
import argparse



class Validation_input:
    def __init__(self):
        self.cloud_upload = Upload_cloud()
        self.handle_files = Handle_files()

        self.args = self.parse_args()

        self.encryption = self.args.encryption
        self.decryption = self.args.decryption
        self.cloud = self.args.cloud

        self.folder = self.args.folder
        self.password = self.args.password
        self.out_path = self.args.output

        self.upload_folder = self.args.upload_folder
        self.folder_name = self.args.folder_name
        self.download_folder = self.args.download_folder


    def parse_args(self):
        parser = argparse.ArgumentParser(description="Application of file Encryption and Decryption with inbuilt upload to the cloud")

        folder_status = parser.add_argument_group('Folder-Options')
        folder_status.add_argument("-e","--encryption", action='store_true', help="enable status for encryption of files")
        folder_status.add_argument("-d","--decryption", action='store_true', help="enable status for decryption of files")
        folder_status.add_argument("-c", "--cloud", action='store_true', help="Enable upload files to the Cloud")

        folder_settings = parser.add_argument_group('Folder-path/key')
        folder_settings.add_argument("-f", "--folder", type=str, help="Path to the directory")
        folder_settings.add_argument("-p","--password", type=str, help="Password for symmetric encryption of files")
        folder_settings.add_argument("-o","--output", type=str, help="output the files to a chosen path")

        cloud_settings = parser.add_argument_group('Cloud-Settings')
        cloud_settings.add_argument("-uf", "--upload_folder", type=str, help="Path to the folder to upload to the cloud")
        cloud_settings.add_argument("-fn","--folder_name", type=str, help="folder name to upload to cloud")
        cloud_settings.add_argument("-df","--download_folder", type=str, help="Path to download folder in the cloud")

        return parser.parse_args()


    def run(self):   
        if self.validation_commands():
            return self.usage_commands()

        if self.encryption and self.validate_encryption():
            self.handle_files.get_encrypt_zip_file(self.folder, self.out_path, self.password)

        if self.decryption and self.validate_decryption():
            self.handle_files.get_decrypt_file(self.folder, self.out_path, self.password)

        if self.cloud and self.validate_cloud_upload():
            self.cloud_upload.run_cloud(self.upload_folder, self.download_folder, self.out_path, self.folder_name)


    def validate_encryption(self):
        if self.folder is not None and self.password is not None and self.out_path is not None:
            return True

        print('[+] Usage: python3 run.py -e -f path/to/folder -p Mypassword -o out/put/folder')

        return False


    def validate_decryption(self):
        if self.decryption and self.folder is not None and self.password is not None and self.out_path is not None:
            return True

        print('[+] Usage: python3 run.py -d -f path/to/folder -p Mypassword -o out/put/folder')

        return False


    def validate_cloud_upload(self):
        if self.cloud and self.upload_folder is not None and self.folder_name is not None:
            return True
        elif self.cloud and self.download_folder is not None and self.out_path is not None:
            return True

        print('[+] Usage: python3 run.py -c -uf path/to/folder -fn MyfolderName')
        print('[+] Usage: python3 run.py -c -df path/folder/to/cloud -o output/folder/of/cloud')
        
        return False


    def validation_commands(self):
        if self.encryption is False and self.decryption is False and self.cloud is False:
            return True


    def usage_commands(self):
        print("[+] Usage: python3 run.py -e -f path/to/folder -p Mypassword -o out/put/folder")
        print("[+] Usage: python3 run.py -d -f path/to/folder -p Mypassword -o out/put/folder")
        print("[+] Usage: python3 run.py -c -uf path/to/folder -fn MyfolderName")
        print("[+] Usage: python3 run.py -c -df path/folder/to/cloud -o output/folder/of/cloud")