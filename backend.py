from flask import Flask, render_template, request
import base64
import re
import boto3
import credentials

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

    itemList = detect_labels_local_file('imageToSave.png')
    print("Labels detected: " + str(itemList))
    outputStr = 'System detected: '
    if len(is_recyclable(itemList)) == 0:
        outputStr += 'Item is not recyclable'
    else:
        for item in is_recyclable(itemList):
            outputStr += item[0] + ' with ' + str(round(item[1], 2)) + '% confidence\n'
        if len(is_recyclable(itemList)) > 1:
            outputStr += '\nItems are recyclable!'
        else: 
            outputStr += '\nItem is recyclable!'
    
    return outputStr       #whatever this returns is what is printed


def is_recyclable(itemList):
    recycleList = ['Plastic', 'Bottle', 'Cardboard', 'Metal', 'Aluminum', 'Can', 'Glass', 'Battery', 'Paper', 'Glass']
    recyclables = []
    for item in itemList:
        if item['Name'] in recycleList:
            recyclables.append((item['Name'], item['Confidence']))
    print(recyclables)
    return recyclables

def detect_labels_local_file(photo):
    client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id=credentials.access_key,
                          aws_secret_access_key=credentials.secret_key)

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    
    #print('Detected labels in ' + photo)
    #for label in response['Labels']:
        #print(label['Name'] + ' : ' + str(label['Confidence']))
        
    return response['Labels']

                        
if __name__ == '__main__':
    while True:
        app.run()
        