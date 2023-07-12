
import json
import os
import sys

from wordpress_xmlrpc import Client,WordPressPost
from wordpress_xmlrpc.methods import posts,media
from dotenv import load_dotenv


from img_resize import Img_Resize
from upload_img import upload_img


load_dotenv()
USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
print("Start ......")



client = Client(url='http://localhost/xmlrpc.php',username=USERNAME,password=PASSWORD)
try:
        os.mkdir('img_in')
except:
        pass

files_in = os.listdir('img_in') # list  of file in the directory

Img_Resize(files_in)

files_out = os.listdir('img_out')



response = upload_img(client, files_out)

print('9999999999999999999999999999')
print(response['id'])

attachment_id = response['id']


# Open the JSON file
with open('your_file.json') as file:
    # Load the contents of the file
    datajson = json.load(file)

# Access the data from the JSON file
print(datajson)


post = WordPressPost()

post.thumbnail = attachment_id
post.title = datajson["title"]
post.content = datajson["content"]
post.id = client.call(posts.NewPost(post))

# whoops, I forgot to publish it!
post.post_status = datajson["status"]
client.call(posts.EditPost(post.id, post))

print("Finish")


