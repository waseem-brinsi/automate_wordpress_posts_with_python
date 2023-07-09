
from wordpress_xmlrpc import Client,WordPressPost
from wordpress_xmlrpc.methods import posts,media
from wordpress_xmlrpc.compat import xmlrpc_client
import json


print("Start ......")

client = Client('http://localhost/xmlrpc.php','wetcci','wassim1995')



filename = "./img1.jpg"

# prepare metadata
data = {
        'name': 'img1.jpg',
        'type': 'image/jpeg',  # mimetype
}

# read the binary file and let the XMLRPC library encode it into base64
with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

response = client.call(media.UploadFile(data))
print(response)

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


