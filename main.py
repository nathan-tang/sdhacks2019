import boto3
import credentials

         
def detect_labels_local_file(photo):

    client=boto3.client('rekognition', region_name='us-west-2', aws_access_key_id=credentials.access_key,
         aws_secret_access_key=credentials.secret_key)
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        
    return response['Labels']
    
        
    
def see_if_recyclable(itemList : list):
    recycle_list = ['Plastic', 'Bottle', 'Cardboard', 'Metal', 'Aluminum', 'Can', 'Glass', 'Battery']
    output = []
    for item in itemList:
        if item['Name'] in recycle_list:
            output.append((item['Name'], item['Confidence']))
    return output


def main():
    photo='C:\\Users\\Michael\\Desktop\\test.jpg'

    label_count=detect_labels_local_file(photo)
    #print("Labels detected: " + str(label_count))
    
    print(see_if_recyclable(label_count))
    
    


if __name__ == "__main__":
    main()