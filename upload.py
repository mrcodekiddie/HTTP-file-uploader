import os
import requests
import base64

img_upload_url = "https://e-maligai.com/api/vsm_chrompet/imageUpload.php"
with open("me.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    post_req= requests.post(img_upload_url,data=
    {
        'icode':'i0011',
        'extension': '.png',
        'image': encoded_string
    }
    )
    print(post_req.text)

