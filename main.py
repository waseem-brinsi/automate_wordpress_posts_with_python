
from wordpress_xmlrpc import Client,WordPressPost
from wordpress_xmlrpc.methods import posts,media
from wordpress_xmlrpc.compat import xmlrpc_client
import json
import os


print("Start ......")

client = Client(url='http://localhost/xmlrpc.php',username='wetcci',password='wassim1995')


files = os.listdir('img') 

for file in files :
        print(file)

        filename = "./img/"+file
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












# attachment_id = response['id']


# # Open the JSON file
# with open('your_file.json') as file:
#     # Load the contents of the file
#     datajson = json.load(file)

# # Access the data from the JSON file
# print(datajson)


# post = WordPressPost()

# post.thumbnail = attachment_id
# post.title = datajson["title"]
# post.content = datajson["content"]
# post.id = client.call(posts.NewPost(post))

# # whoops, I forgot to publish it!
# post.post_status = datajson["status"]
# client.call(posts.EditPost(post.id, post))

print("Finish")


