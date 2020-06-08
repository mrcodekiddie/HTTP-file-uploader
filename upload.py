import os
import requests
import base64
import sys
from sys import argv as argument
from pathlib import Path

try:
    file_path=Path(argument[1])
    if(file_path.is_file()):
        print(file_path)
        img_upload_url = "https://e-maligai.com/api/vsm_chrompet/imageUpload.php"
        with open(str(file_path), "rb") as image_file:
            
            file_name=str(file_path)[::-1].split("/")[0][::-1].split(".")[0]
            file_extension=str(file_path)[::-1].split("/")[0][::-1].split(".")[1]

            print(file_name+file_extension)
            encoded_string = base64.b64encode(image_file.read())
            post_req= requests.post(img_upload_url,data=
            {
                'icode':file_name,
                'extension': file_extension,
                'image': encoded_string
            }
            )
            print(post_req.text)
    else:
        print("provide a valid image path")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

