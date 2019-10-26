# Recycle Cam

## Project Description 
Recycle Cam is a web application which utilizes Amazon Web Service’s (AWS) Rekognition API in order to categorize items in a webcam as recyclable or non-recyclable. 

### Usage
To use <name>, you must have an AWS account. Create an access key and assign them in credentials.py file by using:

```
access_key = ‘yourAccessKey’
secret_key = ‘yourSecretKey’
```

Once specified, run the `backend.py` file and open the `127.9.9.1:5000` in a browser. The “Take a Picture” button will capture an image, and the web page will display whether any recyclable items were detected within the frame.

## How We Built It
(amazon web service) <-> (python interpreter) <-> (web application)
- Utilized Git for version history.
- Python Flask for a localhost web server
- HTML and CSS used to format the web application
- JavaScript to request and send data package between web and python.

## Challenges
The initial difficulty we faced was with incorporating AWS’s Rekognition API in with our code. After speaking with the AWS table for some set up help, we were able to access the API methods. Another challenge we ran into was setting up the frontend web page at first, because none of us were very familiar with HTML and JavaScript. After reading a lot of documentation and watching some tutorial videos, we were able to set up a basic page with usable buttons and the ability to take pictures and save them. We then ran into an issue with communication between the backend and frontend code. The majority of our difficulty stems from our lack of experience with all these different abstractions and layers. This allowed us to learn a lot more from building an entire application from the ground up.

## Relation to the Theme of Sustainability
Our web application can be used to differentiate waste that is recyclable and waste that is not. By utilizing our web application, recyclable wastes will not be mistakenly put into incorrect waste bins. This contributes to the idea of sustainability because nonbiodegradable waste will no longer be scattered around landfills and the environment. Additionally, we can repurpose recycled materials to limit the extraction of resources from the deteriorating Earth. 
