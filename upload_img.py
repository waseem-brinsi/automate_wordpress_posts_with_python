
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media

def upload_img(client, files_out):
    for file in files_out :
            print(file)

            filename = "./img_out/"+file
            print(filename)
        # prepare metadata
            data = {
                "name": file,
                "type": "image/jpeg",  # mimetype
                "caption": "caption blabla",
                "description": "asdasdasdasd", 
        }

        # read the binary file and let the XMLRPC library encode it into base64
            with open(filename, 'rb') as img:
                    data['bits'] = xmlrpc_client.Binary(img.read())

            response = client.call(media.UploadFile(data))
            print(response)
    return response
