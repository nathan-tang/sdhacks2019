from flask import Flask, render_template, request
import base64
import re
import boto3
import credentials

app = Flask(__name__)

@app.route('/')
def request_image(): 
    return render_template('webpage.html')

@app.route('/', methods=['POST'])
def get_image():
    image_b64 = request.values['imageBase64']
    image_data = re.sub(r'^data:image/.+;base64,', '', image_b64)
    img = base64.b64decode(image_data)
    with open('imageToSave.png', 'wb') as fh:
        fh.write(img)

    label_count = detect_labels_local_file('imageToSave.png')
    print("Labels detected: " + str(label_count))
    return image_data

def detect_labels_local_file(photo):
    client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id=credentials.access_key,
                          aws_secret_access_key=credentials.secret_key)

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('Detected labels in ' + photo)
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

    return len(response['Labels'])

if __name__ == '__main__':
    while True:
        app.run()